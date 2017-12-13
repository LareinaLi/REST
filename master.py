import jason
import time
import request
import getpass
from flask import Flask
from flask_restful import Resource, Api, reqparse

app = Flask(__name__)
api = Api(app)


class Complexity(Resource):
    def __init__(self):
        self.master = m
        self.parser = reqparse.RequestParser()
        self.reqparser.add_argument('commit', type=str, location='json')
        self.reqparser.add_argument('complexity', type=str, location='json')

    def get(self):
        if self.master.workerNum < self.master.workerSum:
            return {'sha': -1}
        if len(self.master.commitList) == 0:
            return {'commit': 0}
        commit = self.master.commitList[0]
        del self.master.commitList[0]
        return {'commit': commit}

    def post(self):
        args = self.reqparser.parse_args()
        self.master.complexityList.append({'sha': args['commitSha'], 'complexity': args['complexity']})
        if len(self.master.complexityList) == self.master.commitNum:
            endTime = time() - self.master.startTime
            totalComplexity = 0
            for c in self.master.complexityList:
                if float(c['complexity']) > 0:
                    totalComplexity += float(c['complexity'])
                else:
                    print('Commmit ', c['sha'], ' is not computable.')
            aveComplexity = totalComplexity / len(self.master.complexityList)
            print('Average complexity: ', aveComplexity)
            print('Calculate Time: ', endTime, ' seconds\n')
        return {'success': True}


api.add_resource(Complexity, "/complexity", endpoint="complexity")


class Master:
    def __init__(self):
        self.startTime = 0.0
        self.workerTotal = int(input('The number of workers you need: '))
        self.workerNum = 0.0

        githubID = input('Please input your Github username or email address: ')
        githubPwd = getpass.getpass('Please input your password: ')

        self.commitList = []
        currentPage = 1
        morePage = True

        while morePage:
            commitURL = 'https://api.github.com/repos/rubik/argon/commits?page=' + currentPage + '&per_page=100'
            if len(githubID) == 0:
                response = requests.get(commitURL)
            else:
                response = requests.get(commitURL, auth=(githubID, githubPwd))
            self.data = json.loads(response.text)
            if len(data) < 2:
                morePage = False
            currentPage += 1

        for d in self.data:
            self.commitList.append(d['sha'])
        self.commitNum = len(self.commitList)
        print('Total number of commits is: ', self.commitNum)

        self.complexityList = []


if __name__ == '__main__':
    m = Master()
    app.run(port=9999)
