#sending mail using python 
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("chandanfitjee@gmail.com", "07041998")
 
msg = "hello buddy whatsup"
server.sendmail("chandanfitjee@gmail.com", "chandan.17ec@cmr.edu.in", msg)
server.quit()
