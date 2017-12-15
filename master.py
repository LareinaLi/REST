import json
import time
import requests
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Master():
    def __init__(self):
        self.startTime = 0.0
        print('Work on the default repository: https://github.com/PyCQA/mccabe')
        self.workerTotal = int(input('Please input the number of workers you need: '))
        self.workerNum = 0

        self.commitList = []
        currentPage = 1
        morePage = True

        while morePage:
            commitURL = 'https://api.github.com/repos/PyCQA/mccabe/commits?page=' + str(currentPage) + '&per_page=100'
            response = requests.get(commitURL)
            data = json.loads(response.text)
            if len(data) < 2:
                morePage = False
                print('No more pages.')
            else:
                for d in data:
                    self.commitList.append(d['sha'])
                    print('Commit Sha:', str(d['sha']))
                currentPage += 1

        self.commitNum = len(self.commitList)
        self.complexityList = []
        print('Total number of commits is: ', str(self.commitNum))

class getRepo(Resource):
    def __init__(self):
        self.master = m
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('pullStatus', type=int, location='json')
        self.reqparser.add_argument('complexity', type=float, location='json')

    def get(self):
        args = self.reqparser.parse_args()
        if not args['pullStatus']:
            print('Got 1')
            return {'repo': 'https://github.com/PyCQA/mccabe'}
        if args['pullStatus']:
            self.master.workerNum += 1
            if self.master.workerNum == self.master.workerTotal:
                self.master.startTime = time.time()
            print('The number of workers is: ', str(self.master.workerNum))

    def post(self):
        pass


class Complexity(Resource):
    def __init__(self):
        self.master = m
        self.reqparser = reqparse.RequestParser()
        self.reqparser.add_argument('commitSha', type=str, location='json')
        self.reqparser.add_argument('complexity', type=float, location='json')

    def get(self):
        if self.master.workerNum < self.master.workerTotal:
            time.sleep(0.1)
            return {'sha': -2}
        if len(self.master.commitList) == 0:
            return {'sha': -1}
        commit = self.master.commitList[0]
        del self.master.commitList[0]
        print(commit)
        return {'sha': commit}

    def post(self):
        args = self.reqparser.parse_args()
        self.master.complexityList.append({'sha': args['commitSha'], 'complexity': args['complexity']})
        if len(self.master.complexityList) == self.master.commitNum:
            endTime = time.time() - self.master.startTime
            totalComplexity = 0.0
            for c in self.master.complexityList:
                if float(c['complexity']) > 0:
                    totalComplexity += float(c['complexity'])
                else:
                    print('Commmit ', c['sha'], ' is not computable.')
            aveComplexity = totalComplexity / len(self.master.complexityList)
            print('Average complexity: ', aveComplexity)
            print('Calculate Time: ', endTime, ' seconds\n')
        return {'success': True}

api.add_resource(getRepo, "/repo", endpoint="repo")
api.add_resource(Complexity, "/complexity", endpoint="complexity")

if __name__ == '__main__':
    m = Master()
    app.run(port=9999)
