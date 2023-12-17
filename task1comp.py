import cv2
import numpy as np

def find_polygon_centroids(image_path, num_sides_list):
    image = cv2.imread(image_path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    find_edge = cv2.Canny(gray, 30, 200)

    contours, hierarchy = cv2.findContours(find_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    for contour in contours:
        epsilon = 0.02 * cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, epsilon, True)

       
        if len(approx) in num_sides_list:
            M = cv2.moments(contour)
            if M["m00"] != 0:
                cx = int(M["m10"] / M["m00"])
                cy = int(M["m01"] / M["m00"])
                cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)
                cv2.putText(image, 'centroid', (cx - 30, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
    if len(contours) > 0:
        moments = cv2.moments(contours[0])
        if moments['m00'] != 0:
            cx = int(moments['m10'] / moments['m00'])
            cy = int(moments['m01'] / moments['m00'])

        cv2.circle(image, (cx, cy), 5, (255, 0, 0), -1)
        cv2.putText(image, 'centroid', (cx - 30, cy - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
        cv2.drawContours(image, contours, -1, (0, 255, 0), 5)
    cv2.imshow('RESULT', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
find_polygon_centroids('task1_image.jpg', [3, 6])