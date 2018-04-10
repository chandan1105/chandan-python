# import libraries
import time 
import os 

while True: # do forever

    

    os.system('fswebcam -r 1280x720 -S 3 --jpeg 100 --no-banner --grayscale --save /home/cs2017a114/13.jpg') # uses Fswebcam to take picture

    time.sleep(15) # this line creates a 15 second delay before repeating the loop

