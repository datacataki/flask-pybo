import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'jumptoflask03.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY="dev"

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(
    user='dbmaskersuser',
    pw='[Un1UYRrS$fsRNT!F(x30#%g.mUCEx&U',
    url='ls-846c4623a449184c6b65a8d6bb58be75a0eb1e6f.cq29lywrlzdq.ap-northeast-2.rds.amazonaws.com',
    db='mimo01'
)

