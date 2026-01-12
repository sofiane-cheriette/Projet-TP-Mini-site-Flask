"""
Routes Flask pour le mini catalogue de jeux vidéo
"""
import json
import os
from flask import render_template, abort
from app import app


def load_items():
    """Charge les données depuis le fichier JSON"""
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'items.json')
    with open(json_path, encoding='utf-8') as f:
        return json.load(f)


@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')


@app.route('/items')
def items_list():
    """Liste de tous les éléments du catalogue"""
    items = load_items()
    return render_template('items_list.html', items=items)


@app.route('/items/<int:item_id>')
def item_detail(item_id):
    """Détail d'un élément spécifique"""
    items = load_items()
    item = next((i for i in items if i['id'] == item_id), None)
    if item is None:
        abort(404)
    return render_template('item_detail.html', item=item)


@app.route('/about')
def about():
    """Page À propos"""
    return render_template('about.html')


@app.errorhandler(404)
def page_not_found(e):
    """Page d'erreur 404 personnalisée"""
    return render_template('404.html'), 404
