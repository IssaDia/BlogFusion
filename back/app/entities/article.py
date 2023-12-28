import sqlite3

class Article:
    def __init__(self, title, content, slug, link, id=None):
        self.id = id
        self.title = title
        self.content = content
        self.slug = slug
        self.link = link

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'slug': self.slug,
            'link': self.link
        }
    
    def init_db():
        connection = sqlite3.connect('articles.db')
        cursor = connection.cursor()

        # Création de la table des articles
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS articles (
                id INTEGER PRIMARY KEY,
                title TEXT NOT NULL,
                content TEXT,
                slug TEXT NOT NULL,
                link TEXT
            )
        ''')

        connection.commit()
        connection.close()
    
  