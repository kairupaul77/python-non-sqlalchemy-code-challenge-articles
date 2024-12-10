class Article:
    # Class level list to store all Article instances
    all = []

    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self._title = title  # Use a private variable
        Article.all.append(self)

    # Acesses
    @property
    def title(self):
        return self._title  # Provide read-only access to the title


class Author:
    def __init__(self, name):
        self._name = name

    # Accesses 
    @property
    def name(self):
        return self._name  # Provide read-only access to the name

    def articles(self):
        # Return a list of articles where the author matches self
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        # Collect unique magazines where the author has written articles
        return list({article.magazine for article in Article.all if article.author == self})

    def add_article(self, magazine, title):
        # Create a new article and return it
        new_article = Article(self, magazine, title)
        return new_article

    def topic_areas(self):
        # Use the magazines method to get all magazines and extract their categories
        topic_areas = {magazine.category for magazine in self.magazines()}
        return list(topic_areas) if topic_areas else None


class Magazine:
    def __init__(self, name, category):
        self._name = None  # Use a private attribute for name
        self._category = None  # Use a private attribute for category
        self.name = name  # Use the property setter
        self.category = category  # Use the property setter

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Magazine name must be a string.")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Magazine category must be a string.")
        if not value:
            raise ValueError("Magazine category cannot be empty.")
        self._category = value

    def articles(self):
        # Return a list of articles where the magazine matches self
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        # Collect unique authors who have contributed to the magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Return a list of titles for all articles written for this magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):
        # Return a list of authors who have written more than one article for this magazine
        author_counts = {}
        for article in self.articles():
            author = article.author
            author_counts[author] = author_counts.get(author, 0) + 1

        # Filter authors who have written more than 2 articles
        authors_with_multiple_articles = [author for author, count in author_counts.items() if count > 2]

        # Return None if no authors meet the condition, otherwise return the list
        return authors_with_multiple_articles if authors_with_multiple_articles else None
