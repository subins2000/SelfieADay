import os
import glob
from PIL import Image
from PIL.ExifTags import TAGS
import time


def get_exif(fn):
    ret = {}
    i = Image.open(fn)
    info = i._getexif()
    for tag, value in info.items():
        decoded = TAGS.get(tag, tag)
        ret[decoded] = value
    return ret


def make_square(im, min_size=1000, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    min_size = x if x > y else y
    size = max(min_size, x, y)
    new_im = Image.new('RGB', (size, size), fill_color)
    new_im.paste(im, ((size - x) // 2, (size - y) // 2))
    return new_im


os.chdir('input')

files = glob.glob('*.jpg')

for file in files:
    print(file)
    time = get_exif(file)['DateTimeOriginal']

    time = time.replace(':', '')
    time = time.replace(' ', '_')
    new_name = time + '.jpg'

    os.rename(file, new_name)

    # Resize images

    im = Image.open(new_name)
    imResize = make_square(im)
    imResize.save(new_name, 'JPEG', quality=100)
