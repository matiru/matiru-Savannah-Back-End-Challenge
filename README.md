# matiru-Savannah-Back-End-Challenge


## Description
This project is a simple Flask application that manages customers and orders, featuring:
- Customer details (name and code)
- Order details (item, amount, time)
- SMS notifications using Africa's Talking when an order is placed
- pending is implementing authentication and authorization via OpenID Connect
## Requirements
- Python 3.x
- Flask
- Flask-SQLAlchemy
- Africa's Talking SDK
- Python Dotenv



## Installation
1. Clone the repository:
   ```bash
   git clone <repository_url>
   
2. Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the requirements:
   pip install -r requirements.txt

4. Create a .env file with your sensitive data (API keys, database URL, etc.)

5. Running the application : flask run

## API Endpoints
POST /customers: Add a new customer.
{
  "name": "John Doe",
  "code": "+25470000000"
}

POST /orders: Place a new order and send an SMS to the customer.

{
  "item": "Product A",
  "amount": 100,
  "time": "2024-09-24 10:00:00",
  "customer_id": 1
}

GET /customers: Retrieve all customers.
GET /orders: Retrieve all orders.

   
