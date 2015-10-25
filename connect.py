import subprocess

from multiprocessing import Process
from functools import wraps
# IDEAS
# handle a list of hosts/commands
# different file types as commands (Python, C,BASH anything native to Linux)
# save files locally on each machine. 
# allow scheduling.

def run(host,command):
    ssh = subprocess.Popen(["ssh", "%s" % host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    return result

if __name__=="__main__":
     HOST="localhost"
     import os
     os.getcwd()
     COMMAND="cd {}; ls".format(os.getcwd())
     print(run(HOST,COMMAND))

