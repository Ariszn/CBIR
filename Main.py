from tkinter import *
from tkinter.filedialog import askopenfilename
from PIL import Image, ImageTk
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import test


class CBIR():
    def __init__(self):
        self.window = Tk()
        self.window.title("图像检索系统")
        self.window.geometry('400x200')

        self.canvas = Canvas(self.window)
        Label(self.window, text="输入图片路径：").pack()
        self.filename = StringVar()
        Entry(self.window, textvariable=self.filename).pack()
        Button(self.window, text='选择图片', command=self.getfilename).pack()

        Label(self.window, text="输入检索的数据集").pack()
        self.databasepath = StringVar()
        Entry(self.window, textvariable=self.databasepath).pack()

        Button(self.window, text='搜索', command=self.Search).pack()
        self.window.mainloop()

    def getfilename(self):
        self.filename.set(askopenfilename())
    def Search(self):
        gotfilename = self.filename.get()
        im = mpimg.imread(gotfilename)
        plt.title("query")
        plt.imshow(im)
        plt.show()
        database=self.databasepath.get()
        print(gotfilename)
        print(database)
        test.search(gotfilename,database)
CBIR()
