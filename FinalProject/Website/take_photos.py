from picamera2 import Picamera2
import time

def take_photo():
    picam2 = Picamera2()
    still_config = picam2.create_preview_configuration()
    picam2.configure(still_config)
    picam2.start()
    time.sleep(2)
    picam2.capture_file("static/image.jpg")
    time.sleep(60)                                                  
    picam2.stop()
    return "image captured"
    
