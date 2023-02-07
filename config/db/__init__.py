from flask_sqlalchemy import SQLAlchemy

def init_db(*, app):
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:jzy@localhost:5006/base'
    app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
    db = SQLAlchemy()
    db.init_app(app=app)
    return db
