import cv2
import numpy as np

def detect_stereo_obstacles(imgL, imgR):
    # Konversi ke grayscale
    grayL = cv2.cvtColor(imgL, cv2.COLOR_BGR2GRAY)
    grayR = cv2.cvtColor(imgR, cv2.COLOR_BGR2GRAY)

    # Membuat stereo matcher
    stereo = cv2.StereoBM_create(numDisparities=16*3, blockSize=15)
    disparity = stereo.compute(grayL, grayR)

    # Normalisasi dan konversi ke 8-bit
    disp_norm = cv2.normalize(disparity, None, 0, 255, cv2.NORM_MINMAX)
    disp_uint8 = np.uint8(disp_norm)

    # Threshold untuk deteksi obstacle
    _, obstacle_mask = cv2.threshold(disp_uint8, 100, 255, cv2.THRESH_BINARY)
    obstacle_mask_colored = cv2.applyColorMap(obstacle_mask, cv2.COLORMAP_JET)

    return obstacle_mask_colored
