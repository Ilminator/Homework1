from drawbot_skia.drawbot import oval, saveImage
y = 1
step = 160
for i in range(5):
    oval (90, y, 120, 120 )
    y = y + step
saveImage("HW1.pdf")
