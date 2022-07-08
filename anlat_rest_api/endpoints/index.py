from flask_restful import Resource

class Index(Resource):
    def get(self):
        return 'Welcome to Index'
    def post(self):
        pass