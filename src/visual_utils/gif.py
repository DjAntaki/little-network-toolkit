
#!/usr/bin/env python

def reverse_gif(filename):
    """
    Given a gif composed of a sequence of fixed-duration frames and tha

    taken from http://stackoverflow.com/questions/753190/programmatically-generate-video-or-animated-gif-in-python

    """
    from PIL import Image, ImageSequence
    import sys, os
    filename = sys.argv[1]
    im = Image.open(filename)
    original_duration = im.info['duration']
    frames = [frame.copy() for frame in ImageSequence.Iterator(im)]
    frames.reverse()

    from images2gif import writeGif
    writeGif("reverse_" + os.path.basename(filename), frames, duration=original_duration/1000.0, dither=0)

def make_gif(frame_sequence):
    raise NotImplementedError()