import subprocess, time
from multiprocessing import Process
from functools import wraps
from collections import defaultdict


# IDEAS
# handle a list of hosts/commands
# different file types as commands (Python, C,BASH anything native to Linux)
# save files locally on each machine. 
# allow scheduling.

results = defaultdict(lambda: defaultdict(dict))

def run(host,command):
    ssh = subprocess.Popen(["ssh", "%s" % host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    now = time.time()
    results[host][command][now] = [i.strip('\n') for i in ssh.stdout.readlines()]
    return results[host][command]


if __name__=="__main__":
     HOST="localhost"
     import os
     os.getcwd()
     COMMAND="cd {}; ls".format(os.getcwd())
     print(run(HOST,COMMAND))

