# RESTful Complexity Calculation

for class CS7NS1

Student: Xuan Li

StudentID: 17303493

This system can calculate the complexity for each commit in the repository https://github.com/rubik/radon, also the average complexity.

Before running the scripts, these four things must be installed.
```
pip install flask  # for restful
pip install flask_restful
pip install requests
pip install radon  # for calculating complexity
```

To run the system:

```
python master.py  # must imput the number of workers you need
python worker.py  # must run for times, just equals to the number you input in 'master.py'
```
