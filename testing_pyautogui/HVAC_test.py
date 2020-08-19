import pyautogui
import cv2
import numpy as np

print("HI, Starting Automation")
pyautogui.PAUSE = 2.5
pyautogui.FAILSAFE = True

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
im1PIL = pyautogui.screenshot()
im1 = np.array(im1PIL) 
im1 = im1[:, :, ::-1].copy() 
cv2.imshow("ScreenShot",im1)
cv2.waitKey(1)

img_gray = cv2.cvtColor(im1, cv2.COLOR_BGR2GRAY)
cv2.imshow("img_gray",img_gray)
cv2.waitKey(1)
template = cv2.imread('FC.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow("template",template)
cv2.waitKey(1)



try:

    img1 =img_gray #cv2.imread('book_cover.jpg', 0)
    img2 =template #cv2.imread('book_cover_rotated.jpg', 0)

    orb = cv2.ORB_create(nfeatures=100)
    kp1, des1 = orb.detectAndCompute(img1, None)
    kp2, des2 = orb.detectAndCompute(img2, None)

    # matcher takes normType, which is set to cv2.NORM_L2 for SIFT and SURF, cv2.NORM_HAMMING for ORB, FAST and BRIEF
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    # matches = sorted(matches, key=lambda x: x.distance)
    # draw first 50 matches
    match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None)
    cv2.imshow('Matches', match_img)
    cv2.waitKey()

except Exception as error:
    error: print(error)
    exit(-1)

w, h = template.shape[::-1]
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)
threshold = 0.8
loc = np.where( res >= threshold)
for pt in zip(*loc[::-1]):
    cv.rectangle(im1, pt, (pt[0] + w, pt[1] + h), (0,0,255), 2)
cv2.imshow('Found on Screen',im1)
cv2.waitKey(0)

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.

pyautogui.click()          # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('FC.png',) # Find where button.png appears on the screen and click it.

pyautogui.move(0, 10)      # Move mouse 10 pixels down from its current position.
pyautogui.doubleClick()    # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.

pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES

pyautogui.keyDown('shift') # Press the Shift key down and hold it.
pyautogui.press(['left', 'left', 'left', 'left']) # Press the left arrow key 4 times.
pyautogui.keyUp('shift')   # Let go of the Shift key.

pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.

pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.