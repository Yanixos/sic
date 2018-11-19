import smtplib, base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

 
def ScanReport() :

	try :
	
		fromaddr = "super.integrity.checker@gmail.com"
		enc_mail = open('/usr/share/sic/.email','r').readline()
		enc_mail = enc_mail.strip("\n")
		rot13 = enc_mail.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		enc_mail = enc_mail.translate(rot13)
		mail = base64.b64decode(enc_mail).decode('utf-8')
		toaddr = mail.strip("\n")
		 
		msg = MIMEMultipart()
		 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Super Integrity Checker : Scan Report."
		 
		body = "Hello sir,\n\nWe are pleased to keep you updated with the file scans.\nPlease check the log file we have sent you.\nGreatings from Super Integrity Checker !\n\n#Your integrity is our goal\n"
		 
		msg.attach(MIMEText(body, 'plain'))
		 
		filename = "/var/log/sic.log"
		attachment = open("/var/log/sic.log", "rb")
		 
		part = MIMEBase('application', 'octet-stream')
		part.set_payload((attachment).read())
		encoders.encode_base64(part)
		part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
		 
		msg.attach(part)
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		secret = "H3IjMKWNEzywPt=="
		rot13 = secret.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		secret = secret.translate(rot13)
		pwd = base64.b64decode(secret).decode('utf-8')
		server.login(fromaddr,pwd)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		
	except Exception as e :
		 print("[!] Couldn't send the scan report mail : ",e)
		 

def UpdateAlert() :

	try :
		fromaddr = "super.integrity.checker@gmail.com"
		enc_mail = open('/usr/share/sic/.email','r').readline()
		enc_mail = enc_mail.strip("\n")
		rot13 = enc_mail.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		enc_mail = enc_mail.translate(rot13)
		mail = base64.b64decode(enc_mail).decode('utf-8')
		toaddr = mail.strip("\n")
		 
		msg = MIMEMultipart()
		 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Super Integrity Checker : Update Alert !"
		 
		body = "Hello sir,\n\nWe inform you that your baseline database has been updated.\nIf you are not aware of that, your files may be under attack, we recommend you to find the last time your files where safe from /var/log/sic.history and do a system restoration using that date\n\n\#Your integrity is our goal\n"
		 
		msg.attach(MIMEText(body, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		secret = "H3IjMKWNEzywPt=="
		rot13 = secret.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		secret = secret.translate(rot13)
		pwd = base64.b64decode(secret).decode('utf-8')
		server.login(fromaddr,pwd)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
		
	except Exception as e :
		print("[!] Couldn't send the update alert mail : ",e)
	
if __name__ == "__main__":

	try :

		fromaddr = "super.integrity.checker@gmail.com"
		enc_mail = open('/usr/share/sic/.email','r').readline()
		enc_mail = enc_mail.strip("\n")
		rot13 = enc_mail.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		enc_mail = enc_mail.translate(rot13)
		mail = base64.b64decode(enc_mail).decode('utf-8')
		toaddr = mail.strip("\n")
		 
		msg = MIMEMultipart()
		 
		msg['From'] = fromaddr
		msg['To'] = toaddr
		msg['Subject'] = "Super Integrity Checker : Welcome !"
		 
		body = "Hello sir,\n\nWe have the pleasure to inform you that SuperIntegrityChecker is well installed on your machine\nWe will do our best to keep your 'files, directories, services and your digital life' safe.\n- After every scan you will receive the report here and in the /etc/var/sic.log file in your machine\n- Everytime your database is updated you will receive an alert message, for security reasons.\n\n#Your integrity is our goal\n"
		 
		msg.attach(MIMEText(body, 'plain'))
		 
		server = smtplib.SMTP('smtp.gmail.com', 587)
		server.starttls()
		secret = "H3IjMKWNEzywPt=="
		rot13 = secret.maketrans("ABCDEFGHIJKLMabcdefghijklmNOPQRSTUVWXYZnopqrstuvwxyz","NOPQRSTUVWXYZnopqrstuvwxyzABCDEFGHIJKLMabcdefghijklm")
		secret = secret.translate(rot13)
		pwd = base64.b64decode(secret).decode('utf-8')
		server.login(fromaddr,pwd)
		text = msg.as_string()
		server.sendmail(fromaddr, toaddr, text)
		server.quit()
	except Exception as e :
		print("[!] Couldn't send the welcome mail : ",e)
	
	
########################################################################
