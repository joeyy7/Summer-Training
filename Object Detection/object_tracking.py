import cv2 as cv

# Reading Images
# img = cv.imread("photos/cat.jpg")

# cv.imshow("Cat", img)

# reading videos
capture = cv.VideoCapture('video.mp4')
cv.waitKey(0)
