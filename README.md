Restaurant Review System using SQLAlchemy
Table of Contents

    Introduction
    Project Overview
    Getting Started
    Project Structure
    Usage Examples
    Contributing
    License

Introduction

This project demonstrates a simple restaurant review system built using SQLAlchemy, a powerful Object-Relational Mapping (ORM) library for Python. The system allows you to model restaurants, customers, and their reviews. You can perform various operations such as adding reviews, finding the fanciest restaurant, and more.
Project Overview

The project consists of the following components:

    main.py: This is the main script where you can interact with the restaurant review system.
    models.py: Contains SQLAlchemy model definitions for Restaurant, Customer, and Review.
    restaurants.db: The SQLite database file where data is stored.

Getting Started

To get started with this project, follow these steps:

    Clone the repository to your local machine:

    bash

git clone <repository-url>

Install the required dependencies:

bash

pip install sqlalchemy

Run the main.py script to interact with the restaurant review system:

bash

    python main.py

Project Structure

The project structure is as follows:

diff

- main.py
- models.py
- restaurants.db
- README.md

Usage Examples

Here are some usage examples of the restaurant review system:

    Adding a New Restaurant and Customer:

    python

restaurant1 = Restaurant(name='Restaurant 1', price=3)
customer1 = Customer(full_name='John Doe')
session.add_all([restaurant1, customer1])
session.commit()

Adding a Review:

python

review1 = Review(star_rating=4, restaurant=restaurant1, customer=customer1)
session.add(review1)
session.commit()

Finding the Fanciest Restaurant:

python

fancy_restaurant = restaurant1.fanciest()
print(f'The fanciest restaurant is: {fancy_restaurant.name}')

Getting All Reviews for a Restaurant:

python

all_reviews = restaurant1.all_reviews()
print('All reviews for Restaurant 1:')
print(all_reviews)

Finding a Customer's Favorite Restaurant:

python

favorite = customer1.favorite_restaurant()
print(f"{customer1.full_name}'s favorite restaurant is: {favorite.name}")

Deleting Reviews for a Restaurant by a Customer:

python

    customer1.delete_reviews(restaurant1)
    session.commit()
    print(f"Reviews for {customer1.full_name} at {restaurant1.name} have been deleted.")

Contributing

Contributions to this project are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.
License

This project is licensed under the MIT License - see the LICENSE file for details.
