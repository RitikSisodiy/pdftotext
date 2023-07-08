import PyPDF2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
import pdfminer.high_level 
import pdfminer
import pytesseract ,io
from pdf2image import convert_from_path
from PIL import Image
from pdfminer.layout import LTTextContainer,LTTextBoxHorizontal
# Open the PDF file
def get_image(layout_object):
    if (isinstance(layout_object, LTTextContainer) or isinstance(layout_object, LTTextBoxHorizontal)):
        # pdb.set_trace()
        return layout_object.get_text()
    if isinstance(layout_object, pdfminer.layout.LTContainer):
        result = ""
        for child in layout_object:
            result += get_image(child)
        return result
    else:
        return ""
def pdf_page_to_text(pdf_reader,page_num,filepath):
    page = pdf_reader.pages[page_num]
    if '/XObject' in page['/Resources']:
        page = convert_from_path(filepath,first_page= page_num+1,last_page=page_num+1)[0]
        extracted_image_text = pytesseract.image_to_string(page)
        # return xObject[obj].extract_text()
        extracted_text =  extracted_image_text
        # print("pass")
    else:        
        extracted_text = page.extract_text()
        if not extracted_text:
            pages = list(pdfminer.high_level.extract_pages(filepath))
            page = pages[page_num]
            extracted_text = get_image(page)

    # Append the extracted text to the result string
    open(f"{filepath}{page_num}.txt","w").write(extracted_text)
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