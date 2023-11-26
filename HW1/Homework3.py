from drawbot_skia.drawbot import oval, rect, saveImage
y = 10
x = 10
step = 90
for i in range(10):
    for t in range(6):
        oval (x, y, 60, 60 )
        x = x + step
        rect (x, y, 60, 60 )
        x = x + step
    y = y + step
    x = 10
saveImage("HW3.pdf")