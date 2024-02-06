from tkinter import Tk, Label , PhotoImage
from pygame import init , mixer
from time import sleep
from threading import Thread
from pyautogui import press


# Create the Tkinter window
window = Tk()

# Set the window to fullscreen
window.attributes('-fullscreen', True)

# Load the background image
background_image = PhotoImage(file='Capture.PNG')

# Resize the image to fit the fullscreen size
background_image = background_image.zoom(window.winfo_screenwidth() // background_image.width())
background_image = background_image.subsample(window.winfo_screenheight() // background_image.height())

# Create a label with the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
background_label.configure(background='black')


with open("settings.txt",'r') as f:
    TimeToStart = int(f.readline().split('=')[1])
    VolumeToIncrease = int(f.readline().split('=')[1])
    
# timer
sleep(TimeToStart)
init()
f = mixer.Sound("fallen.mp3")
f.play()
sleep(12)


# volume increase
try:
    for i in range(VolumeToIncrease):
        Thread(target=lambda:press('volumeup',interval=0)).start()
except:
    pass
    
f.stop()
js = mixer.Sound("jump-scare.wav")
js.play()


# Run the Tkinter event loop
window.attributes('-topmost', True)
window.mainloop()
