import os
import fitz
import codecs
files = [f for f in os.listdir() if os.path.isfile(f)]
pdfs = [f for f in files if '.pdf' in f.lower()]

for f in pdfs:
    print(f)
    doc = fitz.open(f)
    text = ""
    for page in doc:
        text += page.get_text()
    file1 = codecs.open(f + ".txt", "w" , "utf-8")
    file1.writelines(text)
    file1.close()
