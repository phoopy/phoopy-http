from phoopy.kernel import Bundle
from os import path


class HttpBundle(Bundle):
    def __init__(self, template_folder=None):
        super(HttpBundle, self).__init__()
        self.template_folder = template_folder

    def service_path(self):
        return path.join(self.get_bundle_dir(), 'config', 'services.yml')  # pragma: no cover

    def setup(self):
        container = self.get_container()
        flask_config = {
            'template_folder': self.template_folder,
        }
        container['flask.config'] = lambda c: flask_config
