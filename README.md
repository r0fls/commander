[![Build Status](https://travis-ci.org/r0fls/commander.png)](https://travis-ci.org/r0fls/commander)
# commander

This is an ansible inspired project. It currently allows running BASH commands on a list of hosts.

Create a configuration file in the following format:

`hosts;commands`

For example:

`localhost,otherhost,blah;echo Hello World,pwd
localhost;ps aux | grep grep`

Then you can call `parse.py config.txt` and it will run them.
