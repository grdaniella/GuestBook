from app import db
from datetime import date


class GuestBook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False, default=date.today)
    deleted = db.Column(db.Boolean)

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'date': self.date,
            'deleted': self.deleted
        }
