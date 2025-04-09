import ckan.plugins as p
from .controller import helloworld_blueprint

class HelloWorldPlugin(p.SingletonPlugin):
    """Plugin that adds a new URL to the site to show some text."""
    p.implements(p.IBlueprint)

    def get_blueprint(self):
        """Return a Flask Blueprint object to define routes."""
        return helloworld_blueprint