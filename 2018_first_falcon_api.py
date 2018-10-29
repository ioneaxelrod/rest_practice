import falcon
from resource_demo import Resource
from resource import PointsResource, UserResource, TeamResource
# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.

# falcon.API instances are callable WSGI apps
app = falcon.API()

# Resources are represented by long-lived class instances
things = Resource()
points_resource = PointsResource()
user_resource = UserResource()
team_resource = TeamResource()

# things will handle all requests to the '/things' URL path
app.add_route('/things', things)
app.add_route('/things/{index:int}', things)
app.add_route('/points', points_resource)
app.add_route('/points/{id:int}', points_resource)
app.add_route('/users/', user_resource)
app.add_route('/users/{id:int}', user_resource)
app.add_route('/teams', team_resource)
app.add_route('/teams/{id:int}', team_resource)
