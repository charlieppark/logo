from PIL import Image
from os import listdir
from os.path import isfile, join

files = [f for f in listdir('./') if isfile(join('./', f))]

for filename in files:
    if filename[-1] == 'g':
        im1 = Image.open(filename)
        im1.save(f'{filename[:-4]}.png')
