from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio/<porcentagem>')
def cardapio(porcentagem):
  porcentagem = int(porcentagem)
  return render_template('cardapio.html', promocao=True, porcentagem=porcentagem)
  
app.run(host='0.0.0.0', port=81)