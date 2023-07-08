import fitz,os
import pytesseract

class PDFConverter:
    def __init__(self, pdf_file):
        self.pdf_file = pdf_file
        self.doc = fitz.open(pdf_file)

    def calculate_image_coverage(self, page):
        images = page.get_images(full=True)
        page_width = page.rect.width
        page_height = page.rect.height
        total_page_area = page_width * page_height
        image_area = 0
        if images:
            for image in images:
                print(image,page_width,page_height)
                x, y, width, height, _, _, _, _, _, _ = image
            image_area += width * height
            image_coverage = (image_area / total_page_area) * 100
            return image_coverage
        else:
            return 0

    def extract_text_from_page(self, page):
        page = self.doc[page]
        image_coverage = self.calculate_image_coverage(page)
        print(image_coverage)
        if image_coverage > 10:
            pix = page.get_pixmap()
            temp_image = f"tmp/temp_page_{page.number}.png"
            pix.save(temp_image)
            page_text = pytesseract.image_to_string(temp_image)
            os.remove(temp_image)
        else:
            page_text = page.get_text()

        return page_text

    def convert_to_text(self):
        extracted_text = ""

        for page in self.doc:
            page_text = self.extract_text_from_page(page)
            extracted_text += "_______________page break______________\n\n\n" + page_text

        self.doc.close()
        return extracted_text


if __name__ == "__main__":
    pdf_file = "proof.pdf"
    converter = PDFConverter(pdf_file)
    extracted_text = converter.convert_to_text()

    with open("out.txt", "w", encoding="utf8") as file:
        file.write(extracted_text)
