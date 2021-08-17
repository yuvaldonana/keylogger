import pynput
import threading
import time

from pynput.keyboard import Key, Listener
from datetime import datetime

keys = []
barcode = [] 
i = 0
count = 0
current_time = 0
    
def thread_function(update_time):
    print(update_time, current_time)
    time.sleep(20)
    if update_time == current_time:
        f = open("exit.barcodes", "w")
        f.write("exit all windows" + str(current_time))
        f.close()
        f = open("exit.barcodes", "r")
        print(f.read())

    

def on_press(key):
    global keys, count, barcode, current_time
    keys.append(key)

    if key == Key.enter and len(barcode) >= 12 :
        test = ''.join(barcode)
        f = open("barcode.barcodes", "w")
        f.write(str(test))
        f.close()
        current_time = datetime.now()
        x = threading.Thread(target=thread_function, args=(current_time,))
        x.start()
    else:
        barcode.append(key.char)
        count += 1
                

def on_release(key):
    if key == Key.esc:
        return False



with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
