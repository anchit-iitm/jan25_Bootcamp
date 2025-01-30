from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/as')
def hello_world():
    return 'Hello, World!'

@app.route('/as/<name>')
def hello_name(name):
    return f'Hello, {name}!'

@app.route('/htp')
def index():
    return render_template('index.html')

@app.route('/ht/1', methods=['GET', 'POST'])
def index1():
    if request.method == 'POST':
        var1 = request.form['name']
        return f'template print, {var1}!'
    else:
        return render_template('index1.html')
    
@app.route('/ht/2', methods=['GET'])
def test_day3():
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)