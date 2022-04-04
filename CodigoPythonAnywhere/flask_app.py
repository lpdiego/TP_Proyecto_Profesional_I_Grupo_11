from flask import Flask,jsonify,request
from flask_cors import CORS
from predictor_emails import emailPredictor
from predictor_images import imagePredictor
#from predictor_audio import audioPredictor

app = Flask(__name__)
CORS(app)
@app.route("/emails/",methods=['GET'])
def return_spam():
    text = request.args.get('email')
    mail_type = emailPredictor.spamPredictor(text)
    mail_json = {
                'mail_type':mail_type,
                }
    return jsonify(mail_json)

@app.route("/images/",methods=['GET'])
def return_color():
    url = request.args.get('url')
    color = imagePredictor.colorPredictor(url)
    color_json = {
                'color':color,
                }
    return jsonify(color_json)

#@app.route("/audio/",methods=['GET'])
#def return_genre():
#    url = request.args.get('url')
#    genre = audioPredictor.genrePredictor(url)
#    genre_json = {
#                'genre':genre,
#                }
#    return jsonify(genre_json)

@app.route("/",methods=['GET'])
def default():
  mensaje = "<p>Implementación de Modelos como Servicio</p>"
  mensaje +="<hr>"
  mensaje +="<p>Instrucciones para usar el servicio</p>"

  mensaje +="<p>Para hacer predicciones con el modelo clasificador de mail ingrese a luminam.pythonanywhere.com/emails/?email= seguido del texto del email a clasificar<br/>"
  mensaje +="Ejemplo: <br/>"
  mensaje +="<a href=\"https://luminam.pythonanywhere.com/emails/?email=text%20ur%20password%20now%20FREE%20CALLS\"> https://luminam.pythonanywhere.com/emails/?email=text%20ur%20password%20now%20FREE%20CALLS</a></p>"

  mensaje +="<p>Para hacer predicciones con el modelo clasificador de imágenes ingrese a luminam.pythonanywhere.com/images/?url= seguido de la url de la imagen a clasificar<br/>"
  mensaje +="Ejemplo: <br/>"
  mensaje +="<a href=\"https://luminam.pythonanywhere.com/images/?url=https://cdn.discordapp.com/attachments/745446281769386088/960319294707744789/Square_0c994ffe-2a96-11ea-8123-8363a7ec19e6.png\"> https://luminam.pythonanywhere.com/images/?url=https://cdn.discordapp.com/attachments/745446281769386088/960319294707744789/Square_0c994ffe-2a96-11ea-8123-8363a7ec19e6.png</a></p>"

  mensaje +="<hr>"
  mensaje +="<p>Proyecto Profesional I - UNGS<br/>"
  mensaje +="TP Inicial - Machine Learning y Python<br/>"
  mensaje +="Por Lucas Leonel Llanos y Diego Lautaro López Páez</p>"
  return mensaje

if __name__ == "__main__":
    app.run()