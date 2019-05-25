import math
import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
from resizeimage import resizeimage
import time


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret

os.chdir('input')

files = glob.glob('*.jpg')

count = 0
for file in files:
    time = get_exif(file)['DateTimeOriginal']

    time = time.replace(':', '')
    time = time.replace(' ', '_')
    new_name = time + '.jpg'

    os.rename(file, new_name)

    # Resize images

    im = Image.open(new_name)
    exif = im.info['exif']

    cover = resizeimage.resize_contain(im, [2500, 2500], bg_color=(0,0,0,1))
    cover.save(new_name, im.format, quality=100, exif=exif)

    print(str(count) + ' - ' + file)
    count += 1
