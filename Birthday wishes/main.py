# Import necessary libraries
from datetime import datetime
import pandas
import random
import smtplib

# Define your email credentials
MY_EMAIL = "YOUR EMAIL"  # Replace with your email address
MY_PASSWORD = "YOUR PASSWORD"  # Replace with your email password

# Get today's date
today = datetime.now()
today_tuple = (today.month, today.day)

# Read birthday data from a CSV file
data = pandas.read_csv("birthdays.csv")

# Create a dictionary of birthdays using a tuple (month, day) as the key
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# Check if there's a birthday today
if today_tuple in birthdays_dict:
    # Retrieve the information of the birthday person
    birthday_person = birthdays_dict[today_tuple]

    # Select a random letter template and replace placeholders
    file_path = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Connect to the SMTP server of your email provider
    with smtplib.SMTP("YOUR EMAIL PROVIDER SMTP SERVER ADDRESS") as connection:
        # Start a secure connection
        connection.starttls()

        # Log in to your email account
        connection.login(MY_EMAIL, MY_PASSWORD)

        # Send a birthday email to the recipient
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
