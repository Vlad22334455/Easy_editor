from fileinput import filename
from tkinter import W
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QListWidget, QLabel, QVBoxLayout, QHBoxLayout, QFileDialog
import os

from PyQt5.QtGui import QPixmap
from PIL import Image

app = QApplication([])
main_win = QWidget()
main_win.resize(700, 500)
main_win.setWindowTitle('Easy Editor')


button1 = QPushButton('Вліво')
button2 = QPushButton('Вправо')
button3 = QPushButton('Дзеркало')
button4 = QPushButton('Різкість')
button5 = QPushButton('Ч/Б')
button6 = QPushButton('Папка')

list = QListWidget()

text = QLabel('sdsd')

v1 = QVBoxLayout()
v2 = QVBoxLayout()
h1 = QHBoxLayout()
h2 = QHBoxLayout()

v1.addWidget(button6)
v1.addWidget(list)

h1.addWidget(button1)
h1.addWidget(button2)
h1.addWidget(button3)
h1.addWidget(button4)
h1.addWidget(button5)

v2.addWidget(text)
v2.addLayout(h1)

h2.addLayout(v1, 20)
h2.addLayout(v2, 80)

main_win.setLayout(h2)


main_win.show()

workdir = ''

def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()

def showFilenameslist():
    
    extensions = ['png', 'jpeg', 'jpg', 'svg']
    chooseWorkdir()

    filenames = filter(os.listdir(workdir), extensions)
    list.clear()
    for f in filenames:
        list.addItem(f)

def filter(files, extensions):
    result = []
    for a in files:
        for e in extensions:
            if a.endswith(e):
                result.append(a)
    return result

button6.clicked.connect(showFilenameslist)

class ImageProccesor():
    def __init__(self):
        self.image = None
        self.dir = None
        self.filename = None
    
    def loadimage(self, filename):
        self.filename = filename
        self.dir = dir
        file_path = os.path.join(dir, filename)
        self.image = image.open(file_path)

    def showImage(self, path):
        text_image.hide()
        pixmapimage = QPixmap(path)
        w = text_image.width()
        h = text_image.height()
        pixmapimage = pixmapimage.scaled(w, h, Qt.KeepAspectRatio)
        text_image = setPixmap(pixmapimage)

        text_image.show() 


def showChosenImage():
    if list.currentRow() >= 0:
        filename = list.currentItem().text()
        workimage.loadimage(filename)
        workimage.showImage(os.path.join(workdir, workimage.filename))
        
workimage = ImageProccesor()
list.currentRowChanged.connect(showChosenImage)




app.exec_()