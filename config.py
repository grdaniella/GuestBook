DEBUG = True,
SECRET_KEY = 'should always be secret',

# Database settings:
SQLALCHEMY_DATABASE_URI = 'sqlite:///GuestBook.db',
SQLALCHEMY_TRACK_MODIFICATIONS = False,
WTF_CSRF_ENABLED = False

