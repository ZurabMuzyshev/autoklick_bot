import cv2
import numpy as np
import mss
import pyautogui
import matplotlib.pyplot as plt
from time import time, sleep
import mouse

# Load the reference image
reference_image = cv2.imread("Screenshot_1.png", 0)

# Create a MSS object to capture the screen
sct = mss.mss()

# Continuously capture the screen and search for the reference image
while True:
    start_time = time()
    # Capture the screen using the MSS object
    screen = np.array(sct.grab({"top": 0, "left": 0, "width": 1920, "height": 1080}))

    # Convert the screen to grayscale
    screen_gray = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

    # Use matchTemplate to search for the reference image in the screen
    result = cv2.matchTemplate(screen_gray, reference_image, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(result)

    # If the reference image is found in the screen
    if max_val > 0.9:
        # Get the top-left corner of the image
        top_left = max_loc
        # Move the mouse pointer to the center of the image
        x, y = max_loc[1] + 18, max_loc[0] + 16
        mouse.move(y, x, absolute=True)
        mouse.click(button='left')
        sleep(0.02)

        # pyautogui.moveTo(top_left[0] + reference_image.shape[1]/2, top_left[1] + reference_image.shape[0]/2)
        # click on found object
        # pyautogui.click()

        # Draw a rectangle around the found image
        # bottom_right = (top_left[0] + reference_image.shape[1], top_left[1] + reference_image.shape[0])
        # cv2.rectangle(screen, top_left, bottom_right, (0, 0, 355), 2)

        # Show the screen with the rectangle
        # cv2.imshow("Screen", screen)
    print("Конец итерации - %s секунд -" % (time() - start_time))

    # Display the screen and reference image
    # plt.subplot(121), plt.imshow(screen_gray, cmap="gray")
    # plt.title("Screen"), plt.xticks([]), plt.yticks([])
    # plt.subplot(122), plt.imshow(reference_image, cmap="gray")
    # plt.title("Reference Image"), plt.xticks([]), plt.yticks([])
    # plt.show()
<<<<<<< HEAD

# merge main
=======
    
>>>>>>> bc38d7ed168af4d9a24caa832ea53bb168eae0c0
