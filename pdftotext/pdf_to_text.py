import PyPDF2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path
def pdf_page_has_images(page):
    if '/XObject' in page['/Resources']:
        xObject = page['/Resources']['/XObject'].get_object()

        for obj in xObject:
            if xObject[obj]['/Subtype'] == '/Image':
                return True
    return False

def pdf_page_to_text(page):
    # Extract text from the page
    extracted_text = page.extract_text()
    return extracted_text

def pdf_page_to_image(page):
    # Convert the page to an image
    image = page.to_image(resolution=150)  # Adjust the resolution as needed
    return image

def image_to_text(image):
    # Use Tesseract OCR to extract text from the image
    extracted_text = pytesseract.image_to_string(image, lang='eng')
    return extracted_text
def pdf_page_to_images(page):
    # Extract images from the page and convert to PIL Image objects
    images = page.extract_images()
    pil_images = []
    for img in images:
        image = Image.frombytes(
            mode=img[0]['/ColorSpace'] if '/ColorSpace' in img[0] else 'RGB',
            size=(img[0]['/Width'], img[0]['/Height']),
            data=img[1]
        )
        pil_images.append(image)
    return pil_images
def pdf_to_text(pdf_file,page_num):
    if isinstance(pdf_file, str):
        pdf_file = open(pdf_file, 'rb')

    # Create a PDF reader object
    pdf_reader = PyPDF2.PdfReader(pdf_file)

    # Iterate over each page in the PDF
        # Get the current page
    page = pdf_reader.pages[page_num]

    # Check if the page contains images
    if pdf_page_has_images(page):
        # Convert the page to an image
        images = convert_from_path(pdf_file.name, first_page=page_num + 1, last_page=page_num + 1)

        # Extract text from the image
        text = ""
        for image in images:
            new_text = image_to_text(image)
            text+= new_text
    else:
        # Extract text from the page
        text = pdf_page_to_text(page)

    # Close the PDF file
    pdf_file.close()
    return text
if __name__ == "__main__":
    for text in pdf_to_text("test.pdf"):
        with open("out.txt", "a", encoding="utf8") as file:
            file.write(text)
