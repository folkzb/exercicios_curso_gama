from flask import Flask, render_template, url_for, redirect
import pandas as pd

df = pd.read_csv('dados.csv')

app = Flask(__name__)

@app.route("/")
def index():
	return 'pagina inicial'

@app.route("/renderizado/<nome>")
def template(nome):
    return render_template ("template.html", usuario=nome)



@app.route("/estatico")
def estatic():
    return redirect(url_for('static', filename='estatico.html'))


"""Faça uma rota que indique se o usuário ganhou ou perdeu um determinado premio, 
utiliza jinja para mostrar uma mensagem diferente para cada uma dessas opções"""

@app.route('/pergan/<int:numero>')
def perganhou(numero):
    global pergan
    if numero == 7:
        pergan= 'Ganhou'
    else:
        pergan= 'Perdeu'
    
    return render_template('pergan.html',pergan=pergan)
    
#Crie um csv com alguns produtos, leia o arquivo no backend(sugestão:pandas), 
# e mostre essa lista utilizando um template html
@app.route('/nome')
def nome():
    global df
    df = pd.read_csv('dados.csv')
    return render_template('nome.html', alunos=df.to_dict('records'))

#Crie uma csv contendo apenas o nome das colunas (csv vazio, sem dados, apenas estrutura), e coloque uma clausula 
# for...else...endfor para que o jinja retorne uma mensagem para o usuario quando o csv estiver vazio, 
# caso contrário mostre os itens do csv

@app.route('/clausula')
def clausula():
    return render_template('nome.html', alunos=df.to_dict('records'))

#rota com tabela html
@app.route('/tabela')
def tabela():
    df = pd.read_csv('dados.csv')
    tabela = df.to_html()
    return render_template('tabela.html', tabela=tabela)

if __name__ == "__main__":
	app.run(debug=True)