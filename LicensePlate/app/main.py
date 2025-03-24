import os
import cv2
import numpy
from dotenv import load_dotenv
import easyocr
import matplotlib.pyplot as plt
load_dotenv()

image_ref = os.environ.get("IMAGE")
cascade_ref = os.environ.get("CASCADE")

images = os.environ.get("IMAGES")

for image_dir in os.listdir(images):

  image_path = os.path.join(images, image_dir)

  image = cv2.imread(image_path)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

  cascade = cv2.CascadeClassifier(cascade_ref)

  plates = cascade.detectMultiScale(gray_image, 1.2, 6)

  for x, y, w, h in plates:

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    gray_plate = gray_image[y:y + h, x:x + w]
    color_plate = image[y:y + h, x:x + w]

    cv2.imwrite('Numberplate.jpg', gray_plate)
    cv2.imshow('Number Plate', gray_plate)
    cv2.imshow('Number Plate Image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()