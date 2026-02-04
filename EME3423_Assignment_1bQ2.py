import cv2
import numpy as np

capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

while True:
    success, img = capture.read()
    if not success:
        print("Failed to capture image")
        break

    img = cv2.resize(img, (int(img.shape[1] / 2), int(img.shape[0] / 2)))


    img_blur = cv2.GaussianBlur(img, (15, 15), 0)


    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


    img_edges = cv2.Canny(img, 100, 200)


    img_edges_color = cv2.cvtColor(img_edges, cv2.COLOR_GRAY2BGR)


    stack_horizontal_1 = np.hstack((img, img_blur))
    stack_horizontal_2 = np.hstack((img_hsv, img_edges_color))
    final_output = np.vstack((stack_horizontal_1, stack_horizontal_2))

    cv2.imshow("Combined Output", final_output)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


capture.release()
cv2.destroyAllWindows()