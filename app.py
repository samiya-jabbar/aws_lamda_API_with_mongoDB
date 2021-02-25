from flask import Flask, request, Response, jsonify
from database.db import initialize_db
from database.models import Items
import json

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb+srv://samiya:samiya@shopping-items.zsh4u.mongodb.net/shopping-items-bag'
}

initialize_db(app)

@app.route('/')
def get_root():
    return "<h1>Hello Welcome to our Shop, which item do you want to buy?<h1>"


@app.route('/getitems')
def get_items():
    items = Items.objects().to_json()
    return Response(items, mimetype="application/json", status=200)

@app.route('/additem', methods=['POST'])
def add_item():
    body = request.get_json()
    item = Items(**body).save()
    id = item.id
    return {'id': str(id)}, 200

@app.route('/<string:name>')
def get_item(name):
    if name==name:
        items = Items.objects.get(name=name).to_json()
        return Response(items, mimetype="application/json", status=200)

@app.errorhandler(500)
def handle_500(e):
    return '<h1>Sorry! the item you want to buy is not available in this shop<h1>'


if __name__=="__main__":
    app.run()
