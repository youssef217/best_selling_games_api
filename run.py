from app.queries import query_all_games, query_game_by_id, query_game_by_developer
from flask import Flask


app = Flask(__name__)

@app.route("/")
def get_all_games():
    games = []
    records = query_all_games()
    for rec in records:
        game = {
            "id": rec[0],
            "title": rec[1],
            "sales": rec[2],
            "platform": rec[3],
            "release_date": rec[4],
            "developer": rec[5],
            "publisher": rec[6]
        }
        games.append(game)
    return {"result": games}


@app.route("/id=<id>")
def get_game_by_id(id):
    record = query_game_by_id(id)
    if record is None:
        return {"error": "Invalid Game ID"}
    game = {
        "id": record[0],
        "title": record[1],
        "sales": record[2],
        "platform": record[3],
        "release_date": record[4],
        "developer": record[5],
        "publisher": record[6]
    }
    return {"result": game}


@app.route("/developer=<developer>")
def get_game_by_developer(developer):
    games = []
    records = query_game_by_developer(developer)
    for rec in records:
        game = {
            "id": rec[0],
            "title": rec[1],
            "sales": rec[2],
            "platform": rec[3],
            "release_date": rec[4],
            "developer": rec[5],
            "publisher": rec[6]
        }
        games.append(game)
    return {"result": games}
