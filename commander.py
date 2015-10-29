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
    ssh, err = subprocess.Popen(["ssh", "%s" % host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE).communicate()
    now = time.time()
    results[host][command][now] = [i.strip('\n') for i in ssh.decode('UTF-8').splitlines()]
    return results[host][command]

def run_group(hosts,commands):
    res = defaultdict(lambda: defaultdict(dict))
    for host in hosts:
        for command in commands:
            res[host][command] = run(host,command)
    return res

if __name__=="__main__":
     HOSTS=["localhost" for i in range(2)]
     import os
     os.getcwd()
     COMMAND="cd {}; ls".format(os.getcwd())
     print(run_group(HOSTS,[COMMAND,'pwd']))
