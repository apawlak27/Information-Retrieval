import ctypes
from tkinter import *
from sklearn.externals import joblib
from sklearn.feature_extraction.text import CountVectorizer

#ctypes.windll.user32.SetProcessDPIAware()

ensemble = joblib.load('ensemble.model')
count_vect = joblib.load('CountVect.cv')

root = Tk()
labelStr = StringVar()
label = Label(root, font='Arial 16 bold', textvariable=labelStr, relief=RAISED).grid(row=1)
text = Text(root, height=10, font='Arial 16 bold')
text.grid(row=0)

def inputListener(arg):
    inputTokenized = count_vect.transform([text.get(1.0, END)])
    if ensemble.predict(inputTokenized)[0] == 0:
        labelStr.set('NO')
    else:
        labelStr.set('YES')

text.bind('<KeyRelease>', inputListener)

root.title('Bully Detector')
root.resizable(False, False)

root.mainloop()




