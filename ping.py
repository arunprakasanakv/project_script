#!/usr/bin/python
import shlex
import subprocess

# Tokenize the shell command
# cmd will contain  ["ping","-c 1","google.com"]     
cmd=shlex.split("ping -c1 8.8.8.8")
try:
   output = subprocess.check_output(cmd)
except subprocess.CalledProcessError,e:
   print "The IP {0} is NotReacahble".format(cmd[-1])
else:
   print "The IP {0} is Reachable".format(cmd[-1])