from crud import db,app
import sqlalchemy
from crud.models import Messages
from config import SQLALCHEMY_DATABASE_URI


try:
    db_uri = app.config['SQLALCHEMY_DATABASE_URI']
    engine = sqlalchemy.create_engine(db_uri)
    conn = engine.connect()
    conn.execute("commit")
    conn.execute("CREATE DATABASE " + app.config['DATABASE_NAME'])
    conn.close()

except:
    print ("Database exists")

db.create_all()
