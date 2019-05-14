from PiVideoStream import PiVideoStream
import cv2
import time

Camera = PiVideoStream().start()

time.sleep(0.1)

while True:
	# grab the raw NumPy array representing the image, then initialize the timestamp
  # and occupied/unoccupied text
  image = Camera.read()
  if image is None:
    continue

  # show the frame
  cv2.imshow("Frame", image)
  key = cv2.waitKey(1) & 0xFF

  # if the `q` key was pressed, break from the loop
  if key == ord("q"):
    break

  time.sleep(0.01)
