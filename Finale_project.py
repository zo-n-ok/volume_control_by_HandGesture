import time
import ctypes
import cv2
import mediapipe as mp
import numpy as np

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize volume adjustment
last_change = time.time()
volume_percentage = 50  # Start at 50% volume (arbitrary reference)

# Function to change system volume
def change_volume(direction):
    global volume_percentage
    VK_VOLUME_UP = 0xAF
    VK_VOLUME_DOWN = 0xAE
    
    if direction == 'up':
        ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 0, 0)
        ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 2, 0)
        volume_percentage += 10
    elif direction == 'down':
        ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
        ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, 2, 0)
        volume_percentage -= 10
    
    volume_percentage = np.clip(volume_percentage, 0, 100)

# Video capture
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

if not cap.isOpened():
    print("Error: Camera not accessible.")
    exit()

try:
    while True:
        success, img = cap.read()
        if not success:
            print("Failed to capture frame.")
            break

        # Convert the image to RGB for MediaPipe
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = hands.process(imgRGB)

        # Draw hand landmarks
        if results.multi_hand_landmarks:
            for handLms in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)  # Draw landmarks
                
                lmList = []
                h, w, c = img.shape
                for id, lm in enumerate(handLms.landmark):
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])

                # Calculate distance between index fingertip (id=8) and thumb tip (id=4)
                tipId, thumbTipId = 8, 4
                tipX, tipY = lmList[tipId][1], lmList[tipId][2]
                thumbTipX, thumbTipY = lmList[thumbTipId][1], lmList[thumbTipId][2]
                distance = ((tipX - thumbTipX)**2 + (tipY - thumbTipY)**2)**0.5
                
                # Draw blue line between index and thumb
                cv2.line(img, (tipX, tipY), (thumbTipX, thumbTipY), (255, 0, 0), 3)
                
                # Calculate and draw midpoint
                midX, midY = (tipX + thumbTipX) // 2, (tipY + thumbTipY) // 2
                cv2.circle(img, (midX, midY), 5, (255, 0, 0), -1)
                
                # Adjust volume based on distance with cooldown
                if distance < 40 and time.time() - last_change > 0.3:
                    print("Volume Down Triggered")
                    change_volume('down')
                    last_change = time.time()
                elif distance > 80 and time.time() - last_change > 0.3:
                    print("Volume Up Triggered")
                    change_volume('up')
                    last_change = time.time()
        
        # Display volume percentage in the top left corner with black text
        cv2.putText(img, f'Volume: {volume_percentage}%', (20, 30), 
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)
        
        # Display the video feed with hand landmarks
        cv2.imshow("Hand Tracker", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    cap.release()
    cv2.destroyAllWindows()
