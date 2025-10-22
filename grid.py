import numpy as np
import cv2

pathfile = r"C:\\Users\\amate\\Downloads\\image1.png"

#---------------------------------
# Load image
#---------------------------------
img_original = cv2.imread(pathfile)
cv2.imshow('original', img_original)

#---------------------------------
# Draw Markers + Get width and Height  + Break into 10 rows and columns
#---------------------------------

width = 720
height = 576

# Draw columns at 50 intervals, width step at 50, height from 0 to 576
col_interval = 50
for i in range(0, width, col_interval):
    cv2.line(img_original, (i, 0), (i, height), (255, 255, 0), 2)
    cv2.putText(img_original, '%s' % (i), (i, col_interval // 2), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0),
                thickness=1)

# Draw rows at 50 interval
row_interval = 50
for i in range(0, height, row_interval):
    cv2.line(img_original, (0, i), (width, i), (255, 255, 0), 2)
    cv2.putText(img_original, '%s' % (i), (row_interval // 2, i), cv2.FONT_HERSHEY_SIMPLEX, 0.3, (0, 0, 0),
                thickness=1)

#---------------------------------
# Manually read the grid and park down the x, y of the area of interest + Draw the polygon to confirm the mask location
#---------------------------------

# First mask - which is whole image black
mask = np.zeros(img_original.shape[:2], dtype="uint8")
cv2.imshow('mask', mask)

pts = np.array([[280, 80], [0, 300], [0, 500], [700, 500], [700, 80]], np.int32)

cv2.polylines(img_original, [pts], True, (255, 0, 0), thickness=2)
cv2.imshow('AreaOfInterest', img_original)

print("Area of Interest :\n", pts)

# Mask + white (255) + infill at '1'
cv2.fillPoly(mask, [pts], 255, 1)
cv2.imshow('Masked', mask)

# Bitwise + mask
masked = cv2.bitwise_and(img_original, img_original, mask=mask)
cv2.imshow('MaskedImg', masked)

cv2.waitKey(0)
cv2.destroyAllWindows()
