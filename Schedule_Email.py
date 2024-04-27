"""
To resolve the SMTPAuthenticationError and send emails using your Gmail account, follow these steps:
1. Go to your Google Account settings page: https://myaccount.google.com/.
2. In the "Security" section, find the "Signing in to Google" option and click on "App passwords" (or visit this link directly: https://myaccount.google.com/apppasswords).
3. You may need to enter your Google account password again for verification.
4. Under "Select app" choose "Mail" and under "Select device" choose "Other (Custom name)".
5. Enter a name for your application (e.g., "Python Script").
6. Click on "Generate" to generate the application-specific password.
7. Google will generate a unique sixteen-character password. Copy this password.
8. Use this generated password in your Python script instead of your regular Gmail password.
"""

import smtplib
import schedule
import time
from datetime import datetime

def send_email():
    # Email configurations
    sender_email = 'machinelearning33@gmail.com'
    sender_password = '*************' # For this password use the above instructions.
    receiver_email = 'anirudh.bayana@gmail.com'
    
    subject = 'Scheduled Email'
    body = 'This is a scheduled email sent from Python.'

    # Connect to SMTP server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    
    # Construct email message
    message = f'Subject: {subject}\n\n{body}'
    
    # Send email
    server.sendmail(sender_email, receiver_email, message)
    
    # Quit SMTP server
    server.quit()
    
    # Cancel the job after sending the email
    return schedule.CancelJob

def schedule_email():
    # Input date and time
    date_str = input("Enter the date in format (YYYY-MM-DD): ")
    time_str = input("Enter the time in format (HH:MM): ")
    datetime_str = f"{date_str} {time_str}"

    # Convert string to datetime object
    schedule_time = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M")

    # Schedule the email
    schedule.every().day.at(schedule_time.strftime("%H:%M")).do(send_email)

# Schedule the email based on user input
schedule_email()

# Loop to continuously check the schedule
while True:
    schedule.run_pending()
    time.sleep(60)  # Check every 60 seconds
