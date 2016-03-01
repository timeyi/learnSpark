'''
The following are SSH command lines

get data:
wget http://en.wikipedia.org/wiki/Hortonworks

copy the data to HDFS
hadoop fs -put ~/Hortonworks /user/guest/Hortonworks

problem: 
put: Permission denied: user=root, access=WRITE, inode=”/user/guest/Hortonworks._COPYING_”:guest:guest:drwxr-xr-x
solution: 
[root@sandbox ~]# su hdfs
[hdfs@sandbox root]$ hadoop fs -chmod -R 777 /user/guest
[hdfs@sandbox root]$ exit
[root@sandbox ~]# hadoop fs -put ~/Hortonworks /user/guest/Hortonworks
[root@sandbox ~]# hadoop fs -ls /user/guest/
Found 1 items
-rw-r–r– 3 root guest 53068 2015-11-20 03:01 /user/guest/Hortonworks
[root@sandbox ~]#

start the PySpark shell:
pyspark
'''

#instantiate RDD 
#sc: spark context
myLines = sc.textFile('hdfs://sandbox.hortonworks.com/user/guest/Hortonworks')

#filter out empty lines
filtered_myLines = myLines.filter(lambda x: len(x) > 0)

#take action on the data
filtered_myLines.count()
