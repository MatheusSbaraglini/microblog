"""user models."""
from app import DB


class Base(DB.Model):
    """ Define a base model. """

    __abstract__ = True

    id = DB.Column(DB.Integer, primary_key=True)
    date_created = DB.Column(DB.DateTime, default=DB.func.current_timestamp())
    date_modified = DB.Column(DB.DateTime, default=DB.func.current_timestamp(),
                              onupdate=DB.func.current_timestamp())


class User(Base):
    """ Define a User model. """

    __tablename__ = 'auth_user'

    name = DB.Column(DB.String(128), nullable=False)
    email = DB.Column(DB.String(128), nullable=False,
                      unique=True)
    password = DB.Column(DB.String(192), nullable=False)
    # role = DB.Column(DB.SmallInteger, nullable=False)
    # status = DB.Column(DB.SmallInteger, nullable=False)

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def __repr__(self):
        return '<User %r>' % (self.name)
