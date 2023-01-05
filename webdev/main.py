import web

urls = (
    '/(.*)', 'index'
)

app = web.application(urls, globals())

class index:
    def GET(self, name):
        return "Hello " + name + ' sup'

if __name__ == "__main__":
    app.run()