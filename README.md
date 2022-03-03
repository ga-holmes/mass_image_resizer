# Mass Image Resize

Just another little tool I made for personal use that I'm throwing up here.
Will resize any jpg/png images to the specified width and scale the y value accordingly to maintain the aspect ratio.
Pretty straightforward. I made this to resize images quickly to put on my website so they load faster.
Might do more later like overlaying a watermark (i think that's possible with opencv?).

## Use
    - `python resize_img.py`
    - pick image file(s)
    - enter x/width number (ex. 1080)
    - output file is 'resize_filename '

## requirements
    - Requires opencv
    - install with `pip install opencv-python`