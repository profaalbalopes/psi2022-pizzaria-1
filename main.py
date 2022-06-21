from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cardapio/<porcentagem>')
def cardapio(porcentagem):
  porcentagem = int(porcentagem)
  return render_template('cardapio.html', promocao=True, porcentagem=porcentagem)


@app.route('/avaliacoes')
def avaliacoes():
  #clientes = ["Arlanda", "Pedro", "Alice", "Bia", "Yanca", "Carlos", "Jonathan"]
  clientes = [ {"nome": "Arlanda", "nota": 1},
              {"nome": "Pedro", "nota": 3},
              {"nome": "Alice", "nota": 5},
              {"nome": "Bia", "nota": 4},
             ]
  return render_template('avaliacoes.html', clientes=clientes)
  
app.run(host='0.0.0.0', port=81)