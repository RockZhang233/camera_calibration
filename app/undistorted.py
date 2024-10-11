import numpy as np
import cv2
import sys
import os
import matplotlib.pyplot as plt

output_dir = 'results'
os.makedirs(output_dir, exist_ok=True)

# Load calibration parameters
DIM = np.loadtxt('results/size.csv', delimiter=',').astype(int)
K = np.loadtxt('results/camera_matrix.csv', delimiter=',')
D = np.loadtxt('results/dist_coeffs.csv', delimiter=',')
print('DIM', DIM)
print('K', K)
print('D', D)

def undistort(img_path):
    img = cv2.imread(img_path)
    h, w = img.shape[:2]
    
    # Generate undistortion map
    map1, map2 = cv2.fisheye.initUndistortRectifyMap(K, D, np.eye(3), K, DIM, cv2.CV_16SC2)
    undistorted_img = cv2.remap(img, map1, map2, interpolation=cv2.INTER_LINEAR, borderMode=cv2.BORDER_CONSTANT)
    
    if True:
        # Create subplots for original and undistorted images
        plt.figure(figsize=(10, 5))

        # Display the original image
        plt.subplot(1, 2, 1)
        plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB), aspect='auto')  # Maintain aspect ratio
        plt.title('Original Image')
        plt.axis('image')  # Keep the aspect ratio intact
        plt.axis('off')  # Hide axis

        # Display the undistorted image
        plt.subplot(1, 2, 2)
        plt.imshow(cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB), aspect='auto')  # Maintain aspect ratio
        plt.title('Undistorted Image')
        plt.axis('image')  # Keep the aspect ratio intact
        plt.axis('off')  # Hide axis

        # Adjust the layout to reduce border space
        plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)

        plt.show()  # Show the plot

    # Save the undistorted image
    output_filename = os.path.join(output_dir, 'out_' + os.path.basename(img_path))  # Add prefix when saving
    plt.imsave(output_filename, cv2.cvtColor(undistorted_img, cv2.COLOR_BGR2RGB))  # Save the undistorted image

if __name__ == '__main__':
    import glob
    images = glob.glob('photos/*.png')
    for p in images:
        undistort(p)
