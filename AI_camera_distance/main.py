import cv2

know_distance = 80
know_width = 14.3

fonts = cv2.FONT_HERSHEY_COMPLEX

cap = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def face_data(image):
  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  faces = face_detector.detectMultiScale(gray_image, 1.1, 5, minSize=(30, 30))
  for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 255), 2)
    return w
  return 0


def focal_length(measured_distance, real_width, width_in_rf_image):
  return (width_in_rf_image * measured_distance) / real_width


def distance_finder(focal_length, real_face_width, face_width_in_frame):
  if face_width_in_frame == 0:
    return None
  return (real_face_width * focal_length) / face_width_in_frame


focal_length_found = None

while True:
  ret, ref_frame = cap.read()
  if not ret:
    print("Error accessing the camera.")
    break

  ref_image_face_width = face_data(ref_frame)

  if ref_image_face_width != 0:
    focal_length_found = focal_length(know_distance, know_width, ref_image_face_width)
    print(f"Focal Length: {focal_length_found}")
    break

print("Starting live video...")

while True:
  ret, frame = cap.read()
  if not ret:
    print("Error accessing the camera.")
    break

  face_width_in_frame = face_data(frame)

  if face_width_in_frame != 0 and focal_length_found:
    dist = distance_finder(focal_length_found, know_width, face_width_in_frame)

    if dist:
      cv2.putText(
        frame, f"Distance = {round(dist, 2)} CM",
        (30, 450), fonts, 1,
        (255, 255, 255), 2)

  cv2.imshow("Live Video", frame)
  if cv2.waitKey(1) == 27:
    print("Exiting...")
    break

cap.release()
cv2.destroyAllWindows()