import web

db = web.database (dbn="sqlite", db="data/main.sqlite3")

def get_all_todos():
    return db.select('todo', order='id')

def get_todo(todo_id):
    rows = db.select('todo', where='id=$todo_id', vars=locals())
    rowslist = list(rows)
    print len(rowslist), rowslist
    if len(rowslist) == 0:
        return None
    else:
        return rowslist[0]
