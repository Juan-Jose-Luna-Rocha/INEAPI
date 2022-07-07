#Proyecto realizado por Juan José Luna Rocha
#Contacto lunarochajuanjose@gmail.com

from flask import Flask, jsonify
import TraerINE
import cv2

app = Flask(__name__)

@app.route('/INE/<string:ruta>')
def index(ruta):
    doc = cv2.imread(ruta)
    Retorno = TraerINE.ExtraerImagen(doc)
    return Retorno

if __name__=="__main__":
    app.run()