from flask import Flask, render_template


def run_server(host, port, api_host, api_port):
    """
    runs the ui server.

    :param host: ip to bind
    :param port: port to bind
    :param api_host: host of ui server
    :param api_port: port of ui server
    :return:
    """
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    @app.route("/")
    def index():
        return render_template("index.html", apisrv=f"http://{api_host}:{api_port}")

    app.run(host=host, port=port)
