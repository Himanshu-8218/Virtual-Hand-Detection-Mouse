import cv2
import mediapipe as mp
import pyautogui
cap = cv2.VideoCapture(0)
hand_detector = mp.solutions.hands.Hands(max_num_hands=1)
screen_width, screen_height = pyautogui.size()

index_y = 0
index_y_6 = 0
index_y_5 = 0
mpHands = mp.solutions.hands
drawing_utils = mp.solutions.drawing_utils

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame,1)
    frame_height, frame_width, _ = frame.shape
    rgb_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = hand_detector.process(rgb_frame)
    hands = output.multi_hand_landmarks
    if hands:
        for hand in hands:
            drawing_utils.draw_landmarks(frame, hand ,mpHands.HAND_CONNECTIONS) 
            #drawing_utils.draw_landmarks(frame,hand)
            landmarks = hand.landmark
            for id, landmark in enumerate(landmarks):
                x = int(landmark.x*frame_width)
                y = int(landmark.y*frame_height)
               
        

                if id == 8:
                    cv2.circle(img=frame, center=(x,y), radius=25, color=(0,255,255))
                    index_x = screen_width/frame_width*x
                    index_y = screen_height/frame_height*y
                    pyautogui.moveTo(index_x,index_y)

                    #Double Click
                elif id == 6:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(746,23,222))
                    index_x_6 = screen_width/frame_width*x
                    index_y_6 = screen_height/frame_height*y

                #Right Click
                elif id == 5:
                    cv2.circle(img=frame, center=(x,y), radius=15, color=(36,887,23))
                    index_x_5 = screen_width/frame_width*x
                    index_y_5 = screen_height/frame_height*y



                elif id == 4:
                    cv2.circle(img=frame, center=(x,y), radius=10, color=(255, 0, 255))
                    thumb_x = screen_width/frame_width*x
                    thumb_y = screen_height/frame_height*y
                    #print(abs(index_y_6-thumb_y))
                    if abs(index_y_6-thumb_y) <8:
                        pyautogui.doubleClick()
                        pyautogui.sleep(0.2)

                    #Right Click
                    #print(abs(index_y_5 - thumb_y))
                    if abs(index_y_5 - thumb_y) <7:
                        pyautogui.rightClick()
            






    cv2.imshow('                                 Virtual Mouse - Himanshu Verma',frame)
    cv2.waitKey(1)
