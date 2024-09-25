import unittest
from app import create_app, db
from models import Customer, Order
from datetime import datetime

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()  # Create app using the factory function
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()  # Create the database for testing

    def tearDown(self):
        db.session.remove()
        db.drop_all()  # Clean up after each test
        self.app_context.pop()

    def test_create_customer_and_order(self):
        # Create a new customer
        customer = Customer(name="John Doe", code="+254794824614")
        db.session.add(customer)
        db.session.commit()
        
        # Create a new order for the customer
        order = Order(item="Product A", amount=100, time=str(datetime.now()), customer_id=customer.id)
        db.session.add(order)
        db.session.commit()

        # Assert that the customer and order were created
        self.assertEqual(Customer.query.count(), 1)
        self.assertEqual(Order.query.count(), 1)

if __name__ == '__main__':
    unittest.main()
