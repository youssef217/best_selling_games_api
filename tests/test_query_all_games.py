from sqlalchemy import engine
from app.queries import query_all_games
from run import get_all_games


def test_query_all_games():
    records = query_all_games()
    assert isinstance(records, list)
    assert len(records) == 51
    for rec in records:
        assert type(rec) == engine.row.Row
        assert len(rec) == 7


def test_get_all_games():
    data = get_all_games()
    data = data["result"]
    assert isinstance(data, list)
    assert len(data) == 51
    keys = [
        'id',
        'title',
        'sales',
        'platform',
        'release_date',
        'developer',
        'publisher'
    ]
    for rec in data:
        assert isinstance(rec, dict)
        assert len(rec) == 7
        assert keys == list(rec.keys())
