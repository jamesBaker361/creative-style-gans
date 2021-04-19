import tensorflow as tf
import pathlib
import os
import numpy as np
from extras import *
from tqdm import tqdm

np.set_printoptions(precision=4)

def dataset_limited(genres,limit=10,shuffle=True,folder='wikiartimages/stylematricesminmax/'):
    np_arrs={s:[] for s in style_blocks}
    labels=[]
    for genre in genres:
        mypath=os.path.join(os.getcwd(),folder+genre)
        files= [f for f in os.listdir(mypath) if f.endswith('.npz')]
        if shuffle is True:
            np.random.shuffle(files)
        pbar=tqdm(files[:limit])
        for file in pbar:
            joined_path=os.path.join(mypath,file)
            pbar.set_description(genre+'/'+file)
            npz=np.load(joined_path)
            for k in npz.keys():
                np_arrs[k].append(npz[k])
            labels.append(genre)
    matrices=tuple([np_arrs[s] for s in style_blocks])
    return tf.data.Dataset.from_tensor_slices((labels,matrices))

def dataset_batched(genres,limit=10,shuffle=True,batch_size=10,folder='wikiartimages/stylematricesminmax/'):
    d_set=dataset_limited(genres,limit=limit,shuffle=shuffle,folder=folder)
    genre_lookup={}
    for g in range(len(genres)):
        genre_lookup[genres[g]]=[0 for _ in range(len(genres))]
        genre_lookup[genres[g]][g]=1
    labels=[]
    mats=[[]  for _ in range(5)]
    for label,matrices in d_set:
        name=str(label.numpy())[2:-1]
        labels.append(genre_lookup[name])
        for i,m in zip(range(5),matrices):
            new_shape=(m.shape[1],m.shape[2],1)
            mats[i].append(tf.reshape(m,new_shape))
    label_data=tf.data.Dataset.from_tensor_slices(labels).batch(batch_size)
    mats_data=[tf.data.Dataset.from_tensor_slices(m).batch(batch_size) for m in mats]
    return label_data,mats_data

def dataset_all(genres,shuffle=True,folder='wikiartimages/stylematrices/'):
    np_arrs={s:[] for s in style_blocks}
    labels=[]
    for genre in genres:
        mypath=os.path.join(os.getcwd(),folder+genre)
        files= [f for f in os.listdir(mypath) if f.endswith('.npz')]
        if shuffle is True:
            np.random.shuffle(files)
        for file in tqdm(files):
            npz=np.load(os.path.join(mypath,file))
            for k in npz.keys():
                np_arrs[k].append(npz[k])
            labels.append(genre)
    matrices=tuple([np_arrs[s] for s in style_blocks])
    return tf.data.Dataset.from_tensor_slices((labels,matrices))