import pickle

class emailPredictor():
  def __init__(self):
    pass

  def spamPredictor(text):
    with open('/home/Luminam/mysite/emails_model.pkl', 'rb') as handle:
      model = pickle.load(handle)
    with open('/home/Luminam/mysite/count_vect.pkl', 'rb') as handle:
      CV = pickle.load(handle)

    email = [text]
    texto_count = CV.transform(email)
    resultado = model.predict(texto_count)
    resultado = resultado[0]
    if resultado == 0:
        return "ham"
    elif resultado == 1:
        return "spam"
    return "error"
