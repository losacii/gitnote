import os

files = os.listdir('.')
for f in files:
    if f.endswith('.mp4'):
        print("\n--------> Compressing", f)
        #os.system("ffmpeg -i {} -vcodec libx265 -crf 24 {}".format(f, '_'+f))
        os.system("ffmpeg -i {} -b 255000 {}".format(f, '_'+f))
        os.system("rm {}".format(f))
        

# ffmpeg -i input.mp4 -vcodec libx265 -crf 24 output.mp4


