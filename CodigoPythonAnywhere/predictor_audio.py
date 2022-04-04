import pickle
from PIL import Image #Para leer de url
import requests #Para leer de url
from io import BytesIO #Para leer de url
import numpy as np
import librosa
import math
import audioread
from urllib.request import urlretrieve

###
###CODIGO INCOMPLETO, NO SIRVE
###
class audioPredictor():
    frecuencia_muestra = 22050
    num_de_muestras_por_audio = frecuencia_muestra * 30
    def __init__(self):
        pass


    def procesar_audio(audio_path, n_mfcc = 13, n_fft = 2048, hop_length = 512, num_segmentos = 10):

        frecuencia_muestra = 22050
        num_de_muestras_por_audio = frecuencia_muestra * 30
        num_de_muestras_por_segmento = int(num_de_muestras_por_audio / num_segmentos)
        num_de_vectores_mfcc_por_segmento = math.ceil(num_de_muestras_por_segmento / hop_length)

        signal, sr = librosa.load(audio_path, sr=frecuencia_muestra, duration = 30.0)

        for segmento in range(num_segmentos):
          inicio_de_muestra = num_de_muestras_por_segmento * segmento
          fin_de_muestra = inicio_de_muestra + num_de_muestras_por_segmento
          mfcc = librosa.feature.mfcc(signal[inicio_de_muestra: fin_de_muestra],
                                      sr=sr,
                                      n_fft = n_fft,
                                      n_mfcc = n_mfcc,
                                      hop_length = hop_length)
          mfcc = mfcc.T
        return mfcc

    def predecir(X, model):
        X = X[np.newaxis, ...]
        prediccion = model.predict(X)
        prediccion = np.argmax(prediccion, axis=1)
        return prediccion




    def genrePredictor(url):

        with open('/home/Luminam/mysite/Genero_model.pkl', 'rb') as handle:
            model = pickle.load(handle)

        audio_file = 'audio.wav'
        urlretrieve("http://api.voicerss.org/?key=04f49802d32d442ca997d4d2ea76d3d5"
            "&hl=pt-pt&c=wav&src=texto", audio_file)
        with audioread.audio_open(url) as f:
            duracion = f.duration

        #Solo predice si el audio tiene una duracion mayor o igual a 30 segundos
        if(duracion >= 30):
            mfcc = procesar_audio(url)
            audio_path = url
            n_mfcc = 13
            n_fft = 2048
            hop_length = 512
            num_segmentos = 10

        frecuencia_muestra = 22050
        num_de_muestras_por_audio = frecuencia_muestra * 30
        num_de_muestras_por_segmento = int(num_de_muestras_por_audio / num_segmentos)
        num_de_vectores_mfcc_por_segmento = math.ceil(num_de_muestras_por_segmento / hop_length)

        signal, sr = librosa.load(audio_path, sr=frecuencia_muestra, duration = 30.0)

        for segmento in range(num_segmentos):
          inicio_de_muestra = num_de_muestras_por_segmento * segmento
          fin_de_muestra = inicio_de_muestra + num_de_muestras_por_segmento
          mfcc = librosa.feature.mfcc(signal[inicio_de_muestra: fin_de_muestra],
                                      sr=sr,
                                      n_fft = n_fft,
                                      n_mfcc = n_mfcc,
                                      hop_length = hop_length)
          mfcc = mfcc.T
        return mfcc















            prediccion = predecir(mfcc, model)
        categoria =prediccion[0]


        if categoria == 0:
            return "reggae"
        elif categoria == 1:
            return "hiphop"
        elif categoria == 2:
            return "rock"
        elif categoria == 3:
            return "country"
        elif categoria == 4:
            return "blues"
        elif categoria == 5:
            return "disco"
        elif categoria == 6:
            return "metal"
        elif categoria == 7:
            return "pop"
        elif categoria == 8:
            return "classical"
        elif categoria == 9:
            return "jazz"
        return "error"





