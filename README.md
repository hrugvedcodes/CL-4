after cloudera opens:
run cloudera express, run that command in terminal, link appears, follow link. 
link opens: login, try starting hdfs,yarn.

in terminal: sudo -u hdfs hdfs dfsadmin -report (user previleges error solved)

now we can see like this: live datanodes(1)
just see the hdfs contents : sudo -u hdfs hdfs dfs -ls /
just try to make directory : sudo -u hdfs hdfs dfs -mkdir /test

create shared folder, reboot system
upload to shared_vb file you want to put in hdfs

to see the files : ls /media/
here we can see the sf_SHARED_VB folder but cannot seet he inside contents
it says permission denied

then run : sudo usermod -aG vboxsf cloudera
then reboot sudo reboot
then we can see contents of the inside sf_SHARED_VB

now bring the files mapper and reducer from shared_vb to home directory

cp /media/sf_SHARED_VB/mapper.py ~/
also for reducer

now we have all 3 files in home directory
make directory in hdfs
sudo -u hdfs dfs -mkdir -p /user/cloudera1/input
this cannot make directory namenode is in safe mode

run : sudo -u hdfs hdfs dfsadmin -safemode leave




