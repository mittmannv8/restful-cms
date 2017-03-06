import falcon
import os
import jinja2
import settings


def load_template(name):
    path = os.path.join('templates', name)
    with open(os.path.abspath(path), 'r') as fp:
        return jinja2.Template(fp.read())



class HTMLTest:
    def on_get(self, request, response):
        template = load_template('base.html')

        response.status = falcon.HTTP_200
        response.content_type = 'text/html'
        response.body = template.render(title='Title Teste')

