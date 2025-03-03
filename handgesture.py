import cv2
import mediapipe as mp
import numpy as np
import keyboard  # Import keyboard library

# Initialize MediaPipe Hands module
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Define hand tracking model
hands = mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.7)

last_finger_count = None  # Store last detected fingers
current_action = ""  # Store current action to display

def count_fingers(hand_landmarks):
    """ Count fingers based on landmarks """
    tips = [4, 8, 12, 16, 20]  # Thumb & Finger tips
    count = 0
    
    # Thumb detection
    if hand_landmarks.landmark[tips[0]].x < hand_landmarks.landmark[tips[0] - 1].x:
        count += 1
    
    # Other fingers detection
    for tip in tips[1:]:
        if hand_landmarks.landmark[tip].y < hand_landmarks.landmark[tip - 2].y:
            count += 1
    
    return count

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Convert frame to RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process frame
    results = hands.process(rgb_frame)
    
    fingers = 0  # Default count if no hand detected

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
            
            # Count fingers
            fingers = count_fingers(hand_landmarks)

    # Only trigger key press when finger count changes
    if fingers != last_finger_count:
        last_finger_count = fingers  # Update last detected fingers

        if fingers == 1:
            current_action = "← LEFT"
            keyboard.press_and_release('left')
            print("Detected LEFT")
        elif fingers == 2:
            current_action = "→ RIGHT"
            keyboard.press_and_release('right')
            print("Detected RIGHT")
        elif fingers == 3:
            current_action = "↓ DOWN"
            keyboard.press_and_release('down')
            print("Detected DOWN")
        elif fingers == 5:
            current_action = "↑ JUMP"
            keyboard.press_and_release('up')
            print("Detected JUMP")
        else:
            current_action = ""

    # Display finger count and action on screen
    cv2.putText(frame, f'Fingers: {last_finger_count}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
    cv2.putText(frame, f'Action: {current_action}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)

    # Display output
    cv2.imshow("Hand Gesture Recognition", frame)
    
    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()