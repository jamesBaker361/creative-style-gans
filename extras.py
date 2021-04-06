import random

all_genres=['abstract-expressionism', 'action-painting', 'analytical-cubism', 'art-nouveau-modern', 'baroque', 'color-field-painting', 'contemporary-realism', 'cubism', 'early-renaissance', 'expressionism', 'fauvism', 'high-renaissance', 'impressionism', 'mannerism-late-renaissance', 'minimalism', 'na-ve-art-primitivism', 'new-realism', 'northern-renaissance', 'pointillism', 'pop-art', 'post-impressionism', 'realism', 'rococo', 'romanticism', 'symbolism', 'synthetic-cubism', 'ukiyo-e']

renn_genres=['high-renaissance',  'early-renaissance',  'northern-renaissance','mannerism-late-renaissance']

style_blocks=['block1_conv1','block2_conv1','block3_conv1','block4_conv1','block5_conv1']
style_block_shapes=[(1, 64, 64),(1, 128, 128),(1, 256, 256),(1, 512, 512),(1, 512, 512)]

def random_genres(num=4):
    return(random.sample(all_genres,num))