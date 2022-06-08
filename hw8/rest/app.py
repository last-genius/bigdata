from flask import Flask, request
from cassandra_client import CassandraClient
from json import dumps

app = Flask(__name__)


@app.route("/", methods=['POST'])
def main():
    client = CassandraClient('cassandra-server', 9042, 'hw8')
    client.connect()
    data = request.get_json()

    method = None
    try:
        method = getattr(client, f'select_{data["type"]}')
    except AttributeError:
        raise NotImplementedError(data["type"])

    return dumps(method(data), indent=4, default=str)


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
