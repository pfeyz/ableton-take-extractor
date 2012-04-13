=============================
 Ableton Live Take Extractor
=============================

You've recorded a bunch of live multitrack takes in Ableton Live and want to
easily group the audio files by take. Tell this script where to find your
Ableton Session file, the directory where the samples are located, and where you
want them to go. It will make a directory for each take with its samples within.

This assumes that all takes are sequential- that every take has a unique start
time in the project. If you've dragged one take to start at the same instant as
another, this won't work correctly.

Example
=======

Here I have an Ableton Live session, mysession.als in my current working
directory, the audio files Ableton wrote to disk in
/media/audio/Samples/Recoreded/, and I want the organized takes to end up in
/media/takes.

::

  $ python extract_takes.py mysession.als /media/audio/Samples/Recorded/ /media/takes

  /media/audio/Samples/Recorded/0008 COLIN e22-anamod 1.wav --> /media/takes/take-01/0008 COLIN e22-anamod 1.wav
  /media/audio/Samples/Recorded/0002 MIKE cab.wav --> /media/takes/take-01/0002 MIKE cab.wav
  /media/audio/Samples/Recorded/0002 KICK-anamod 2.wav --> /media/takes/take-01/0002 KICK-anamod 2.wav
  /media/audio/Samples/Recorded/0002 FT.wav --> /media/takes/take-01/0002 FT.wav
  /media/audio/Samples/Recorded/0002 OV.wav --> /media/takes/take-01/0002 OV.wav
  /media/audio/Samples/Recorded/0002 ROOM.wav --> /media/takes/take-01/0002 ROOM.wav

  /media/audio/Samples/Recorded/0009 COLIN e22-anamod 1.wav --> /media/takes/take-02/0009 COLIN e22-anamod 1.wav
  /media/audio/Samples/Recorded/0003 MIKE cab.wav --> /media/takes/take-02/0003 MIKE cab.wav

  ...

  * If this looks right run it again with -c to copy the files

  $ python extract_takes.py -c mysession.als /media/audio/Samples/Recorded/ /media/takes

  /media/audio/Samples/Recorded/0008 COLIN e22-anamod 1.wav --> /media/takes/take-01/0008 COLIN e22-anamod 1.wav
  /media/audio/Samples/Recorded/0002 MIKE cab.wav --> /media/takes/take-01/0002 MIKE cab.wav
  /media/audio/Samples/Recorded/0002 KICK-anamod 2.wav --> /media/takes/take-01/0002 KICK-anamod 2.wav
  /media/audio/Samples/Recorded/0002 FT.wav --> /media/takes/take-01/0002 FT.wav
  /media/audio/Samples/Recorded/0002 OV.wav --> /media/takes/take-01/0002 OV.wav
  /media/audio/Samples/Recorded/0002 ROOM.wav --> /media/takes/take-01/0002 ROOM.wav

  /media/audio/Samples/Recorded/0009 COLIN e22-anamod 1.wav --> /media/takes/take-02/0009 COLIN e22-anamod 1.wav
  /media/audio/Samples/Recorded/0003 MIKE cab.wav --> /media/takes/take-02/0003 MIKE cab.wav

  ...

The takes are now grouped in /media/takes/take-01, take-02 etc.

Usage
=====

::

  usage: extract_takes.py [-h] [-c] [-o] session source target_dir

  Extract takes from an Abelton Live session file

  positional arguments:
    session          The Ableton ALS (XML) file to parse
    source           The directory containing the audio files
    target_dir       The directory to copy the takes to

  optional arguments:
    -h, --help       show this help message and exit
    -c, --copy       Copy the files to the target directory, defaults to showing
                     you what would happen
    -o, --overwrite  Overwrite existing files Default is to stop and raise an
                     error
