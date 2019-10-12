"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import pyautogui
import time
from gaze_tracking import GazeTracking

gaze = GazeTracking()
webcam = cv2.VideoCapture(0)
resetTimeDuration = 1.0

while True:
    # We get a new frame from the webcam
    _, frame = webcam.read()

    # We send this frame to GazeTracking to analyze it
    gaze.refresh(frame)

    frame = gaze.annotated_frame()
    text = ""

    if gaze.is_blinking():
        text = "Blinking"
        pyautogui.doubleClick()
    elif gaze.is_right():
        text = "Looking right"
        pyautogui.moveTo(1800, 600, duration = resetTimeDuration) 
    elif gaze.is_left():
        text = "Looking left"
        pyautogui.moveTo(200, 600, duration = resetTimeDuration) 
        # timeout = time.time() + resetTimeDuration  # t seconds from now
        # while True:
        #     test = 0
        #     if test == 5 or time.time() > timeout:
        #         break
        #     test = test - 1
    elif gaze.is_center():
        text = "Looking center"

    cv2.putText(frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2)

    left_pupil = gaze.pupil_left_coords()
    right_pupil = gaze.pupil_right_coords()
    cv2.putText(frame, "Left pupil:  " + str(left_pupil), (90, 130), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)
    cv2.putText(frame, "Right pupil: " + str(right_pupil), (90, 165), cv2.FONT_HERSHEY_DUPLEX, 0.9, (147, 58, 31), 1)

    cv2.imshow("Demo", frame)

    if cv2.waitKey(1) == 27:
        break
