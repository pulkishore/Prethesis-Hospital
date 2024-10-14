
import pandas as pd
import pywhatkit as pw
from datetime import datetime, timedelta

# Read Excel data
df = pd.read_excel('appointments.xlsx')

# Loop through each row in the Excel file
for index, row in df.iterrows():
    patient_name = row['Patient Name']
    # Make sure the number includes the country code, e.g., '+91 9876543210'
    phone_number = row['Phone Number']
    # Convert appointment time to datetime
    appointment_time = pd.to_datetime(row['Appointment Time'])
    # Convert check-in time to datetime
    check_in_time = pd.to_datetime(row['Check-In Time'])    
    delay = row['Predicted Delay']  # Delay time in minutes

    # Current time + delay
    notification_time = datetime.now() + timedelta(minutes=delay)

    # Message body
    message = f"Hello {patient_name}, your appointment scheduled at {appointment_time.strftime('%H:%M')} is delayed by {delay} minutes. Thank you for your patience!"

    # Send message at notification_time
    # pywhatkit takes the hour and minute in 24-hour format for sending the message
    pw.sendwhatmsg(phone_number, message, notification_time.hour,
                   notification_time.minute)

    print(
        f"Message scheduled for {patient_name} at {notification_time.strftime('%H:%M')}")
    