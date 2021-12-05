from flask_restful import Resource


class OrderInfo(Resource):
    def get(self):
        return "order infooo"

    def post(self):
        pass
