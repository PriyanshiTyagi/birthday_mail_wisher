##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import datetime as dt
import pandas
import random
import smtplib
import os
from dotenv import load_dotenv

load_dotenv()


my_email = os.getenv("GMAIL")
password = os.getenv("GMAIL_PASS")

today=dt.datetime.now()
month=today.month
day=today.day

data=pandas.read_csv("birthdays.csv")
if day in list(data.day) and month in list(data.month):
    person=data[data.day==day]

    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter=file.read()
        new_letter=letter.replace("[NAME]",*person.name)
        print(new_letter)

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=person.email,
            msg=f"Subject:Wishing You Happy Birthday\n\n{new_letter}"

        )


