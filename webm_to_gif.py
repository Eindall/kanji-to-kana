#!/usr/bin/env python3

import ffmpeg
import os, sys
import re

def webm_to_gif(input_filename, output_filename):
    input_format = re.search("(\.[a-z]+)$", input_filename).group()
    output_format = re.search("(\.[a-z]+)$", output_filename).group()

    process = (
        ffmpeg
        .input(input_filename, f=input_format[1:])
        .output(output_filename, f=output_format[1:], pix_fmt="rgb24")
        .run_async()
    )

    _, cerr = process.communicate(input=sys.stdout) # Streams standard output and stores error output
    process.wait() # Wait until process finishes

    if (cerr):
        print(cerr)