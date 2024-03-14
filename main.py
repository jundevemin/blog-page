import requests
from flask import Flask, render_template

app = Flask(__name__)
BLOG_ENDPOINT = "https://api.npoint.io/674f5423f73deab1e9a7"

response = requests.get(url=BLOG_ENDPOINT)
blog_data = response.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_data)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def get_post(index):
    return render_template('post.html', article_id=index, posts=blog_data)


if __name__ == '__main__':
    app.run(debug=True, host="localhost")
