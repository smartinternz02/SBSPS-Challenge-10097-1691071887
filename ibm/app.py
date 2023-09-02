from flask import Flask, render_template

app = Flask(__name__, template_folder='templates')

# Sample news articles data
news_articles = [
    {
        "title": "Breaking News 1",
        "content": "This is the content of the first news article."
    },
    {
        "title": "Breaking News 2",
        "content": "This is the content of the second news article."
    }
    # Add more news articles as needed
]

@app.route('/')
def index():
    return render_template('index.html', articles=news_articles)

if __name__ == '__main__':
    app.run(debug=True)
