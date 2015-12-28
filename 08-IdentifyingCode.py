from PIL import Image

image_name = r'result\08-IdentifyingCode\test1.jpg'

sx = 20
sy = 16
ex = 8
ey = 10
st = 20

def gc(a):
    if a>180:
        return 0
    else:
        return 1

def disp(im):
    sizex, sizey = im.size
    tz = []
    for y in range(sizey):
        t = []
        for x in range(sizex):
            t.append(gc(im.getpixel((x,y))))
        tz.append(t)
    for i in tz:
        print('')
        for l in i:
            print(l, sep='', end='')
    return tz

im = Image.open(image_name)
im = im.convert('L')

im_new = []
for i in range(5):
    im1 = im.crop((sx+(i*st),sy,sx+ex+(i+st),sy+ey))
    im_new.append(im1)

for i in im_new:
    disp(i)
    print('')

#input('')