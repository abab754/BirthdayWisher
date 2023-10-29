import smtplib
import datetime as dt
import random
import pandas

MY_MAIL = ""
PASSWORD = ""
RECIPIENT = ""

my_mail = MY_MAIL
password = PASSWORD
recipient = RECIPIENT
# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv
data = pandas.read_csv("birthdays.csv")
today = (dt.datetime.now().month, dt.datetime.now().day)

birthday_dic = {(data_row.month, data_row.day): data_row for (index, data_row) in data.iterrows()}

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if today in birthday_dic:
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    birthday_person = birthday_dic[today]
    with open(file_path, "r") as letter_file:
        txt = letter_file.read()
        txt = txt.replace("[NAME]", birthday_person["name"])

        print(txt)


# 4. Send the letter generated in step 3 to that person's email address.
with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=my_mail, password=password)
    connection.sendmail(from_addr=my_mail, to_addrs= birthday_person["email"], msg=f"Subject: Happy Birthday\n\n{txt}")



