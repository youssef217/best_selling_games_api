from app.db_conn import db_connection


db  = db_connection()

def query_all_games():
    records = db.execute(
        f"SELECT\
            *\
        FROM\
            games_api.games\
        ORDER BY\
            id"
    ).fetchall()
    db.commit()
    return records

def query_game_by_id(id):
    records = db.execute(
        f"SELECT\
            *\
        FROM\
            games_api.games\
        WHERE\
            id = {id}\
        ORDER BY\
            id"
    ).fetchone()
    db.commit()
    return records

def query_game_by_developer(developer):
    records = db.execute(
        f"SELECT\
            *\
        FROM\
            games_api.games\
        WHERE\
            developer = '{developer}'\
        ORDER BY\
            id"
    ).fetchall()
    db.commit()
    
    return records
