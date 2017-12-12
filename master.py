import commands
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

task = []


class Master():
    def __init__(self):
        self.startTime = 0 
        self.workerNum = 0

    def get(self):
        return {'hello': 'world'}

    cmdline = 'radon cc ' + filename + ' -a'
    result = commands.getoutput(cmdline)
    print(result)


api.add_resource(Master, '/')

if __name__ == '__main__':
    app.run(port=9999)
