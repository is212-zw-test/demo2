from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# Globally accessible libraries
db = SQLAlchemy()
cors = CORS()

def init_app():
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object('config.Config')

    # Initialize Plugins
    db.init_app(app)
    cors.init_app(app)

    with app.app_context():
        # Include our Routes
        from .routes import role_listing_route
        # Register routes
        app.register_blueprint(role_listing_route.api, url_prefix='/api')

        # Register error handlers
        from . import errors
        app.register_error_handler(404, errors.handle_resource_not_found)
        app.register_error_handler(400, errors.handle_bad_request)
        app.register_error_handler(Exception, errors.handle_unhandled_exception)

        db.create_all() # Create database tables for our data models

        return app