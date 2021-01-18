from flask import Flask, request, render_template, url_for, redirect, flash
import json
import pymysql
from datetime import date
from flaskext.mysql import MySQL


app = Flask(__name__)
app.secret_key = "secret key"

mysql = MySQL()

# Configurando MySQL
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1994'
app.config['MYSQL_DATABASE_DB'] = 'mercadoria'

mysql.init_app(app)


# rota home com lista de produtos
@app.route('/pag_home')
@app.route('/')
def pag_home():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT * FROM produto")
        rows = cursor.fetchall()
    except:
        return 'ERRO'
    finally:
        conn.close()
        cursor.close()

    return render_template('Home.html', rows=rows)


# rota para receber os dados do cadastro do produto
@app.route('/pag_cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        try:
            nome = request.form['nome']
            cod_registro = request.form['cod_registro']
            fabricante = request.form['fabricante']
            tipo = request.form['tipo'] 
            descricao = request.form['descricao']
            quantidade = '0'

            insert = "INSERT INTO produto(cod_registro, nome, fabricante, tipo, quantidade, descricao) VALUES (%s, %s, %s, %s, %s, %s)"
            dados = (cod_registro, nome, fabricante, tipo, quantidade, descricao)

            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(insert, dados)
            conn.commit()

            cursor.close()
            conn.close()

            return redirect(url_for('pag_home'))
        
        except Exception:
            flash('Erro ao Cadastrar')

    return render_template('Cadastro.html')


@app.route('/pag_estoque', methods=['GET', 'POST'])
def selecione_produto():
    if request.method == 'GET':
        try:
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)
            cursor.execute("SELECT * FROM produto")
            rows = cursor.fetchall()
        except:
            return 'ERRO'
        finally:
            conn.close()
            cursor.close()

        return render_template('Estoque.html', rows=rows)
    
    elif request.method == 'POST':
         
         return movimento()

def movimento():

    movimentacao = request.form['movimentacao']

    if movimentacao == 'Entrada':

        try:
            registro_qtd = request.form['registro']
            quantidade = request.form['quantidade']
            data_atualizacao = request.form['data']
            local = request.form['local']

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

    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM produto WHERE cod_registro=%s", (id))
        conn.commit()

        return redirect('/')

    except Exception as e:
        print(e)
    
    finally:
        cursor.close() 
        conn.close()








# abrindo servidor
if __name__ == '__main__':
    app.run(debug=True)