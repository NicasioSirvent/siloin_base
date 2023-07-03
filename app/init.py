from flask import Flask, jsonify, request
from logging.config import dictConfig

def create_app():

    dictConfig({
        'version': 1,
        'formatters': {'default': {
            'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
        }},
        'handlers': {'app_logger': {
            'class': 'logging.FileHandler',
            'filename': 'logs.log',
            'formatter': 'default'
        }},
        'root': {
            'level': 'INFO',
            'handlers': ['app_logger']
        }
    })

    # creamos aplicacion
    app = Flask(__name__)

    # configuracion conexion bd
    app.config["SECRET_KEY"] = "asdf"
    #app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://usr:pwd@pgsql:5432/siloin"
    #app.config["SQLALCHEMY_ECHO"] = True
    #app.config["SQLALCHEMY_RECORD_QUERIES"] = True


    # 404 generico.... logea error y devuelve json
    @app.errorhandler(404)
    def not_found(error):
        app.logger.info(
            f"404 => user tried to access route {request.full_path}"
        )
        return jsonify({
            "msg": "resource not found, aborting...",
            "success": False,
            "data": None
        }), 404

    return app