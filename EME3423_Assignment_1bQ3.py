import cv2
import numpy as np


capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img = capture.read()
    if not success:
        print("Failed to capture image")
        break

    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


    img_flip_horizontal = cv2.flip(img, 1)
    img_flip_vertical = cv2.flip(img, 0)
    img_flip_both = cv2.flip(img, -1)


    top_row = np.hstack((img, img_flip_horizontal))
    bottom_row = np.hstack((img_flip_vertical, img_flip_both))


    combined_output = np.vstack((top_row, bottom_row))

    cv2.imshow("Mirrored Frames", combined_output)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()