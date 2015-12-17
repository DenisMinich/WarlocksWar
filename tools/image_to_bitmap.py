import cv2
import getopt
import numpy
import sys

DEFAULT_DELIMETER = ','


def convert_image_to_bitmap(img_name, bitmap_name, delimiter):
    img = cv2.imread(img_name, 0)
    ret, thresh = cv2.threshold(img, 10, 255, cv2.THRESH_BINARY)
    thresh.dtype = bool
    numpy.savetxt(bitmap_name, thresh, delimiter=delimiter, fmt="%5i")


def main(argv):
    img = ''
    bitmap = ''
    delimiter = DEFAULT_DELIMETER
    try:
        opts, args = getopt.getopt(argv, "i:b:d:", [
            "img=", "bitmap=", "delimiter="])
    except getopt.GetoptError:
        print('image_to_bitmap.py -i <image> -b <bitmap> -d <delimiter>')
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-i", "--img"):
            img = arg
            bitmap = "{img_name}.csv".format(img_name=arg[:-4])
        if opt in ("-b", "--bitmap"):
            bitmap = arg
        if opt in ("-d", "--delimiter"):
            delimiter = arg
    convert_image_to_bitmap(img, bitmap, delimiter)


if __name__ == "__main__":
    main(sys.argv[1:])
