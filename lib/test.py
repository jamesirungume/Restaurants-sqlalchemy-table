from sqlalchemy.orm import sessionmaker
from models import Restaurant, Customer, engine

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Create instances of Restaurant and Customer
restaurant1 = Restaurant(name="Restaurant 1")
restaurant2 = Restaurant(name="Restaurant 2")
customer1 = Customer(full_name="Customer 1")
customer2 = Customer(full_name="Customer 2")

# Add the instances to the session
session.add(restaurant1)
session.add(restaurant2)
session.add(customer1)
session.add(customer2)

# Establish the relationship using the association table
restaurant1.customers.append(customer1)
restaurant2.customers.append(customer2)

# Commit the changes to the database
session.commit()

# Now you can access the related data
restaurants = session.query(Restaurant).all()

for restaurant in restaurants:
    customers = restaurant.customers
    print(f"Restaurant: {restaurant.name}")
    
    for customer in customers:
        print(f"Customer: {customer.full_name}")

# Close the session
session.close()
