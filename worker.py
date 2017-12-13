import jason
import os
import commands

def Worker():
    ip = '127.0.0.1'
    port = 9999

    cmdline = 'radon cc ' + filename + ' -a'
    result = commands.getoutput(cmdline)
    print(result)

if __name__ == '__main__':
    Worker()

