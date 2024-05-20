# Створюємо файл, де відбуватимуться основні процеси і який відповідатиме за роботу програми.

import os
from dotenv import load_dotenv
from flask import Flask


load_dotenv()


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')


from . import routes



if __name__ == "__main__":
    app.run(debug=True)