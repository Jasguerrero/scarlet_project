import traceback

import pymongo
from flask import Flask, request, jsonify, make_response

from data_entrypoint import DataEntryPoint
from lib.loot import Loot
from lib.session import Session

app = Flask(__name__)
mongo_client = pymongo.MongoClient()
data_entry_point = DataEntryPoint(mongo_client)


def validate_data(data):
    return "session" in data and "loot" in data


@app.post("/post_data")
def data_collection():
    data = request.json
    if not validate_data(data):
        return make_response(jsonify({"error": "missing fields"}), 400)
    try:
        session = Session(data['session'])
        loot = Loot(data['loot'])
        data_entry_point.save_point(session.session_data, loot.item_counts)
    except Exception:
        return make_response(jsonify({"error": traceback.format_exc()}), 500)

    return make_response({"sucess": "data saved"})


if __name__ == '__main__':
    app.run()
