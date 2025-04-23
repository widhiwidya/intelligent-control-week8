import cv2

def open_cameras():
    cam_bawah = cv2.VideoCapture(2)   # Menghadap ke bawah (bantalan)
    cam_depan = cv2.VideoCapture(0)   # Menghadap ke depan (jalur rel)

    for cam in [cam_bawah, cam_depan]:
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

    return cam_bawah, cam_depan
