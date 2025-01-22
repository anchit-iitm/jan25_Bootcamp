from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/as')
def hello_world():
    return 'Hello, World!'

@app.route('/as/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/ht')
def index():
    return render_template('index.html')

@app.route('/ht/1', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        var1 = request.form['name']
        return f'template print, {var1}!'
    else:
        return render_template('index1.html')

if __name__ == '__main__':
    app.run(debug=True)