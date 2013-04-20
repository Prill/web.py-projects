import web
import model

render = web.template.render("templates", base="base")

urls = (
    '/', 'Index',
    '/view/(\d+)/?', "View",
)

class Index:
    def GET(self):
        todos = model.get_all_todos()
        return render.index(todos)

class View:
    def GET(self,todo_id):
        todo = model.get_todo(todo_id)
        return render.view(todo)


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
