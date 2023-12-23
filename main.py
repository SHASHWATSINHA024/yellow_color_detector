import cv2
from scratch_5 import gets_limits
from PIL import Image
# Open the camera with index 2 (you can try other indices like 0 or 1)
cap = cv2.VideoCapture(0)
yellow =[0,255,255]

#yellow in RGBCOLOR
# Check if the camera is opened successfully 
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Check if the frame is read successfully
    if not ret:
        print("Error: Failed to capture frame.")
        break
    hsvImage=cv2.cvtColor(frame,cv2.COLOR_HSV2BGR)
    lowerLimit,upperLimit =gets_limits(color=yellow)
    mask=cv2.inRange(hsvImage,lowerLimit,upperLimit)
    mask_=Image.fromarray(mask)
    bbox=mask_.getbbox()
    if bbox is not None:
     print(bbox)
     x1,y1,x2,y2=bbox
     frame=cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),7)
    # Display the frame in a window named 'frame'
    cv2.imshow('frame', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Check")
        break

# Release the video capture object and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
