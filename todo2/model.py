import web

db = web.database (dbn="sqlite", name="data/main.sqlite3")

def get_all_todos():
    return db.select('todo', order='id')


