from drawbot_skia.drawbot import oval, saveImage
y = 10
x = 10
step = 160
for i in range(5):
    for t in range(6):
        oval (x, y, 120, 120 )
        x = x + step
    y = y + step
    x = 10
saveImage("HW2.pdf")