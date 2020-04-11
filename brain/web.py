import pathlib

import click
from flask import Flask

app = Flask(__name__)

_INDEX_HTML = '''
<html>
    <head>
    <title>Brain Computer Interface</title>
        </head>
    <body>
        <ul>
            {users}
        </ul>
    </body>
</html>
'''
_USER_LINE_HTML = '''
<li><a href="/users/{user_id}">user {user_id}</a></li>
'''

USER_DATA_HTML = '''
<html>
    <head>
        <title>Brain Computer Interface: User {uid}</title>
    </head>
    <body>
        <table>
            {thoughts}
            </tr>
        </table>
    </body>
</html>
'''

THOUGHT_HTML = '''
<tr><td>{timestamp}</td><td>{thought}</td></tr>
'''


@click.command()
@click.option('--address', default="127.0.0.1:8080",
              help='Server address in [HOST]:[PORT] format. Default is 127.0.0.1:8080')
@click.option('--datadir', required=True,
              help='Data directory for the server.')
def run_webserver(address, datadir):
    @app.route('/')
    def index_html():
        users_html = []
        for user_dir in pathlib.Path(datadir).iterdir():
            users_html.append(_USER_LINE_HTML.format(user_id=user_dir.name))
        index_html = _INDEX_HTML.format(users='\n'.join(users_html))
        return index_html

    @app.route('/users/<userid>')
    def users_html(userid):
        user_path = pathlib.Path(datadir, userid)
        if not user_path.exists():
            return None

        thoughts = []
        for thought in user_path.iterdir():
            ts = thought.name
            ts_parts = ts[:ts.index(".")].split("_")
            ts = ts_parts[0] + " " + ts_parts[1].replace("-", ":")

            with open(thought, 'r') as f:
                thought_content = f.read()
                thoughts.append(THOUGHT_HTML.format(timestamp=ts, thought=thought_content))
        th_html = ''.join(thoughts)
        data = USER_DATA_HTML.format(uid=userid, thoughts=th_html)
        return data

    addr = address.split(':')
    app.run(host=addr[0], port=int(addr[1]))


if __name__ == '__main__':
    run_webserver()
