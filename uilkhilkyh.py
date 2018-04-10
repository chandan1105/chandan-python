# import libraries
import time 
import os 
t=1
while (t<=5): # do forever

    

    os.system('fswebcam -r 1280x720 -S 3 --jpeg 100 --no-banner --swapchannels BG --save /home/cs2017a114/Desktop/'+str(t)+'.jpg') # uses Fswebcam to take picture
    t+=1
    time.sleep(5) # this line creates a 15 second delay before repeating the loop

