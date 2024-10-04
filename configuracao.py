from database.database import db
from database.models.cliente import Cliente
from routes.home import home_route
from routes.cliente import cliente_route

def configure_tudo(app):
    configure_rotas(app)
    configure_db()

def configure_rotas(app):
    app.register_blueprint(home_route)
    app.register_blueprint(cliente_route, url_prefix='/clientes')

def configure_db():
    db.connect()
    db.create_tables([Cliente])