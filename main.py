# PIL is pillow
from PIL import Image
import os

directoryPath = 'data'
directoryFiles = os.listdir(directoryPath)
print(directoryFiles)

for file in directoryFiles:
    rawData = open("data/" + file)
    buffer = [0 for i in range(102400)]
    for values in range(0,102400):
        line = rawData.readline()
        floatData = int(line)
        buffer[values] = floatData
    byteData = bytes(buffer)
    imgSize = (320,320)
    img = Image.frombytes('L', imgSize, byteData)
    img.save('output/' + file.replace('txt','jpg'))

# from PIL import Image
# rawData = open("data/image-converted_000000000.txt")
# buffer = [0 for i in range(102400)]
# for values in range(0,102400):
#     line = rawData.readline()
#     floatData = int(line)
#     buffer[values] = floatData
# byteData = bytes(buffer)
# imgSize = (320,320)
# img = Image.frombytes('L', imgSize, byteData)
# img.save('DUT.jpg')