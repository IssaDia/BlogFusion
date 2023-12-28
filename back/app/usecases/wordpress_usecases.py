from entities.article import Article
from providers.wordpress.wordpress_provider import WORDPRESSPROVIDER
from typing import List


class WORDPRESSSCRAPERUSECASE:
    def __init__(self):
        self.provider = WORDPRESSPROVIDER()

    def get_articles(self)-> List[dict]:
        articles = self.provider.get_articles()
        print(f"Number of articles: {len(articles)}")
        articles_dict = [article.to_dict() for article in articles]
        return articles_dict