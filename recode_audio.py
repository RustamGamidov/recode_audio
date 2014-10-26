#!/usr/bin/env python2

import os
import argparse
import datetime


def is_audio(fname):
    if not os.path.isfile(fname):
        return False
    name, extension = os.path.splitext(fname)
    if not extension:
        return False
    audio_ext = ['.mp3', '.ogg', '.flac', '.m4a', '.ape', '.mv']
    if extension not in audio_ext:
        return False
    return True


def recode2ogg(fname):
    name, extension = os.path.splitext(fname)
    print datetime.datetime.now(), ":: Encoding to OGG:", fname
    metadataname = name + '.txt'
    os.system('ffmpeg -i "' + fname + '" -f ffmetadata "' + metadataname + '"')
    outname = name + '.ogg'
    os.system('ffmpeg -i "' + fname + '" -f wav - | oggenc -q6 - > "' + outname + '"')
    os.system('vorbiscomment -a "' + outname + '" -c "' + metadataname + '"')


def main():
    parser = argparse.ArgumentParser(
        description='Recodes given audion to OGG Vorbisi')
    parser.add_argument(
        'fname', metavar='audio_filr_names', type=str, nargs='+',
        help='files to recode')
    cmd_args = parser.parse_args()

    for name in cmd_args.fname:
        if not is_audio(name):
            continue
        print name
        recode2ogg(os.path.abspath(name))


if __name__ == '__main__':
    main()
