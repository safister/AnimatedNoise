import cv2
import os

image_folder = 'Render'
video_name = 'PerlinNoise.mp4'

imagesDict = {}
for fileName in os.listdir(image_folder):
    name = int(fileName[:-4])
    imagesDict[name] = fileName
images = []
for i in range(len(imagesDict)):
    images.append(imagesDict[i])

frame = cv2.imread(os.path.join(image_folder, images[0]))
height, width, layers = frame.shape

video = cv2.VideoWriter(video_name, 0, 30, (width,height))

for image in images:
    video.write(cv2.imread(os.path.join(image_folder, image)))

cv2.destroyAllWindows()
video.release()
