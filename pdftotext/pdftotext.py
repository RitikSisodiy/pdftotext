import PyPDF2,io,pdb
import pytesseract,random
from PIL import Image
io.BytesIO
# Open the PDF file

def pdf_page_to_text(file,page_num):
    pdf_reader = PyPDF2.PdfReader(file)
    page = pdf_reader.pages[page_num]
    if '/XObject' in page['/Resources']:
        # If the page contains images
        xObject = page['/Resources']['/XObject'].get_object()

        for obj in xObject:
            # print(xObject[obj]['/Subtype'])
            if xObject[obj]['/Subtype'] == '/Image':
                # Use Tesseract OCR to extract text from the image
                # print(xObject[obj])
                # pdb.set_trace()
                try:
                    # print("extraciting....",end="\r")
                    extracted_image_text = pytesseract.image_to_string(Image.open(io.BytesIO(xObject[obj]._data)))
                    # print("extracted....",end="\r")
                    # Append the extracted image text to the result string
                    return extracted_image_text
                except:
                    open(f"{random.randint(1000,100000)}.jpg","wb").write(xObject[obj]._data)
                    # pdb.set_trace()
                    # return xObject[obj].extract_text()
                    return ""
                    # print("pass")
    else:
        print("inside else")
        # If the page contains text elements
        extracted_text = page.extract_text()

    # Append the extracted text to the result string
    return extracted_text
def pdf_to_text(pdf_file):
    if isinstance(pdf_file,str):
        pdf_file = open(pdf_file, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Initialize an empty string to store the extracted text

    # Iterate over each page in the PDF
    for page_num in range(len(pdf_reader.pages)):
        # Extract the page as an image
        text = pdf_page_to_text(pdf_reader,page_num)      
        yield text
        

    # Close the PDF file
    pdf_file.close()

    # Print the extracted text
if __name__ == "__main__":
    for text in pdf_to_text("test.pdf"):
        with open("out.txt","a",encoding="utf8") as file:
            file.write(text)