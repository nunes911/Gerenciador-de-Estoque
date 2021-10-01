from bson.objectid import ObjectId
from flask import Flask, request, render_template, url_for, redirect, flash, jsonify
from bson.json_util import dumps
from pymongo import MongoClient
from datetime import date


app = Flask(__name__)
app.secret_key = "secret key"



# criando a base de dados
client = MongoClient("localhost", 27017)
db = client.test

# rota home com lista de produtos
@app.route('/pag_home')
@app.route('/')
def pag_home():
    estoque = db.estoque.find()

    return render_template('Home.html', rows=rows)


# rota para receber os dados do cadastro do produto
@app.route('/pag_cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        try:
            _json = request.form

            produto = _json['produto']
            fabricante = _json['fabricante']
            tipo = _json['tipo'] 
            descricao = _json['descricao']
            quantidade = '0'

            insert = db.estoque.insert_one(
                {'produto': produto, 'fabricante': fabricante, 
                'tipo': tipo, 'descricao': descricao, 'quantidade': quantidade})
            

            return redirect(url_for('pag_home'))
        
        except Exception:
            flash('Erro ao Cadastrar')

    return render_template('Cadastro.html')


@app.route('/pag_estoque', methods=['GET', 'POST'])
def selecione_produto():
    if request.method == 'GET':
        estoque = db.estoque.find()

        return render_template('Estoque.html', rows=estoque)
    
    elif request.method == 'POST':
         
         return movimento()

def movimento():

    movimentacao = request.form['movimentacao']

    if movimentacao == 'Entrada':

        try:
            json = request.form

            registro_qtd = json['registro']
            quantidade = json['quantidade']
            data_atualizacao = json['data']
            local = json['local']

            cod_registro = registro_qtd.split(':')[0]

            update = "UPDATE produto SET quantidade=%s+quantidade, data_atualizacao=%s, local=%s WHERE cod_registro = %s;"
            dados = (quantidade, data_atualizacao, local, cod_registro)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(update, dados)
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('pag_home'))
        
        except Exception as e:
            return e
        
    if movimentacao == 'Saída':

        try:
            registro_qtd = request.form['registro']
            quantidade = request.form['quantidade']
            data_atualizacao = request.form['data']
            local = request.form['local']

            [cod_registro, qtd] = registro_qtd.split(':')

            if int(quantidade) <= int(qtd):

                update = "UPDATE produto SET quantidade=quantidade-%s, data_atualizacao=%s, local=%s WHERE cod_registro = %s;"
                dados = (quantidade, data_atualizacao, local, cod_registro)

                conn = mysql.connect()
                cursor = conn.cursor()
                cursor.execute(update, dados)
                conn.commit()

                cursor.close()
                conn.close()

                return redirect(url_for('pag_home'))
            
            else:
                return 'Quantidade de Saída maior que em Estoque'
        
        except Exception as e:
            return e


@app.route('/delete/<id>', methods=['POST'])
def delete(id):
    mongo.db.estoque.delete_one({'id': ObjectId(id)})
    resp = jsonify('Produto deletado do estoque com sucesso')

    return resp



# abrindo servidor
if __name__ == '__main__':
    app.run(debug=True)