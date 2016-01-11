from PIL import Image, ImageTk
from Tkinter import Tk, Label, BOTH, Text
from ttk import Frame, Style
from time import sleep
import pozycjoner


class Skacz(Frame):

    def __init__(self, parent):
        self.y = 240
        self.pozycjoner = pozycjoner.Pozycjoner(self.y)
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.parent.bind('<Key>', self.steruj)

    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)
        bard = Image.open("kitty.png")
        bardejov = ImageTk.PhotoImage(bard)
        self.label1 = Label(self, image=bardejov)
        self.label1.image = bardejov
        self.label1.place(x=20, y=self.y)

    def steruj(self, event):
        change = False
        if event.char == 'w' and self.y > 0:
            change = True
            self.y -= 10
        elif event.char == 's' and self.y < 240:
            change = True
            self.y += 10

        if change:
            self.label1.place(x=20, y=self.y)

    def tick(self):
        # pos =
        self.pozycjoner(pos)
        self.after(200, self.tick)


def main():
    root = Tk()
    root.geometry("1024x800")
    app = Skacz(root)
    app.after(200, app.tick)
    root.mainloop()


if __name__ == '__main__':
        main()
