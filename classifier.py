from fastai.imports import *
from fastai.vision import *

# path to the folder
PATH = '/Users/Danny/fast.ai/Baseball_V_Tennis/baseball_vs_tennis/'

# has to have the following structure
'''
.
└── baseball_vs_tennis
    ├── train
    │   ├── baseball
    │   │   ├── pix of baseball stuff to train model
    │   └── tennis
    │       ├── pix of tennis stuff to train model
    └── valid
        ├── baseball
        │   ├── pictures of baseball stuff to TEST model
        └── tennis
            ├── pictures of tennis stuff to TEST model

'''
