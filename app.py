import os
from dotenv import load_dotenv
from flask import Flask, render_template
from extensions import db
from routes.main import main

load_dotenv()


app = Flask(__name__)
app.secret_key = os.environ.get('APP_SECRET')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///test.db"

db.init_app(app)

app.register_blueprint(main, url_prefix='/')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)