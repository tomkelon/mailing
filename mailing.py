import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase 
from email import encoders 
import threading
                                     
                                                       
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\li1.txt', 'r', encoding="utf8") as f:
     li1 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\li2.txt', 'r', encoding="utf8") as f:
     li2 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\li3.txt', 'r', encoding="utf8") as f:
     li3 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\li4.txt', 'r', encoding="utf8") as f:
     li4 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\li5.txt', 'r', encoding="utf8") as f:
     li5 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\name1.txt', 'r', encoding="utf8") as f:
     name1 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\name2.txt', 'r', encoding="utf8") as f:
     name2 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\name3.txt', 'r', encoding="utf8") as f:
     name3 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\name4.txt', 'r', encoding="utf8") as f:
     name4 = [s.strip() for s in f.readlines()]
with open('C:\\Users\\Tomk Vu\\Desktop\\Gmail Marketing\\name5.txt', 'r', encoding="utf8") as f:
     name5 = [s.strip() for s in f.readlines()] 
   

def acc1 (li, name):
     length = len(li)
     for i in range(length):
          X = li[i]
          reciver_mail = X
          Y = name[i]
          sender_address = "a"
          sender_pass = "a"
          fName = Y
          message = MIMEMultipart()
          message['From'] = "Vũ Nhật Vượng"
          message['To'] =  reciver_mail             
          message['Subject'] =  f"""Xin chào {fName}"""
          message['Reply-To']  = 'a.gdt@gmail.com'    
     
          mail_content = f"""
          Xin chào {fName}. Tôi là Vũ Nhật Vượng
          """

    
          message.attach(MIMEText(mail_content))

          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls() 
          s.login(sender_address, sender_pass) 
          text = message.as_string()
          s.sendmail(sender_address, reciver_mail, text)
          s.quit()
           
          print("Acc 1 đã gửi tới: " + reciver_mail)
def acc2 (li, name):
     length = len(li)
     for i in range(length):
          X = li[i]
          reciver_mail = X
          Y = name[i]
          sender_address = "a"
          sender_pass = "a"
          fName = Y
          message = MIMEMultipart()
          message['From'] = "Vũ Nhật Vượng"
          message['To'] =  reciver_mail             
          message['Subject'] =  f"""Xin chào {fName}"""
          message['Reply-To']  = 'a.gdt@gmail.com'    
     
          mail_content = f"""
          Xin chào {fName}. Tôi là Vũ Nhật Vượng
          """

    
          message.attach(MIMEText(mail_content))


          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls() 
          s.login(sender_address, sender_pass) 
          text = message.as_string()
          s.sendmail(sender_address, reciver_mail, text)
          print("Acc 2 đã gửi tới: " + reciver_mail) 

def acc3 (li, name):
     length = len(li)
     for i in range(length):
          X = li[i]
          reciver_mail = X
          Y = name[i]
          sender_address = "a"
          sender_pass = "a"
          fName = Y
          message = MIMEMultipart()
          message['From'] = "Vũ Nhật Vượng"
          message['To'] =  reciver_mail             
          message['Subject'] =  f"""Xin chào {fName}"""
          message['Reply-To']  = 'a.gdt@gmail.com'    
     
          mail_content = f"""
          Xin chào {fName}. Tôi là Vũ Nhật Vượng
          """

    
          message.attach(MIMEText(mail_content))


          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls() 
          s.login(sender_address, sender_pass) 
          text = message.as_string()
          s.sendmail(sender_address, reciver_mail, text)
          print("Acc 3 đã gửi tới: " + reciver_mail)  

def acc4 (li, name):
     length = len(li)
     for i in range(length):
          X = li[i]
          reciver_mail = X
          Y = name[i]
          sender_address = "a"
          sender_pass = "a"
          fName = Y
          message = MIMEMultipart()
          message['From'] = "Vũ Nhật Vượng"
          message['To'] =  reciver_mail             
          message['Subject'] =  f"""Xin chào {fName}"""
          message['Reply-To']  = 'a.gdt@gmail.com'    
     
          mail_content = f"""
          Xin chào {fName}. Tôi là Vũ Nhật Vượng!
          """

    
          message.attach(MIMEText(mail_content))


          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls() 
          s.login(sender_address, sender_pass) 
          text = message.as_string()
          s.sendmail(sender_address, reciver_mail, text)
          print("Acc 4 đã gửi tới: " + reciver_mail)  


def acc5 (li, name):
     length = len(li)
     for i in range(length):
          X = li[i]
          reciver_mail = X
          Y = name[i]
          sender_address = "a@gmail.com"
          sender_pass = "a"
          fName = Y
          message = MIMEMultipart()
          message['From'] = "Vũ Nhật Vượng"
          message['To'] =  reciver_mail             
          message['Subject'] =  f"""Xin chào {fName}"""
          message['Reply-To']  = 'a.gdt@gmail.com'    
     
          mail_content = f"""
          Xin chào {fName}. Tôi là Vũ Nhật Vượng
          """

    
          message.attach(MIMEText(mail_content))


          s = smtplib.SMTP('smtp.gmail.com', 587) 
          s.starttls() 
          s.login(sender_address, sender_pass) 
          text = message.as_string()
          s.sendmail(sender_address, reciver_mail, text) 
          print("Acc 5 đã gửi tới: " + reciver_mail) 
thread1 = threading.Thread(target=acc1, args=(li1,name1))
thread2 = threading.Thread(target=acc2, args=(li2,name2))
thread3 = threading.Thread(target=acc3, args=(li3,name3))
thread4 = threading.Thread(target=acc4, args=(li4,name4))
thread5 = threading.Thread(target=acc5, args=(li5,name5))

thread1.start()
thread2.start()
# thread3.start()
# thread4.start()
# thread5.start()
