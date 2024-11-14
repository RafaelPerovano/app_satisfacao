from flask import Flask, request, render_template, redirect, jsonify
import psycopg2
from psycopg2 import sql
from db import cursor, conn
app = Flask(__name__)

def bd():
    return 'CREATE TABLE usuarios (usuario int(1) not null, opcao int(1) not null, comentario varchar(100));'

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        usuario = request.form['usuario']
        opcao = request.form['opcao']
        comentario = request.form['comenarios']

        inserir_query = "INSERT INTO usuarios (usuario, opcao, comentarios) VALUES (%s, %s, %s)" # Verificar depois se da erro ao passar um comentario que não existe
        cursor.execute(inserir_query, (usuario, opcao))
        cursor.close()
        conn.close()

        return render_template('index.html')
        # return redirect('/login')
    else:
        return render_template('index.html')