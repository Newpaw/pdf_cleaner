import os
from pdf2image import convert_from_path
from PIL import Image
from reportlab.pdfgen import canvas
import logging

# Nastavení logování
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pdf_to_images_and_back(pdf_path, output_pdf_path):
    try:
        # Převod PDF na obrázky
        images = convert_from_path(pdf_path)
        logging.info(f"PDF {pdf_path} bylo úspěšně převedeno na obrázky.")
        
        # Příprava na spojení obrázků do PDF
        c = canvas.Canvas(output_pdf_path)
        for image in images:
            image_path = "temp_image.png"
            image.save(image_path, 'PNG')
            img = Image.open(image_path)
            c.setPageSize((img.width, img.height))
            c.drawImage(image_path, 0, 0, img.width, img.height)
            c.showPage()
            os.remove(image_path)  # Odstranění dočasného obrázku
        c.save()
        logging.info(f"Všechny obrázky byly úspěšně spojeny do {output_pdf_path}.")
    except Exception as e:
        logging.error(f"Chyba při zpracování {pdf_path}: {e}")

def process_all_pdfs(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(directory, filename)
            output_pdf_path = f"{os.path.splitext(pdf_path)[0]}_done.pdf"
            pdf_to_images_and_back(pdf_path, output_pdf_path)
            logging.info(f"Zpracováno: {filename}")

if __name__ == "__main__":
    # Zpracování všech PDF souborů ve složce
    #current_directory = os.getcwd()
    #process_all_pdfs(current_directory)
    pass