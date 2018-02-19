#!/usr/bin/python
import shlex
import subprocess
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","root","palaniM@67","lab_log" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

sql = "SELECT * FROM log_history"
# Execute the SQL command
cursor.execute(sql)
# Fetch all the rows in a list of lists.
results = cursor.fetchall()
for row in results:
  flag = 0;
  fname = row[0]
  lname = row[1]
  age = row[2]
  # Now print fetched result
  # print (fname,lname,age)
  cmd=shlex.split("ping -c1 "+age)
  print(cmd)
  try:
   output = subprocess.check_output(cmd)
  except subprocess.CalledProcessError,e:
  	#print "The IP {0} is NotReacahble".format(cmd[-1])
  	flag = 0;
  else:
  	flag = 1;
  	# print "The IP {0} is Reachable".format(cmd[-1])
  if flag == 1:
  	print(age)
  else:
  	print "nothing"


# disconnect from server
db.close()