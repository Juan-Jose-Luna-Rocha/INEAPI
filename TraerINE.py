#Proyecto realizado por Juan José Luna Rocha
#Contacto lunarochajuanjose@gmail.com

import cv2
import pytesseract

def ExtraerImagen(image):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    escalaDeColor = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    texto = pytesseract.image_to_string(escalaDeColor)
    directorio = open('Info.txt',"w")
    directorio.write(texto)
    directorio.close()
    return texto


