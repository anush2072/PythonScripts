from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'hello': 'world'}

class LivenessProbe(Resource):
    def get(self):
        return {"message": "Engine is ALIVE"},201

class ReadinessProbe(Resource):
    def get(self):
        return {"message": "Engine is READY"},201

api.add_resource(HelloWorld, "/")
api.add_resource(LivenessProbe, '/health')
api.add_resource(ReadinessProbe, '/ready')

if __name__ == '__main__':
    app.run(debug=True)