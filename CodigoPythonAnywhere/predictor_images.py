import pickle
from PIL import Image #Para leer de url
import requests #Para leer de url
from io import BytesIO #Para leer de url
import numpy as np

class imagePredictor():
  def __init__(self):
    pass

  def colorPredictor(url):
    with open('/home/Luminam/mysite/Color_model.pkl', 'rb') as handle:
      model = pickle.load(handle)

    response = requests.get(url)
    img = Image.open(BytesIO(response.content))
    img = img.resize((150,150))
    array_imagen = np.asarray(img)
    if array_imagen.shape != (150,150,3): ##Por si viene una imagen rgba
        img.load()
        background = Image.new('RGB', img.size, (255, 255, 255))
        background.paste(img, mask=img.split()[3])
        img = background
        array_imagen = np.asarray(img)
    array_imagen = array_imagen * 1.0/255.0
    array_imagen = np.expand_dims(array_imagen, axis=0)
    array_imagen = array_imagen.reshape(len(array_imagen),-1)
    array_imagen = array_imagen.astype(np.float32, order='K', casting='unsafe', subok=True, copy=True)

    categoria = (model.predict(array_imagen)[0])
    categoria = int(categoria)
    if categoria == 0:
        return "verde"
    elif categoria == 1:
        return "rojo"
    elif categoria == 2:
        return "violeta"
    elif categoria == 3:
        return "violeta"
    elif categoria == 4:
        return "amarillo"
    elif categoria == 5:
        return "azul"
    elif categoria == 6:
        return "violeta"
    elif categoria == 7:
        return "amarillo"
    elif categoria == 8:
        return "verde"
    elif categoria == 9:
        return "azul"
    return "error"
