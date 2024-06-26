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
        cognom1 = data['cognom1']
        cognom2 = data['cognom2']
        telefon = data['telefon']
        CRUD.connectar()
        id_saved =client.create(nom,cognom1,cognom2,telefon)
        CRUD.desconnectar()
       
        # TODO Save data (database insert)
        
        # Redirect to show page
        return redirect(url_for('resource_read', id=id_saved))
    else:
        # Not found response
        abort(404)

@app.route('/clients/read/<int:id>')
def resource_read(id):
    # TODO Get data (database select)
    CRUD.connectar()
    dades=client.read(id)
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


@app.route('/clients/update/<int:id>', methods=["GET", "POST"])
def resource_update(id):
    if request.method == 'GET':
        CRUD.connectar()
        dades=client.read(id)
        CRUD.desconnectar()
        return render_template('clients/update.html', dades=dades)
    
    elif request.method == 'POST':
        # Get POST data
        data = request.form
        nom = data['nom']
        cognom1 = data['cognom1']
        cognom2 = data['cognom2']
        telefon = data['telefon']
        CRUD.connectar()
        id_saved = client.update(id, nom, cognom1, cognom2, telefon)
        CRUD.desconnectar()
       
        # TODO Save data (database insert)
        # Redirect to show page
        return redirect(url_for('resource_list', id=id_saved))
    else:
        # Not found response
        abort(404)

@app.route('/clients/delete/<int:id>', methods=["GET", "POST"])
def resource_delete(id):
    if request.method == 'GET':
        CRUD.connectar()
        dades=client.read(id)
        CRUD.desconnectar()
        return render_template('clients/delete.html', dades=dades)
    
    elif request.method == 'POST':
        # Get POST data
        CRUD.connectar()
        client.delete(id)
        CRUD.desconnectar()
       
        # TODO Save data (database insert)
        # Redirect to show page
        return redirect(url_for('resource_list'))
    else:
        # Not found response
        abort(404)



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