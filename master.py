import commands
import jason
import time
import request
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)

task = []


class Complexity(Resource):
    def __init__(self):
        self.master = m
        self.parser = reqparse.RequestParser()
        self.reqparser.add_argument('file', type=str, location='json')
        self.reqparser.add_argument('complexity', type=str, location='json')

    def get(self):
        if self.master.workerNum < self.master.workerSum:
            return {'file': 'wait'}
        if len(self.master.file) == 0:
            return {'file': 'no file'}
        else:
            fileid = self.master.file[0]
            del self.master.file[0]
            return {'file': fileid}

    def put(self):
        if len(self.master.fileComplexity) == self.master.fileNum:
            endTime = time() - self.master.startTime
            totalComplexity = 0
            for c in self.master.fileComplexity:
                if float(c['complexity']) > 0:
                    totalComplexity += float(c['complexity'])
            aveComplexity = totalComplexity / len(self.master.complexity)
            print('Average complexity: ', aveComplexity, '\n')
            print('Calculate Time: ', endTime, ' seconds\n')


class Master:
    def __init__(self):
        self.startTime = 0.0
        self.workerTotal = int(input('The number of worker you need: '))
        self.workerNum = 0
        response = requests.get('url to github repo')
        data = json.loads(response)
        for d in data:
            self.file.append(d['id'])
        self.file = []
        self.complexity = []
        self.fileNum = len(self.file)
        print('The number of files: ', self.fileNum)

    def get(self):
        return {'hello': 'world'}




api.add_resource(Master, '/')

if __name__ == '__main__':
    m = Master()
    app.run(port=9999)
