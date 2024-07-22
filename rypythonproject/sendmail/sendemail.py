import smtplib as s
smtpobj=s.SMTP('smpt.gmail.com',587)
smtpobj.ehlo() #EHLO stands for Extended HELLO. It is an SMTP command that the client uses to tell the server that it is an SMTP client.
smtpobj.starttls() #STARTTLS is an extension to the SMTP protocol that allows you to upgrade an insecure connection to a secure one using TLS or SSL.
#This is useful if you are sending sensitive information, such as passwords, over email.  
password=input("enter password")
smtpobj.login("ronakyadav9977@gmail.com",password)
listadd=["abc@gmail.com","xyz@gmail.com"]
subject=" sending email by using python"
body=" smtplib is used to send email .it is used to route emails between email servres  "
message="subject:{}\n\n{}".format(subject,body)
smtpobj.sendmail("ronakyadav9977@gmail.com",listadd,message)
print("send mail")
smtpobj.quit()  # to close server