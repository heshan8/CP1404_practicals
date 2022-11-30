from flask import Flask

app = Flask(__name__)


@app.route('/f')
@app.route('/f/<celsius>')
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit


if __name__ == '__main__':
    app.run()
