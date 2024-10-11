import cv2 as cv
import os
import time

# Ensure the output directory exists
output_dir = 'photos'
os.makedirs(output_dir, exist_ok=True)

# Open the camera
cap = cv.VideoCapture(2)  # Use index 2 to open the camera

if not cap.isOpened():
    print("Unable to open the camera")
    exit()

while True:
    # Capture a frame from the camera
    ret, frame = cap.read()
    
    if not ret:
        print("Unable to read video frame")
        break

    # Display the original camera feed without distortion correction
    cv.imshow('Camera Feed', frame)

    # Wait for a key press
    key = cv.waitKey(1) & 0xFF
    
    # Capture photo when spacebar is pressed
    if key == ord(' '):
        # Generate a unique filename with timestamp
        timestamp = time.strftime("%Y%m%d_%H%M%S")  # Format: YearMonthDay_HourMinuteSecond
        filename = os.path.join(output_dir, f'captured_image_{timestamp}.png')
        cv.imwrite(filename, frame)  # Save the original frame
        print(f"Image saved as {filename}")
        
    # Exit when 'q' is pressed
    if key == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv.destroyAllWindows()
