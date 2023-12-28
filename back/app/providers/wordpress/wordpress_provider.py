from entities.article import Article
from interfaces.data_provider_interfaces import DATAPROVIDERINTERFACE
from utils.functions import get_stripped_content
from utils.functions import remove_encoded_chars

import requests, os
import sqlite3


from dotenv import load_dotenv
load_dotenv()

wordpress_api_url = os.environ.get("WORDPRESS_API_URL")

class WORDPRESSPROVIDER(DATAPROVIDERINTERFACE):
    def __init__(self,  database_path='articles.db'):
        self.connection = sqlite3.connect(database_path)
        self.create_table()
    
    def create_table(self):
        cursor = self.connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT NOT NULL,
                slug TEXT NOT NULL,
                link TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def get_articles(self):
        response = requests.get(wordpress_api_url + "/wp-json/wp/v2/posts/?per_page=100")
        print(response.status_code)
        articles = []
        if response.status_code == 200:
            data = response.json()
            id = 1
            for data_article in data:
                title = data_article["title"]["rendered"]
                content = data_article["content"]["rendered"]
                slug = data_article["slug"]
                link = data_article["link"]
                article = Article(
                  title, content, slug, link)
                self.insert_article((title, content, slug, link))
                articles.append(article)
                id += 1
            return articles
        
    def insert_article(self, article):
        cursor = self.connection.cursor()
        cursor.execute('''
            INSERT INTO articles (title, content, slug, link)
            VALUES (?, ?, ?, ?)
        ''', article)
        self.connection.commit()
           