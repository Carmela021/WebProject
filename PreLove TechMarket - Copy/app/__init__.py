from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
                # ,template_folder='templates', 
                # static_folder='static')
    
    app.config['SQLALCHEMY_DATABASE_URI'] = \
        'mysql+pymysql://root:@localhost/preloved_db'
    app.config['SECRET_KEY'] = 'preloved-techmarket-2026'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    from app.controllers.product import product_bp
    from app.controllers.pages import pages_bp

    app.register_blueprint(product_bp)
    app.register_blueprint(pages_bp) 

    return app