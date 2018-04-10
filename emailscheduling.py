#email schedulimg
import smtplib
s=smtplib.SMTP("smtp.gmail.com",587)
s.starttls()
s.login("sumaiyachachiya65@gmail.com","saifali123")
msg="hi how are you"
s.sendmail("sumaiyachachiya65@gmail.com","brunda045@gmail.com","msg")
s.quit()
