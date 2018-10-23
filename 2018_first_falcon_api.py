
import falcon
from resource_demo import Resource
from resource.points_resource import PointsResource

# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = Resource()
points_resource = PointsResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/things/{index:int}', things)
app.add_route('/points', points_resource)
app.add_route('/points/{id:int}', points_resource)
