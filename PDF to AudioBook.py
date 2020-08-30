import pyttsx3 as pt
import PyPDF2 as pdf
from tkinter.filedialog import *

book = askopenfilename()

pdfreader = pdf.PdfFileReader(book)

pages = pdfreader.numPages

for number in range(1,pages):
    page = pdfreader.getPage(number)
    text = page.extractText()
    player = pt.init()
    player.say(text)
    player.runAndWait()


