#Custom convolution filtering
import cv2
import numpy as np

 # 
image = cv2.imread('kucing.jpg',0)
image = cv2.resize(image,(300,200))
 #Custom convolution kernel


 # Sobel edge operator
kernel_Sobel_x = np.array([
    [-1, 0, 1],
    [-2, 0, 2],
    [-1, 0, 1]])
kernel_Sobel_y = np.array([
    [1, 2, 1],
    [0, 0, 0],
    [-1, -2, -1]])
 # Prewitt edge operator
kernel_Prewitt_x = np.array([
    [-1, 0, 1],
    [-1, 0, 1],
    [-1, 0, 1]])
kernel_Prewitt_y = np.array([
    [1, 1, 1],
    [0, 0, 0],
    [-1, -1, -1]])

kernel_Laplacian_1 = np.array([
    [0, 1, 0],
    [1, -4, 1],
    [0, 1, 0]])
kernel_Laplacian_2 = np.array([
    [1, 1, 1],
    [1, -8, 1],
    [1, 1, 1]])
 # Two convolution kernels do not have rotation invariance
kernel_Laplacian_3 = np.array([
    [2, -1, 2],
    [-1, -4, -1],
    [2, 1, 2]])
kernel_Laplacian_4 = np.array([
    [-1, 2, -1],
    [2, -4, 2],
    [-1, 2, -1]])
 # 5*5 LoG Convolution Template
kernel_LoG = np.array([
    [0, 0, -1, 0, 0],
    [0, -1, -2, -1, 0],
    [-1, -2, 16, -2, -1],
    [0, -1, -2, -1, 0],
    [0, 0, -1, 0, 0]])
 # convolution

output_2 = cv2.filter2D(image, -1, kernel_Sobel_x)
output_3 = cv2.filter2D(image, -1, kernel_Prewitt_x)
output_4 = cv2.filter2D(image, -1, kernel_Laplacian_1)
 # Show sharpening effect
image = cv2.resize(image, (300, 200))
output_2 = cv2.resize(output_2, (300, 200))
output_3 = cv2.resize(output_3, (300, 200))
output_4 = cv2.resize(output_4, (300, 200))
cv2.imshow('Original Image', image)
cv2.imshow('SOBEL', output_2)
cv2.imshow('PREWITT', output_3)
cv2.imshow('LAPLACIAN', output_4)
# 
if cv2.waitKey(0) & 0xFF == 27:
    cv2.destroyAllWindows()
