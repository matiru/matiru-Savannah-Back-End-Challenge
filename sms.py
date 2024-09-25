# sms.py
import africastalking
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

username = os.getenv('AFRICAS_TALKING_USERNAME')  # e.g. 'sandbox'
api_key = os.getenv('AFRICAS_TALKING_API_KEY')  # Your API key

africastalking.initialize(username, api_key)
sms = africastalking.SMS

def send_sms(to, message):
    try:
        response = sms.send(message, [to])
        print(f"SMS sent: {response}")
        return response
    except Exception as e:
        print(f"Failed to send SMS: {e}")
