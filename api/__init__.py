from flask import Flask
from flask_cors import CORS
import logging
from api.main import main

def create_app(config_file='settings.py'):
    app = Flask(__name__)

    app.config.from_pyfile(config_file)

    logging.basicConfig(level=logging.DEBUG)

    app.register_blueprint(main)

    # app.cli.add_command(create_tables)
    # app.cli.add_command(delete_user)
    # app.cli.add_command(send_blast)
    # app.cli.add_command(temp_migrate)
    # app.cli.add_command(upgrade)
    # app.cli.add_command(add_column)
    # app.cli.add_command(fill_closet_index)


    CORS(app)

    # Talisman(app)

    return app