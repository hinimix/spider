#coding:utf-8

from flask import Flask, render_template, jsonify
from flask.ext.script import Manager
from spider import DataGetModel
import json
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>wrong path</h1>'


@app.route('/icp/company/<url>/', methods=['GET'])
def get_tasks(url):
    datamodel = DataGetModel()
    html = datamodel.get_html_source(url.encode('utf-8'))
    table = datamodel.get_table_value(html)
    data = datamodel.get_data(table)
    return_value = {
        'status': 'OK',
        'code': 200,
        'auth-count': -1,
        'data': data
    }
    # return jsonify(_uniout.unescape(return_value, 'utf-8'))
    return json.dumps(return_value,ensure_ascii=False)


if __name__ == '__main__':
    # app.run(debug=True)
    manager.run()
