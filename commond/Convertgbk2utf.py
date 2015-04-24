# -*- coding:utf-8 -*-
__author__ = 'tsbc'

import os,sys
import chardet

def convert( filename, in_enc = "GBK", out_enc="UTF8" ):
    try:
        print "convert " + filename,
        content = open(filename).read()
        result = chardet.detect(content)
        coding = result.get('encoding')
        if coding != 'utf-8':
            print coding + "to utf-8!",
            new_content = content.decode(in_enc).encode(out_enc)
            open(filename, 'w').write(new_content)
            print " done"
        else:
            print coding
    except IOError,e:
    # except:
        print " error"


def explore(dir):
    for root, dirs, files in os.walk(dir):
        for file in files:
            path = os.path.join(root, file)
            convert(path)

def main():
    for path in sys.argv[1:]:
        if os.path.isfile(path):
            convert(path)
        elif os.path.isdir(path):
            explore(path)

if __name__ == "__main__":
    main()