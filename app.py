from flask import Flask
from flask import request
from flask_sqlalchemy import SQLAlchemy
from tracker.database import reinit_db, db_session
from tracker.models import User

app = Flask(__name__)
reinit_db()


@app.route('/')
def hello():
    return 'hello world'

@app.route('/api/users', methods=["POST"])
def create_users():
    u = User(request.form["name"], request.form["email"])
    db_session.add(u)
    db_session.commit()
    return f'{u.name} has commited.'
    



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
