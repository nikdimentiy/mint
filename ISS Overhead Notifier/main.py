import requests  # Library for HTTP requests
from datetime import datetime  # Module for date and time handling
import smtplib  # Library for sending emails
import time  # Library for time-related operations

# Constants for your email credentials and location coordinates
MY_EMAIL = "nikdimentiy@yahoo.com"  # Change this to your email
MY_PASSWORD = "12345f"  # Change this to your email password
MY_LAT = 51.507351  # Latitude of your location
MY_LONG = -0.127758  # Longitude of your location

# Function to check if the ISS is overhead (within 5 degrees of latitude and longitude)
def is_iss_overhead():
    """
    Determines whether the International Space Station (ISS) is overhead,
    within a 5-degree range of latitude and longitude from your location.
    """
    # Get the current ISS position from the Open Notify API
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()  # Raise an exception if the request failed
    data = response.json()  # Parse the JSON response

    # Extract the ISS latitude and longitude
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # Check if the ISS is within 5 degrees of the specified latitude and longitude
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    return False

# Function to check if it's night at your location
def is_night():
    """
    Determines whether it's currently night at your location.
    Uses the Sunrise-Sunset API to get sunrise and sunset times.
    """
    # Parameters for the Sunrise-Sunset API
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,  # 0 means times are returned in UTC
    }
    # Make the request to get the sunrise and sunset times
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()  # Raise an exception if the request failed
    data = response.json()  # Parse the JSON response
    
    # Extract the sunrise and sunset times and convert to hours (UTC)
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # Get the current hour in UTC
    time_now = datetime.utcnow().hour

    # Return True if it's currently night
    return time_now >= sunset or time_now <= sunrise

# Main loop to check every minute if the ISS is overhead and it's night
while True:
    # Pause for 60 seconds before checking again
    time.sleep(60)
    
    # If the ISS is overhead and it's night, send an email alert
    if is_iss_overhead() and is_night():
        # Establish a connection to the SMTP server (Yahoo in this case)
        connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)  # Specify port 587 for TLS
        connection.starttls()  # Start TLS (Transport Layer Security)
        connection.login(MY_EMAIL, MY_PASSWORD)  # Login with your email and password
        
        # Send an email to yourself with a notification
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky."
        )
        
        # Close the connection to the SMTP server
        connection.quit()
