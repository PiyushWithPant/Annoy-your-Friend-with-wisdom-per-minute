# Importing required libraries
import random
import time
import datetime as dt
import smtplib
import os
from dotenv import load_dotenv

#! YOU CAN HOST THIS PROGRAM ON "PYTHONANYWHERE.COM" TO RUN IT ON CLOUD AND SEND UNLIMITED MAILS 

# run dotenv function to load the envs
load_dotenv()


# List to store the quotes
quotes = []

# Email and password
myEmail = "YOUR EMAIL COMES HERE"
password= os.getenv('password') # the password comes from the ENV file so add yours too

    
with open("quotes.txt", "r") as q:

        # now we need to make it a list
        for line in q.readlines():

            quotes.append(line)
 
 
wannaAnnoy = True  

mailsSent = 0
 
while wannaAnnoy:
    
    time.sleep(1) # waiting for 1 second so that while loop doesn't overload every ms
    
    now = dt.datetime.now()
    
    if(now.second == 10 or now.second == 30 or now.second == 50):   
    
    # usually it takes around 5 or 6 second to send an email so you can change your code as per it
    # therefore it should send around 3 mails per minute
    
        with smtplib.SMTP("smtp.gmail.com", 587, timeout=120) as con:
            
            # securing
            con.starttls()

            # login
            con.login(myEmail, password)

            # getting our random quote
            quote = random.choice(quotes)

            # sending mail
            con.sendmail(
                from_addr = myEmail,
                to_addrs = "email of your friend comes here",
                msg = f"Subject: Add your subject here\n\n{quote}\n\nBy Piyush Pant"
            )
            
            mailsSent += 1
            print(f"Email successfully sent! Annoy count reached: {mailsSent}")
        
    else:
        print(f"seconds: {now.second}")



