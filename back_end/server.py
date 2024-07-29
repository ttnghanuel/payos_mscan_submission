import json
import os
import random

from payos import PaymentData as PayOSPaymentData, PayOS
from flask import Flask, jsonify

# Load environment variables
from dotenv import load_dotenv
load_dotenv()

# Initialize PayOS
payOS = PayOS(
    client_id=os.environ.get('PAYOS_CLIENT_ID'),
    api_key=os.environ.get('PAYOS_API_KEY'),
    checksum_key=os.environ.get('PAYOS_CHECKSUM_KEY')
)

# Initialize Flask app
app = Flask(__name__, static_folder='public', static_url_path='', template_folder='public')


@app.route('/create_payment_link', methods=['POST'])
def create_payment():
    print("Received a request for /create_payment_link")  # Debug log
    domain = "https://mscan.atwebpages.com"
    try:
        # Create a payment data object
        payment_data = PayOSPaymentData(
            orderCode=random.randint(1000, 9999),
            amount=200000,
            description='demo',
            cancelUrl=f"{domain}/cancel.html",
            returnUrl=f"{domain}/success.html"
        )
        print(f"Payment data created: {payment_data}")  # Debug log

        # Create the payment link
        payos_create_payment = payOS.createPaymentLink(payment_data)
        print(f"Payment link created: {payos_create_payment.to_json()}")  # Debug log
        
        return jsonify(payos_create_payment.to_json())
    except Exception as e:
        print(f"Error occurred: {str(e)}")  # Debug log
        return jsonify(error=str(e)), 403

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4242)
