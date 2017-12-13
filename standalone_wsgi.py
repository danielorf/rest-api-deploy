from app import app
from db import db

db.init_app(app)
db.create_all()

if __name__ == "__main__":
    db.init_app(app)
    db.create_all()
    app.run()