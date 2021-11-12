from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'android_login.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xe9b"\xa8\rd\x07\xb3\xa0\x7f\x1b\xb2\xeav:\x13'