La idea es desarrollar todo el proyecto en Flask con ayuda de un ORM (sqlalchemy) y un gestor de migraciones (Alembic).
-https://flask.palletsprojects.com/en/2.3.x/
https://www.sqlalchemy.org/
https://alembic.sqlalchemy.org/en/latest/index.html

## entre las ventajas, 
-el modelado facil y mapeado a la base de datos, actualizaciones rapidas, y la integracion en git hara facil ver la evolucion del modelo de datos.
-creacion de endpoints y routes limpia, todo el manejo de transacciones e interaccion con base de datos se hace de manera transparente. 

## conexion pgadmin:
usuario: test@test.com
password: pwd

Hostname: pgsql
Username: usr
Password: pwd



## creacion entorno virtual python:
  python3 -m venv .venv
activacion:
  source .venv/bin/activate
cargamos modulos:
  python3 -m pip install -r requirements.txt


## Flask cli
 https://flask.palletsprojects.com/en/2.3.x/cli/
 (como lanzar app en distintos modos, etc..)
 ## ejemplos con Flask shell

(.venv) n@n5:~/dev/workspace/BeCloud/codigo/siloin2/app$ flask shell
Python 3.8.10 (default, May 26 2023, 14:05:08) 
[GCC 9.4.0] on linux
App: init
Instance: /home/n/dev/workspace/BeCloud/codigo/siloin2/app/instance

# mapear objetos a bd: (vacia, sin usar alembic para migraciones)
>>> from database import init_db
>>> init_db()

# Añadir usuario:
>>> from database import db_session
>>> from models import User
>>> u = User(id=1, name='admin', email='admin@localhost', password='password')
>>> db_session.add(u)
>>> db_session.commit()

# select
>>> db_session.scalar(select(User)).all()
[<User 'admin'>,...]

>>> db_session.scalar(select(User).filter_by(name='admin')
<User 'admin'>
