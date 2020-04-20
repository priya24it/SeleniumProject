# importing required modules
import PyPDF2

# creating a pdf file object
pdfFileObj = open('English.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)
pageObj = None
# creating a page object
for i in range(0,209):
    pageObj = pdfReader.getPage(i)
    print(pageObj.extractText())
    # extracting text from page


# closing the pdf file object
pdfFileObj.close()
