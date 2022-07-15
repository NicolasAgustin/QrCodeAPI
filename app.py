import json

from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    print('hola')
    return json.dumps(
        {
            'name': 'nico',
            'email': 'nico@gmail.com'
        }
    )


if __name__ == '__main__':
    app.run()
