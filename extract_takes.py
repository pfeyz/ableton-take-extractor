"Groups takes from an ableton session into directories"
from __future__ import print_function

import shutil
import argparse
from collections import defaultdict
from os import path, mkdir
from xml.etree.ElementTree import ElementTree, ParseError

parser = argparse.ArgumentParser(description=("Extract takes from an "
                                              "Abelton Live session file"))
parser.add_argument('-c', '--copy', action='store_true',
                    help=("Copy the files to the target directory, "
                          "defaults to showing you what would happen"))
parser.add_argument('-o', '--overwrite', action='store_true',
                    help=("Overwrite existing files "
                          "Default is to stop and raise an error"))
parser.add_argument('session', help="The Ableton ALS (XML) file to parse")
parser.add_argument('source', help="The directory containing the audio files")
parser.add_argument('target_dir', help="The directory to copy the takes to")

def get_samples(tree):
    return [name.get("Value")
            for name in tree.findall(".//SampleRef/FileRef/Name")]

def get_clips(tree):
    clips = defaultdict(list)
    for clip in tree.findall(".//AudioClip"):
        clips[clip.attrib["Time"]].append(clip)
    return clips

def match_sample(prefix, samples, suffix=".wav"):
    for sample in samples:
        if sample.endswith(prefix + suffix):
            return sample
    raise Exception("Couldn't find {0}".format(prefix))

def clip_to_sample(clip_dict, samples):
    for i, (time, clips) in enumerate(clip_dict.items()):
        for j, clip in enumerate(clips):
            c = clip_dict[time][j]
            if c is not None:
                x = c.find("Name").attrib["Value"]
                clip_dict[time][j] = match_sample(x, samples)

if __name__ == "__main__":
    args = parser.parse_args()
    try:
        tree = ElementTree(file=args.session)
    except ParseError:
        raise Exception("{0} appears to be corrupted".format(args.session))
    samples = get_samples(tree)
    clips = get_clips(tree)
    clip_to_sample(clips, samples)
    sorted_clips = sorted(clips.items(), key=lambda x: float(x[0]))
    for num, (time, cs) in enumerate(sorted_clips):
        take = "take-" + format(num + 1,
                                "0{0}d".format(len(sorted_clips)/10))
        destination = path.join(args.target_dir, take)
        if args.copy:
            try:
                mkdir(destination)
            except OSError as e:
                if e.errno == 17:
                    if not args.overwrite:
                        raise Exception("Directory '{0}' exists. "
                    "Run with -o to overwrite.".format(destination))
                else:
                    raise e
        for c in cs:
            source = path.join(args.source, c)
            file_destination = path.basename(source)
            target_file = path.join(args.target_dir, take,
                                    file_destination)
            if args.copy:
                if path.exists(target_file):
                    if not args.overwrite:
                        raise Exception("File '{0}' exists. Run with "
                        "-o to overwrite.".format(target_file))
                shutil.copy2(source, target_file)
            print(source, "-->", target_file)
        print()
    if not args.copy:
        print("* If this looks right run it again with -c to copy the files")
        print()
