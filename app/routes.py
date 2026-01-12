"""
Routes Flask pour le mini catalogue de jeux vidéo
"""
import json
import os
from flask import render_template, abort, request
from app import app


def load_items():
    """Charge les données depuis le fichier JSON"""
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'items.json')
    with open(json_path, encoding='utf-8') as f:
        return json.load(f)


def get_unique_values(items, key):
    """Extrait les valeurs uniques d'une clé donnée"""
    return sorted(set(item[key] for item in items if key in item))


def get_year_ranges():
    """Retourne les plages d'années pour le filtrage"""
    return [
        ("2020-2025", "2020 - 2025"),
        ("2015-2019", "2015 - 2019"),
        ("2010-2014", "2010 - 2014"),
        ("2000-2009", "2000 - 2009"),
        ("avant-2000", "Avant 2000")
    ]


def filter_by_year_range(items, year_range):
    """Filtre les items par plage d'années"""
    if year_range == "2020-2025":
        return [i for i in items if 2020 <= i.get('year', 0) <= 2025]
    elif year_range == "2015-2019":
        return [i for i in items if 2015 <= i.get('year', 0) <= 2019]
    elif year_range == "2010-2014":
        return [i for i in items if 2010 <= i.get('year', 0) <= 2014]
    elif year_range == "2000-2009":
        return [i for i in items if 2000 <= i.get('year', 0) <= 2009]
    elif year_range == "avant-2000":
        return [i for i in items if i.get('year', 0) < 2000]
    return items


@app.route('/')
def index():
    """Page d'accueil"""
    return render_template('index.html')


@app.route('/items')
def items_list():
    """Liste de tous les éléments du catalogue avec recherche et filtrage"""
    all_items = load_items()
    
    # Récupérer les paramètres de recherche/filtrage
    search_query = request.args.get('q', '').strip().lower()
    genre_filter = request.args.get('genre', '')
    year_filter = request.args.get('year', '')
    platform_filter = request.args.get('platform', '')
    
    # Appliquer les filtres
    filtered_items = all_items
    
    # Filtre par recherche textuelle
    if search_query:
        filtered_items = [
            item for item in filtered_items
            if search_query in item.get('title', '').lower()
            or search_query in item.get('developer', '').lower()
            or search_query in item.get('description', '').lower()
        ]
    
    # Filtre par genre
    if genre_filter:
        filtered_items = [
            item for item in filtered_items
            if item.get('genre', '') == genre_filter
        ]
    
    # Filtre par plage d'années
    if year_filter:
        filtered_items = filter_by_year_range(filtered_items, year_filter)
    
    # Filtre par plateforme (recherche partielle)
    if platform_filter:
        filtered_items = [
            item for item in filtered_items
            if platform_filter.lower() in item.get('platform', '').lower()
        ]
    
    # Préparer les options de filtrage (basées sur tous les items)
    genres = get_unique_values(all_items, 'genre')
    platforms = get_unique_values(all_items, 'platform')
    year_ranges = get_year_ranges()
    
    return render_template(
        'items_list.html',
        items=filtered_items,
        total_items=len(all_items),
        genres=genres,
        platforms=platforms,
        year_ranges=year_ranges,
        current_search=search_query,
        current_genre=genre_filter,
        current_year=year_filter,
        current_platform=platform_filter
    )


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
