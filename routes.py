# Створюємо файл із роутами, роути з якого потім заімпортовуємо у __init__.py.

from . import app
from flask import render_template
from dotenv import load_dotenv
import requests
import os


load_dotenv()


@app.route('/chuck_norris_facts', methods=['GET'])
def chuck_norris_facts():
    url = f'https://{os.getenv("API_HOST_RAPID")}/jokes/random'

    headers = {
        "X-RapidAPI-Key": os.getenv('API_KEY_RAPID'),
        "X-RapidAPI-Host": os.getenv('API_HOST_RAPID')
    }


    response = requests.get(url, headers=headers)
    result = response.json()

    return render_template('chuck_norris_funny_facts.html', answer=result['value'], title='Chuck Norris Jokes')