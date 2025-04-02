import os
import cv2
import numpy
import imutils
import easyocr
from dotenv import load_dotenv

load_dotenv()

cascade_ref = os.environ.get("CASCADE")
images = os.environ.get("IMAGES")

for image_dir in os.listdir(images):

  image_path = os.path.join(images, image_dir)

  image = cv2.imread(image_path)
  image = imutils.resize(image, width=500)
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)


  cascade = cv2.CascadeClassifier(cascade_ref)

  plates = cascade.detectMultiScale(gray_image, scaleFactor=1.2, minNeighbors=5)

  for x, y, w, h in plates:

    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
    gray_plate = gray_image[y:y + h, x:x + w]
    color_plate = image[y:y + h, x:x + w]

    cv2.imwrite('Numberplate.jpg', gray_plate)
    gray_plate = cv2.cvtColor(gray_plate, cv2.COLOR_RGB2GRAY)
    processed = cv2.adaptiveThreshold(gray_plate, 255, 
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      cv2.THRESH_BINARY, 11, 2)
    processed = cv2.GaussianBlur(processed, (5, 5), 1)
    processed = cv2.resize(processed, None, fx=2, fy=2)


    reader = easyocr.Reader(["en"])
    plate_str = reader.readtext(processed)

    print(plate_str[0][1])

    cv2.imshow('Number Plate', gray_plate)
    cv2.imshow('Number Plate Image', image)
    cv2.waitKey(0)

cv2.destroyAllWindows()