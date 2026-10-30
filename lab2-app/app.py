from flask import Flask
app = Flask(__name__)
@app.route('/')
def hola():
return '<h1>¡Hola! Aplicación empaquetada en Docker - Laboratorio 2</h1>'
if __name__ == '__main__':
app.run(host='0.0.0.0', port=5000)