from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/Заготовка')
def prepeare_to_mission():
    planet = 'Марс'
    return render_template('base.html', title=planet)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
