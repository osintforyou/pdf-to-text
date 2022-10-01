import PyPDF2

#You have to place the pdf file in the same folder as this python file, and then add the pdf file name below.
pdf_file = open('your_file.pdf','rb') 
read_pdf = PyPDF2.PdfFileReader(pdf_file)
number_of_pages = read_pdf.getNumPages()

for page_number in range(number_of_pages):
    page = read_pdf.getPage(page_number)
    pdfData = page.extractText()
    f = open('out.txt', 'a') #The result will be in the out.txt in the same folder where is this python file.
    f.write(pdfData)
    f.close()

print('Job done')
