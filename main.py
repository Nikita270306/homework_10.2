from flask import Flask

from function import *

app = Flask(__name__)

@app.route('/')
def main_page():
    return information(load_candidates())


@app.route('/candidates/<int:x>')
def candidates_dan(x):
    return f'<img src="{get_by_pk(x)["picture"]}">\n{information([get_by_pk(3)])}'

@app.route('/skills/<x>')
def their_skills(x):
    return f'<pre>{information([get_by_skill(x)])}</pre>'

app.run()