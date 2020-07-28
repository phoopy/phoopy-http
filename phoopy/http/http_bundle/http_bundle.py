from phoopy.kernel import Bundle
from os import path


class HttpBundle(Bundle):
    def __init__(self, template_folder=None, config=None, disable_file_log=False):
        super(HttpBundle, self).__init__()
        self.template_folder = template_folder
        self.disable_file_log = disable_file_log
        self.config = config

    def service_path(self):
        return path.join(self.get_bundle_dir(), 'config', 'services.yml')  # pragma: no cover

    def setup(self):
        container = self.get_container()
        flask_config = {
            'template_folder': self.template_folder,
            'config': self.config,
        }
        container['flask.config'] = lambda c: flask_config
        phoopy_http_config = {
            'disable_file_log': self.disable_file_log,
        }
        container['phoopy_http.config'] = lambda c: phoopy_http_config
