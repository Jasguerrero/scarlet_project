from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.post("/post_data")
def data_collection():
    data = request.json
    print(data)
    return "abc"


if __name__ == '__main__':
    app.run()
