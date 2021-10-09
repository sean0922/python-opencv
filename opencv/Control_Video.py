import cv2
import threading
import tkinter as tk
from PIL import ImageTk,Image
import time
import numpy

class cam():
    def __init__(self):
        self.frame=[]
        self.window = tk.Tk()
        self.window.title("Python")
        self.window.geometry("1000x1000")
        self.label1 = tk.Label(self.window, text="", font=("標楷體", 20), fg="#0000ff")
        self.label1.pack()
        self.btn1 = tk.Button(self.window, text="播放", font=("標楷體", 20), fg="#0000ff",command=self.strat)
        self.btn1.pack()
        self.btn2 = tk.Button(self.window, text="stop", font=("標楷體", 20), fg="#0000ff", command=self.stopp)
        self.btn2.pack()
        self.btn3 = tk.Button(self.window, text="over", font=("標楷體", 20), fg="#0000ff", command=self.over1)
        self.btn3.pack()
        self.ok=True

        self.window.mainloop()

    def camtest(self):
        self.stop=False
        #self.cam1=cv2.VideoCapture("v8.mp4")
        self.cam1=cv2.VideoCapture("ex1.mov")
        self.over=False
        #self.cam1 = cv2.VideoCapture(0)
        
        while(True):
            if cv2.waitKey(1) & 0xFF == ord('q') or self.over==True:
                break
            if self.stop==False:
                self.status, self.frame = self.cam1.read()
            if self.status==False:
                break
            if self.status:
                time.sleep(0.05)
                timee=self.cam1.get(cv2.CAP_PROP_POS_MSEC)
                print(timee)

            oimg = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGB)
            img2 = Image.fromarray(oimg)
            image2 = ImageTk.PhotoImage(image=img2)

            if self.label1 is None:
                self.label1 = tk.Label(image=image2)
                self.label1.image = image2
                self.label1.pack()
            else:
                self.label1.configure(image=image2)
                self.label1.image = image2

            #cv2.imshow("im",self.frame)



        self.cam1.release()

        cv2.destroyAllWindows()

    def strat(self):
        if(self.ok==True):
            threading.Thread(target=self.camtest,daemon=True).start()
            self.ok=False

    def getFrame(self):
        return self.frame

    def stopp(self):
        if self.stop==False:
            self.stop=True
            return

        if self.stop == True:
            self.stop = False
            return
    def over1(self):
        self.over=True
        self.ok = True



c=cam()


