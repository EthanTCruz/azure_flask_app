from flask import Flask, jsonify


def get_app():
    app = Flask(__name__)
    @app.route("/")
    def hello():
        return jsonify({"Message": "How you doin' Emily"})
    return app

if __name__ == "__main__":

    app = get_app()
    app.run(host='0.0.0.0',port=5000, debug=True)