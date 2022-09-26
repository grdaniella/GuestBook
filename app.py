from flask import Flask, request, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
import config as config

app = Flask(__name__)
app.config.update(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)


# def to_date(strdate):
#     return datetime.strptime(strdate, "%Y-%m-%d").date()


@app.route('/')
def index():
    from models import GuestBook
    author = GuestBook.query.all()
    return jsonify({
        'author': [p.to_json() for p in author]
    })


@app.route('/create')
def add_post():
    from models import GuestBook
    from forms import GuestBookForm
    if request.method == 'POST':
        form = GuestBookForm(request.form)

        if form.validate():
            post = GuestBook(**form.data)
            db.session.add(post)
            db.session.commit()

            flash('Post was added!')
        else:
            flash('Form is not valid! Post was not created.')
            flash(str(form.errors))
    posts = GuestBook.query.all()
    for post in posts:
        print(post)


if __name__ == '__main__':
    from models import *
    db.create_all()
    # # Deleting all records:
    # GuestBook.query.delete()
    # Running app:
    app.run()
