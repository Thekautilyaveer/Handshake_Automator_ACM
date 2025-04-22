#importing various modules
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.options import Options
import time
import datetime
import smtplib
from email.mime.text import MIMEText



datee = datetime.date.today()


#setting up borwswer window and opening
options = Options()
options.add_argument("--inprivate")
options.add_argument("--headless")
driver = webdriver.Edge(options = options)
driver.get("https://webauth.usf.edu/login?service=https%3A%2F%2Fusf.joinhandshake.com%2Fauth%2Fcas%2F72%2Fsession")


time.sleep(5)

#fetching email from text file
with open ("email.txt", "r") as file:
    email = file.read()
#finding email textbox and writing the email
driver.find_element(By.ID, "i0116").send_keys(email)
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(5)
#fetching password from the text file
with open("password.txt", "r") as file:
    password = file.read()
#finding password textbox and writing the password 
driver.find_element(By.ID, "i0118").send_keys(password)
driver.find_element(By.ID, "idSIButton9").click()

time.sleep(4)


#Verification on Outlook
code_ = driver.find_element(By.CLASS_NAME, "display-sign-container")
print(code_.text)
time.sleep(10)
ele = driver.find_element(By.ID, "idSIButton9")
ele.click()
time.sleep(5)


#Apply filters
driver.get("https://usf.joinhandshake.com/stu/postings?page=1&per_page=25&sort_direction=desc&sort_column=created_at&query=cyber%20security%20intern")
time.sleep(5)





#Locate elements
ele2 = driver.find_elements(By.CLASS_NAME, "style__card___LCqKH")
str = ""
for i in ele2:
    # print(i.text)
    # print("\n")
    str += (i.text)
    str += ("\n")
    str += ("\n")
    str += ("\n")
# print("String below")
# print(str)


#Writing in jobs.txt file
try:
    with open("jobs.txt", "r") as file1:
        dat = file1.read()
        if dat != str:
            with open("jobs.txt", "w") as file2:
                file2.write(str)
        else:
            print("Data already fetched")
            str = "No updates"
except:
    with open("jobs.txt", "w") as file3:
        file3.write(str)
driver.close()


time.sleep(5)


#send email

sender_email = "'''Enter your email here'''"
with open("email_sender_password.txt", "r") as file2:
    password = file2.read()
with open("email_ist.txt", "r") as file:
    data = file.read()
    for i in data.split("\n"):
        receiver_email = i.strip()
        if not receiver_email:
                continue
        smtp_server = "smtp.gmail.com" 
        smtp_port = 587 
        body = str
        message = MIMEText(body)
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = "HANDSHAKE UPDATES"
        try:
            with smtplib.SMTP(smtp_server, smtp_port) as server:
                server.starttls()  #Secure the connection
                server.login(sender_email, password) 
                server.sendmail(sender_email, receiver_email, message.as_string()) 
                print("Email sent successfully!")
        except Exception as e:
            print(f"Error: {e}")


