from flask import Flask, request, Response
from flask.json import jsonify, dumps
from flask_sqlalchemy import SQLAlchemy
from multiprocessing import Process

from tracker import routine
from tracker import database as db
from tracker._tracker import add, record, update, get_work

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


@app.route('/api/work/<uid>', methods=["GET"])
def getwork(uid):
    work = get_work(uid)
    if work:
        return jsonify(
            uid=work.uid,
            name=work.name,
            club=work.club,
            cvs=[cv.name for cv in work.cvs],
            series=work.series,
            publish_date=work.publish_date,
            records=[{
                'timestamp': record.timestamp,
                'dl_count': record.dl_count,
                'wishlist_count': record.wishlist_count
            } for record in work.records]
        )
    else:
        return "wut?"


if __name__ == "__main__":
    routine_process = Process(target=routine.run)
    routine_process.start()
    app.run(host="0.0.0.0", port=5000, debug=False)
    routine_process.terminate()
