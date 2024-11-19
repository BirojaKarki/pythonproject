'''
Write a program to manipulate pdf files using pyPDF.Your programs sould be able to merge multiple pdf files into a single pdf.You are welcome to add more functionalities

'''
from pypdf import PdfWriter
import os
merger = PdfWriter()
files=[file for file in os.listdir() 
       if file.endswith(".pdf")]

for pdf in files:
    merger.append(pdf)

merger.write("merged-pdf.pdf")
merger.close()