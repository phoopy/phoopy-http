import cherrypy
from flask import Flask
from paste.translogger import TransLogger


class Application(object):
    def __init__(self, logger, debug, flask_config):
        self.debug = debug
        self.logger = logger
        self.flask = self.create_flask_application(flask_config)

    def create_flask_application(self, flask_config):
        app = Flask(
            'phoopy_http_server',
            template_folder=flask_config['template_folder']
        )

        default_config = {}

        if self.debug:
            default_config.update({
                'ENV': 'testing',
                'DEBUG': True,
                'TESTING': True,
                'TEMPLATES_AUTO_RELOAD': True,
            })

        app.config.update(default_config)
        app.logger.handlers = [handler for handler in self.logger.handlers]

        custom_config = flask_config.get('config', None)
        if custom_config:
            app.config.update(custom_config)

        return app

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
            app_wrapper = TransLogger(self.flask.wsgi_app, logger=self.logger)
            cherrypy.tree.graft(app_wrapper, '/')
            cherrypy.config.update({
                'server.socket_host': host,
                'server.socket_port': port,
                'engine.autoreload.on': False,
                'server.max_request_body_size': self.flask.config.get('MAX_CONTENT_LENGTH', 0),
            })
            cherrypy.engine.start()
            cherrypy.engine.block()
