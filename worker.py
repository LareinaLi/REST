import request
import json
import os
import commands


def Worker():
    masterURL = 'http://127.0.0.1:9999/repo'
    response = requests.get(masterURL, json={'pullStatus': False})
    data = json.loads(response.text)
    repoURL = data['repo']
    cmdLine = 'cd repoData &' \
              'rm -rf .git/ &' \
              'git init &' \
              'git remote add origin {} &' \
              'git pull'.format(repoURL)
    result = commands.getoutput(cmdLine)
    print(result.decode())
    response = requests.get(masterURL, json={'pullStatus': True})

    finishNum = 0
    moreCommit = True
    while moreCommit:
        response = requests.get('http://127.0.0.1:9999/complexity')
        data = json.loads(response.text)
        print(data)
        if data['sha'] == -1:
            print('Waiting for enough workers.')
        else:
            if data['sha'] == 0:
                print('No more commit.')
                break
            cmdLine = 'cd repoData &' \
                      'git reset --hard {}'.data['sha']
            result = commands.getoutput(cmdLine)
            print(result.decode())

            cmdLine = 'radon cc -a -s ' + repoData
            result = commands.getoutput(cmdLine)
            print(result.decode())
            finishNum += 1
    print('The number of commits have been calculated is: ', finishNum)

if __name__ == '__main__':
    Worker()
