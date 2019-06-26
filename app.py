from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from multiprocessing import Process

from tracker import routine
from tracker import database as db
from tracker._tracker import add, record, update

app = Flask(__name__)
db.init_db()


@app.route('/')
def hello():
    return 'hello world'


@app.route('/api/work', methods=["POST"])
def create_work():
    return add(request.form["uid"])


@app.route('/api/work', methods=["PUT"])
def update_work():
    return update(request.form["uid"])

if __name__ == "__main__":
    routine_process = Process(target=routine.run)
    routine_process.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
    routine_process.terminate()
