from flask import abort, jsonify, redirect, render_template, request, session, url_for, Flask, flash
import sys

from sqlalchemy import select
from database import db_session
from models import Usuario
from init import create_app

app = Flask(__name__)
app.config["SECRET_KEY"] = "asdf"

#app = create_app()

@app.route('/')
def index():
  return render_template('index.html', session=session)

@app.route('/login', methods=['GET','POST'])
def login():
  if request.method == 'POST':
    error = None
    #ver si username en bd:
    #myUser = db_session.scalar(select(User).filter_by(name=request.form['username']))
    myUser = db_session.scalar(select(Usuario).where(Usuario.nombre == request.form['username']))
    if not myUser:
      error = "Usuario no Existe"
      return render_template('login.html', error=error)

    #comprobar contraseña
    if request.form['password'] != myUser.clave:
      error = "Clave Erronea"
      return render_template('login.html', error=error)
      
    #ok
    flash('You were successfully logged in')
    session['name'] = myUser.nombre
    session['id'] = myUser.id
    return redirect(url_for('index'))
  else:         
    return render_template('login.html')

@app.route('/logout')
def logout():
  session.pop('name')
  session.pop('id')
  return redirect(url_for('index'))


@app.teardown_appcontext
def shutdown_session(exception=None):
  db_session.remove()

if __name__ == '__main__':
  app.run()