from flask import Flask, jsonify
from entities.article import Article
from usecases.wordpress_usecases import WORDPRESSSCRAPERUSECASE
import sqlite3
from flask_cors import CORS



import os, sys
sys.path.insert(0, os.path.abspath(".."))

app = Flask(__name__)
CORS(app)


article = Article
Article.init_db()

@app.route("/articles", methods=["GET"])
def get_external_articles():
    usecase = WORDPRESSSCRAPERUSECASE()
    articles = usecase.get_articles()
    return jsonify(articles)

@app.route('/api/articles', methods=['GET'])
def get_db_articles():
    connection = sqlite3.connect('articles.db')
    cursor = connection.cursor()

    # Exécutez la requête SQL pour récupérer tous les articles
    cursor.execute('SELECT * FROM articles')
    articles = cursor.fetchall()

    # Fermez la connexion à la base de données
    connection.close()

    # Construisez la liste d'articles à partir des résultats de la requête
    articles_list = [{
        'id': article[0],
        'title': article[1],
        'content': article[2],
        'slug': article[3],
        'link': article[4]
    } for article in articles]

    return jsonify(articles_list)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000)