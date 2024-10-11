import numpy as np
import cv2
import os

output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Load calibration parameters
DIM = np.loadtxt('results/size.csv', delimiter=',').astype(int)
K = np.loadtxt('results/camera_matrix.csv', delimiter=',')
D = np.loadtxt('results/dist_coeffs.csv', delimiter=',')
print('DIM', DIM)
print('K', K)
print('D', D)

def undistort(frame):
    h, w = frame.shape[:2]
    
    # Generate undistortion map
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_frame = cv2.remap(frame, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)

    return undistorted_frame

if __name__ == '__main__':
    # Initialize video capture
    cap = cv2.VideoCapture(2)  # 0 for default camera, or change to video file path if needed

    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        # Undistort the current frame
        undistorted_frame = undistort(frame)

        # Display the original frame
        cv2.imshow('Original Video', frame)

        # Display the undistorted frame
        cv2.imshow('Undistorted Video', undistorted_frame)

        # Press 'q' to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
