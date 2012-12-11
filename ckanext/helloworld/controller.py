from ckan.lib.base import BaseController

class HelloWorldController(BaseController):
    def dispatch_get(self, *args, **kwargs):
        return "Hello World! Here are your %s" % kwargs['eggs']