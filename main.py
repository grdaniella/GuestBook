from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY='should always be secret',

    # Database settings:
    SQLALCHEMY_DATABASE_URI='sqlite:///GuestBook.db',
    SQLALCHEMY_TRACK_MODIFICATIONS=False,

    WTF_CSRF_ENABLED=False
)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


def to_date(strdate):
    return datetime.strptime(strdate, "%Y-%m-%d").date()


class GuestBook(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    author = db.Column(db.String, nullable=False)
    text = db.Column(db.String, nullable=False)
    date = db.Column(db.Date, nullable=False)
    deleted = db.Column(db.Boolean)

    def to_json(self):
        return {
            'id': self.id,
            'author': self.author,
            'text': self.text,
            'date': self.date,
            'deleted': self.deleted
        }


@app.route('/')
def index():
    author = GuestBook.query.all()
    return jsonify({
        'author': [p.to_json() for p in author]
    })


if __name__ == '__main__':
    db.create_all()
    # Deleting all records:
    GuestBook.query.delete()
    ivan = GuestBook(
        author='Ivan',
        text='Some text',
        date=to_date('2020-12-11'),
        deleted=False)
    db.session.add(ivan)
    db.session.commit()  # note
    # Running app:
    app.run()
