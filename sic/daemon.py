#!/usr/bin/python3.6
import sys, subprocess

fr = open('/var/log/auth.log','r')
content = fr.readlines()
last = content[-3]
if 'bin' in last :
	if 'echo' in last or 'chmod' in last or 'chown' in last or 'mv' in last or 'cp' in last or 'rm' in last :
		li = subprocess.getstatusoutput("sudo /usr/share/sic/sic -c -t SHORT >> /var/log/sic_realtime.log")
	else :
		sys.exit(0)
else :
	sys.exit(0)

			
		
	 
