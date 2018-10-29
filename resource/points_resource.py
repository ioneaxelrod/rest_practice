import json
import falcon
from model import Points


class PointsResource:

    def on_get(self, req, resp, id=None):

        if not id:
            resp.body = Points.get_all_points_json()
        else:
            resp.body = Points.get_points_json(id)

    def on_post(self, req, resp):

        data = json.loads(req.stream.read().decode('utf-8'))
        Points.create_points_from_json(data)

        body = {
            'response': 'Ok',
            'created_data': data
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, id):

        data = json.loads(req.stream.read().decode('utf-8'))

        for key in data:
            Points.update_points(id, key, data[key])

        body = {
            'response': 'Ok',
            'changed_data': data
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201