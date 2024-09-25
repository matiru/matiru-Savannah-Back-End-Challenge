# app.py
# app.py
from flask import Flask
from models import db
from config import Config
from routes import routes

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Load configuration from Config class

    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(routes)

    with app.app_context():
        db.create_all()  # Create tables if they don't exist

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
