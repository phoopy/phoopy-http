import cherrypy
from flask import Flask


class Application(object):
    def __init__(self, logger, debug, flask_config):
        self.flask = Flask(
            'phoopy_http_server',
            template_folder=flask_config['template_folder']
        )
        self.debug = debug

    def parse_controller(self, controller):
        for name in dir(controller):
            value = getattr(controller, name)
            if name.startswith("__") or not callable(value):
                continue
            if not hasattr(value, '__phoopy_http_annotations__'):
                continue
            annotations = getattr(value, '__phoopy_http_annotations__')
            for annotation in annotations:
                annotation.apply(self.flask, controller)

    def listen(self, host, port):
        if self.debug:
            self.flask.run(host, port)
        else:
            cherrypy.tree.graft(self.flask.wsgi_app, '/')
            cherrypy.config.update({
                'server.socket_host': host,
                'server.socket_port': port,
                'engine.autoreload.on': False,
            })
            cherrypy.engine.start()
