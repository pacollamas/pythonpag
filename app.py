##!/usr/bin/env python3

import logging
from flask import Flask, request, redirect, abort, render_template, url_for, flash

import CRUD, CRUD.cliente as client
app = Flask(__name__)

# Defineix el nivell per defecte de log
app.logger.setLevel(logging.INFO)

#SECRET_KEY: clau d'encriptació de la cookie
app.config.update(
    SECRET_KEY='secret_xxx'
)
@app.route("/")
def home():
    return render_template('index.html')

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    # Get value from URL
    return render_template('hello.html', name=name)

@app.route('/hello2')
def hello2():
    # Get value from URL query param
    # /hello2?alias=xxx
    param = request.args.get('alias')
    return render_template('hello.html', alias=param)

@app.route('/clients/create', methods=["GET", "POST"])
def resource_create():
    if request.method == 'GET':
        # Show form
        return render_template('clients/create.html')
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        nom = data['nom']
        cognom1 = data['Cognom1']
        cognom2 = data['Cognom2']
        telefon = data['telefon']
        CRUD.connectar()
        client.create(nom,cognom1,cognom2,telefon)
        CRUD.desconnectar()
        # saved_id = 1234
        # TODO Save data (database insert)
        
        # Redirect to show page
        # return redirect(url_for('clients/read.html', id=saved_id))
    else:
        # Not found response
        abort(404)

@app.route('/clients/read/<int:id>')
def resource_read(id):
    # TODO Get data (database select)
    CRUD.connectar()
    dades=client.list()
    CRUD.desconnectar()
    # Show data
    return render_template('clients/read.html',dades=dades)

@app.route('/clients/list')
def resource_list():
    # TODO Get data (database select)
    CRUD.connectar()
    dades=client.list()
    CRUD.desconnectar()
    # Show data
    return render_template('clients/list.html',dades=dades )

@app.route("/contacte", methods = ["GET", "POST"])
def contacte():
    if request.method == 'GET':
        # Show form
        return render_template('contacte.html')
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        email = data.get("email-contacte") 

        app.logger.info(f"Comentaris de {email}")
        # TODO: Add more logs 

        # Flash message to inform the user
        flash(f"En breu rebreu resposta a {email}")
        return redirect(url_for('thanks'))

@app.route("/thanks-for-your-comments") # default is GET
def thanks():
    return render_template('contacte-thanks.html')

# Run this application in debug mode ap port 5001
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)