import cv2
from yolo_detector import detect_objects
from camera_utils import open_cameras

# Nilai awal threshold (dalam % karena trackbar butuh int)
initial_threshold = 50  # 50% = 0.5

def nothing(x):
    pass  # Fungsi dummy untuk trackbar

def proses_deteksi(kamera, nama_window, conf_threshold):
    ret, frame = kamera.read()
    if not ret:
        print(f"Gagal membaca frame dari {nama_window}")
        return False

    hasil_frame, _ = detect_objects(frame, conf=conf_threshold)

    # Tampilkan nilai threshold
    cv2.putText(
        hasil_frame,
        f"Threshold: {conf_threshold:.2f}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    cv2.imshow(nama_window, hasil_frame)
    return True

def main():
    cam_bawah, cam_depan = open_cameras()

    if not (cam_bawah.isOpened() and cam_depan.isOpened()):
        print("Gagal membuka salah satu kamera.")
        return

    # Buat jendela dan slider trackbar
    cv2.namedWindow("Kontrol Threshold")
    cv2.createTrackbar("Confidence %", "Kontrol Threshold", initial_threshold, 100, nothing)

    while True:
        # Ambil nilai threshold dari slider (0 - 100), lalu ubah ke float (0.0 - 1.0)
        conf = cv2.getTrackbarPos("Confidence %", "Kontrol Threshold") / 100.0

        if not proses_deteksi(cam_bawah, "Deteksi Bantalan (YOLO)", conf):
            break
        if not proses_deteksi(cam_depan, "Deteksi Jalur Rel (YOLO)", conf):
            break

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam_bawah.release()
    cam_depan.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
