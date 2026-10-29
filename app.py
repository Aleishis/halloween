from flask import Flask, render_template, request, redirect
from entities.monster import Monster

app = Flask(__name__)


@app.route('/')
def index():
    monsters = Monster.get_all()
    added = request.args.get('added') == '1'
    return render_template('index.html', monsters=monsters, added=added)


@app.route('/monster', methods=['POST'])
def save_monster():
    monster = Monster(name=request.form['name'],
                      power=request.form['power'])
    monster.save()
    return redirect('/?added=1')


if __name__ == '__main__':
    app.run(debug=True)
