from flask import Flask, render_template, send_from_directory


def run_ui_server(host, port, api):
    """
    runs the ui server.

    :param host: ip to bind
    :param port: port to bind
    :param api: url of the api server in the form http://ip:port
    :return:
    """
    app = Flask(__name__, static_folder="build/static", template_folder="build")

    @app.route('/favicon.ico')
    def favicon():
        return send_from_directory('build',
                                   'favicon.ico', mimetype='image/vnd.microsoft.icon')

    @app.route("/")
    def index():
        return render_template("index.html", apisrv=api)

    app.run(host=host, port=port)
