import json
import falcon
from model import User


class UserResource:

    def on_get(self, req, resp, id=None):

        if not id:
            resp.body = User.get_all_users_json()
        else:
            resp.body = User.get_user_json(id)

    def on_post(self, req, resp):

        data = json.loads(req.stream.read().decode('utf-8'))
        User.create_user_from_json(data)

        body = {
            'response': 'Ok',
            'created_data': data
        }
        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, id):

        data = json.loads(req.stream.read().decode('utf-8'))

        for key in data:
            User.update_user(id, key, data[key])

        body = {
            'response': 'Ok',
            'changed_data': data
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201