import tkinter as tk
import tkextrafont as tkfont
import time
from pynput import keyboard as kbd

class GUI:
    def __init__(self):
        self.timestart = 0.0
        self.timeruns = False
        
        self.win = tk.Tk()
        self.win.title("StopWatch")
        self.win.resizable(0,0)
        self.win.attributes("-topmost", 1)

        self.font = tkfont.Font(file="kode.ttf", family="Kode Mono", size=48, weight="bold")

        self.tlabel = tk.Label(self.win, text="00:00.0", font=self.font, fg="#ededed", bg="#121212")
        self.tlabel.pack(fill=tk.X)

        self.listener = kbd.Listener(on_press=self.on_press, on_release=self.on_release)
        self.listener.start()
        self.win.after(100, self.centerit)
        self.win.after(200, self.runtimer)

    def on_press(self, key):
        if key == kbd.Key.ctrl_r:
            if self.timeruns:
                self.stoptimer()
            else:
                self.starttimer()

    def on_release(self, key):
        pass
    
    def centerit(self):
        x = (self.win.winfo_screenwidth() // 2) - (self.win.winfo_width() // 2)
        y = (self.win.winfo_screenheight() // 2) - (self.win.winfo_height() // 2)
        self.win.geometry(f"+{x}+{y}")

    def starttimer(self):
        self.timestart = time.time()
        self.timeruns = True

    def stoptimer(self):
        self.timeruns = False

    def runtimer(self):
        if self.timeruns:
            timegone = int((time.time() - self.timestart) * 10.0)
            tenth = timegone % 10
            secs = (timegone // 10) % 60
            mins = (timegone // 600)
            txt = f"{mins:02}:{secs:02}.{tenth}"
            self.tlabel.config(text=txt)
        self.win.after(20, self.runtimer)

def main():
    gui = GUI()
    gui.win.mainloop()
    gui.listener.stop()

if __name__ == '__main__':
    main()

