from flask import render_template, Flask
import requests
app = Flask(__name__)


posts = requests.get('https://api.npoint.io/23e6704409b497819260').json()


@app.route('/')
def home():
    return render_template('index.html', all_posts=posts)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/post')
def post():
    return render_template('post.html')


if __name__ == '__main__':
    app.run(debug=True)
