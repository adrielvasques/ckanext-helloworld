from ckan.plugins import implements, SingletonPlugin
from ckan.plugins import IRoutes

class HelloWorldPlugin(SingletonPlugin):
    """Plugin that should add a new URL to my site, and just show some text"""
    implements(IRoutes, inherit=True)
    
    def before_map(self, map):
        """
        Called before the routes map is generated. ``before_map`` is before any
        other mappings are created so can override all other mappings.
    
        :param map: Routes map object
        :returns: Modified version of the map object
        """
        
        # Identify the controller class for the new route
        controller = "ckanext.helloworld.controller:HelloWorldController"
        
        # Now build a route
        #   ``action`` is the method to call on the controller class
        #   ``conditions`` seem to apply conditions to the route. I don't know the limitations...
        map.connect('hello-world',
                    '/hello/world/:eggs',
                    controller=controller,
                    action="dispatch_get",
                    conditions={"method": ["GET"]})
        return map
    
    def after_map(self, map):
        """
        Called after routes map is set up. ``after_map`` can be used to
        add fall-back handlers.
    
        :param map: Routes map object
        :returns: Modified version of the map object
        """
        return map
