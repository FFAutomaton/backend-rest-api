from flask_restful import Resource


# TODO burayi kubernetesle bagla ki data alalim kral
class DataRef(Resource):
    def get(self):
        return "data reeefff"

    def post(self):
        pass
