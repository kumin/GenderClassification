import falcon
from GenderPrediction import GenderPrediction


class SexService(object):
    def __init__(self):
        self.predictor = GenderPrediction()

    def on_get(self, req, resp):
        name = req.get_param('name')
        gender = self.predictor.get_gender_by_name(name)
        resp.status = falcon.HTTP_200
        resp.body = '{"gender":"' + str(gender) + '"}'


app = falcon.API()
service = SexService()
app.add_route("/gender", service)
