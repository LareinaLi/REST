import requests
import json
import subprocess


def Worker():
    masterURL = 'http://127.0.0.1:9999/repo'
    response = requests.get(masterURL, json={'pullStatus': False})
    data = json.loads(response.text)
    repoURL = data['repo']
    bashCommand = "cd repoData &" \
                  "rm -rf .git/ &" \
                  "git init &" \
                  "git remote add origin {} &" \
                  "git pull".format(repoURL)
    subprocess.Popen(bashCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    response = requests.get(masterURL, json={'pullStatus': True})

    finishNum = 0
    moreCommit = True
    while moreCommit:
        response = requests.get('http://127.0.0.1:9999/complexity')
        data = json.loads(response.text)
        print(data)
        print('Received: ', str(data['sha']))

        if data['sha'] == -2:
            print('Waiting for enough workers.')
        else:
            if data['sha'] == -1:
                print('No more commit.')
                break

            bashCommand = "cd repoData &" \
                          "git reset --hard {}".format(data['sha'])
            subprocess.Popen(bashCommand, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            cmdLine = 'radon cc -a -s repoData'
            result = subprocess.check_output(cmdLine).decode()
            print(result)

            aveComplexityPos = result.rfind('(')
            if result[aveComplexityPos + 1:-2] == '':
                print('No computable files.')
                response = requests.post('http://127.0.0.1:9999/complexity',
                                         json={'commitSha': data['sha'], 'complexity': -1})
            else:
                aveComplexity = float(result[aveComplexityPos + 1:-2])
                response = requests.post('http://127.0.0.1:9999/complexity',
                                         json={'commit': data['sha'], 'complexity': aveComplexity})

            finishNum += 1
    print('The number of commits have been calculated is: ', str(finishNum))


if __name__ == '__main__':
    Worker()
