# -*- coding: utf-8 -*-

from phoopy.http.core import Application
from phoopy.console import AbstractCommand


class ServerStartCommand(AbstractCommand):
    """
    Start HTTP Server

    server:start

    {--host=127.0.0.1 : Host}
    {--port=9000 : Port}
    {--debug : Enable debugging server}
    """
    def __init__(self, logger, container, flask_config):
        super(ServerStartCommand, self).__init__(logger)
        self.container = container
        self.flask_config = flask_config

    def handle(self):
        self.setup_logger()

        debug = self.option('debug')
        host = self.option('host')
        port = int(self.option('port'))

        application = Application(self.logger, debug, self.flask_config)

        controllers = self.container.get_tagged_entries("controller")
        for controller in controllers:
            application.parse_controller(controller)

        application.listen(host, port)
