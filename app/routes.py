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


def load_news():
    """Charge les actualités depuis le fichier JSON"""
    json_path = os.path.join(os.path.dirname(__file__), 'data', 'news.json')
    with open(json_path, encoding='utf-8') as f:
        return json.load(f)


def get_unique_values(items, key):
    """Extrait les valeurs uniques d'une clé donnée"""
    return sorted(set(item[key] for item in items if key in item))


def get_years(items):
    """Retourne les années disponibles dans le catalogue (triées décroissant)"""
    years = sorted(set(item.get('year', 0) for item in items if item.get('year')), reverse=True)
    return years


def get_platforms():
    """Retourne les plateformes simplifiées comme Instant Gaming"""
    return [
        ("PC", "🖥️ PC"),
        ("PlayStation", "🎮 PlayStation"),
        ("Xbox", "🟢 Xbox"),
        ("Nintendo", "🔴 Nintendo")
    ]


def filter_by_year(items, year):
    """Filtre les items par année exacte"""
    try:
        year_int = int(year)
        return [i for i in items if i.get('year', 0) == year_int]
    except (ValueError, TypeError):
        return items


@app.route('/')
def index():
    """Page d'accueil avec jeux populaires et tendances"""
    all_items = load_items()
    
    # Jeux populaires (les mieux notés / classiques)
    popular_ids = [3, 4, 20, 1, 8]  # Elden Ring, Witcher 3, Baldur's Gate 3, Zelda, Cyberpunk
    popular_games = [item for item in all_items if item['id'] in popular_ids][:4]
    
    # Tendances (jeux récents 2020+)
    trending_games = [item for item in all_items if item.get('year', 0) >= 2020][:6]
    
    # Stats
    stats = {
        'total_games': len(all_items),
        'genres': len(set(item.get('genre', '') for item in all_items)),
        'recent': len([i for i in all_items if i.get('year', 0) >= 2020])
    }
    
    return render_template('index.html', 
                           popular_games=popular_games,
                           trending_games=trending_games,
                           stats=stats)


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
    
    # Filtre par année exacte
    if year_filter:
        filtered_items = filter_by_year(filtered_items, year_filter)
    
    # Filtre par plateforme (recherche partielle)
    if platform_filter:
        filtered_items = [
            item for item in filtered_items
            if platform_filter.lower() in item.get('platform', '').lower()
        ]
    
    # Préparer les options de filtrage
    genres = get_unique_values(all_items, 'genre')
    platforms = get_platforms()  # Plateformes simplifiées style Instant Gaming
    years = get_years(all_items)  # Années individuelles
    
    return render_template(
        'items_list.html',
        items=filtered_items,
        total_items=len(all_items),
        genres=genres,
        platforms=platforms,
        years=years,
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


@app.route('/privacy')
def privacy():
    """Page Politique de confidentialité"""
    return render_template('privacy.html')


@app.route('/cookies')
def cookies():
    """Page Politique des cookies"""
    return render_template('cookies.html')


@app.route('/news')
def news_list():
    """Liste des actualités"""
    news = load_news()
    return render_template('news_list.html', news=news)


@app.route('/news/<int:news_id>')
def news_detail(news_id):
    """Détail d'une actualité"""
    all_news = load_news()
    article = next((n for n in all_news if n['id'] == news_id), None)
    if article is None:
        abort(404)
    
    # Récupérer le jeu lié si applicable
    related_game = None
    if article.get('related_game_id'):
        items = load_items()
        related_game = next((i for i in items if i['id'] == article['related_game_id']), None)
    
    # Autres actualités (exclure l'article actuel)
    other_news = [n for n in all_news if n['id'] != news_id]
    
    return render_template('news_detail.html', 
                           article=article,
                           related_game=related_game,
                           other_news=other_news)


@app.errorhandler(404)
def page_not_found(e):
    """Page d'erreur 404 personnalisée"""
    return render_template('404.html'), 404
