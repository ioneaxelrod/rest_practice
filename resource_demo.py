import json
import falcon


class Resource:

    def __init__(self):
        self.docs = {
            'results': [
                {
                    'name': 'malia',
                    'age': 28,
                },
                {
                    'name': 'yun',
                    'age': 31,
                },
                {
                    'name': 'jacob',
                    'age': 26,
                }
            ]
        }

    def on_get(self, req, resp, index=None):
        # Create a JSON representation of the resource
        if not index:
            resp.body = json.dumps(self.docs, ensure_ascii=False)

            # The following line can be omitted because 200 is the default
            # status returned by the framework, but it is included here to
            # illustrate how this may be overridden as needed.
            resp.status = falcon.HTTP_200
        else:
            resp.body = json.dumps(self.docs['results'][index])
            resp.status = falcon.HTTP_200

    def on_post(self, req, resp):
        data = json.loads(req.stream.read().decode('utf-8'))

        self.docs['results'].append(data)

        body = {
            'response': 'Ok',
            'created_data': self.docs['results'][-1]
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201

    def on_put(self, req, resp, index):
        data = json.loads(req.stream.read().decode('utf-8'))

        for key in data:
            self.docs['results'][index][key] = data[key]

        body = {
            'response': 'Ok',
            'changed_data': self.docs['results'][index]
        }

        resp.body = json.dumps(body, ensure_ascii=False)
        resp.status = falcon.HTTP_201



