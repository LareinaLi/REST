# RESTful Complexity Calculation

for class CS7NS1

Student: Xuan Li

StudentID: 17303493

This system can calculate the complexity for each commit in the repository https://github.com/PyCQA/mccabe, also the average complexity.

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

The results of this system is stored in the file 'Result.pdf'. Time is calculated in seconds.

I have teste with 1 to 10 workers to see what happened. At the first stage, the time spent decreased as the number of worker increased. But when there are over 7 workers, the time increased. I think that's because there are only 109 commits, and the master would spend more time to assign works, which increase the calculating time.


Reference: https://github.com/suttonr0/Flask-RESTful-Cluster-Computing
