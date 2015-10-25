import subprocess

def run(host,command):
    ssh = subprocess.Popen(["ssh", "%s" % host, command],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
    result = ssh.stdout.readlines()
    return result

if __name__=="__main__":
     HOST="localhost"
     COMMAND="uname -a"
     print run(HOST,COMMAND)

