import json
import falcon
from model import Team


class TeamResource:

    def on_get(self, req, resp, id=None):

        if not id:
            resp.body = Team.get_all_teams_json()
        else:
            resp.body = Team.get_team_json(id)

    def on_post(self, req, resp):

        data = json.loads(req.stream.read().decode('utf-8'))
        Team.create_team_from_json(data)

        body = {
            'response': 'Ok',
            'created_data': data
        }
        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, id):

        data = json.loads(req.stream.read().decode('utf-8'))

        for key in data:
            Team.update_team(id, key, data[key])

        body = {
            'response': 'Ok',
            'changed_data': data
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201