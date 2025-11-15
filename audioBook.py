import pyttsx3
import pdfplumber
from tkinter.filedialog import askopenfilename

book = askopenfilename()
if not book:
    print("No file selected.")
    exit()

speaker = pyttsx3.init()

with pdfplumber.open(book) as pdf:
    for page in pdf.pages:
        text = page.extract_text()
        if text:
            print(text)
            speaker.say(text)
            speaker.runAndWait()