import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR,'weAct.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False