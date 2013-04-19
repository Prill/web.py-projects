import web
import model

render = web.template.render("templates", base="base")

urls = (
    '/', 'Index',
)

class Index:
    def GET(self):
        todos = model.get_all_todos()
        return render.index(todos)

if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
