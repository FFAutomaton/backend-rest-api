from flask_restful import Resource


class OrderInfo(Resource):
    def get(self):
        return "order info"

    def post(self):
        pass
