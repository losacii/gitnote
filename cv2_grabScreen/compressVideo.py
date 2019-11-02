import os

files = os.listdir('.')
for f in files:
    if f.endswith('.mp4'):
        print("\n--------> Compressing", f)
        os.system("ffmpeg -i {} -vcodec libx265 -crf 24 {}".format(f, '_'+f))

# ffmpeg -i input.mp4 -vcodec libx265 -crf 24 output.mp4


