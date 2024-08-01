from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

posts = []

@app.route('/')
def index():
    return render_template('index.html', posts=posts)

@app.route('/post', methods=['POST'])
def post():
    name = request.form['name']
    message = request.form['message']
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    posts.append({'name': name, 'message': message, 'timestamp': timestamp})
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
