[![Build Status](https://travis-ci.org/r0fls/commander.png)](https://travis-ci.org/r0fls/commander)
# commander

This is an ansible inspired project. It currently allows running BASH commands on a list of hosts.

Create a configuration file in the following format:

`hosts;commands`

For example, if this is in a file called `config.txt`:

    localhost, user@otherhost; echo Hello World,pwd
    localhost; ps aux | grep grep

Then you can call `python parse.py config.txt` and it will run the specified commands on the list of hosts.

You will need SSH keys to be configured for all machines.
