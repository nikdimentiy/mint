import smtplib
import datetime as dt
import random

# Set your email credentials
MY_EMAIL = "test@gmail.com"
MY_PASSWORD = "12345"

def send_motivational_email():
    # Get the current date and weekday
    now = dt.datetime.now()
    weekday = now.weekday()
    
    # Check if today is Monday (weekday 0 is Monday)
    if weekday == 0:
        # Read motivational quotes from a text file
        with open("quotes.txt") as quote_file:
            all_quotes = quote_file.readlines()
            quote = random.choice(all_quotes)

        # Print the selected quote
        print(quote)
        
        # Connect to Gmail's SMTP server
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            
            # Send the Monday motivation email to yourself
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Monday Motivation\n\n{quote}")

if __name__ == "__main__":
    send_motivational_email()
