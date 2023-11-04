
```markdown
# Pizzeria Project

This project is a web-based application for managing a pizza orders, allowing customers to place orders for customized pizzas and tracking the status of their orders.

## Features

- Order pizza with customizable options for base, cheese, and toppings.
- Real-time tracking of order status.
- Asynchronous task management using Celery.
- Docker containerization for easy deployment.
```
## Installation

1. Clone the repository to your local machine.
   ```bash
   git clone https://github.com/your-username/pizzeriaApi.git
   ```

2. Navigate to the project directory.
   ```bash
   cd pizzeria_project
   ```

3. Keep Docker app open so docker can pick the docker commands

## Usage

1. Start the Docker containers.
   ```bash
   docker-compose up
   ```

2. Access the application at [http://localhost:8000](http://localhost:8000).
3. For Creating an order [http://localhost:8000/create_order](http://localhost:8000/create_order).
   here add the order in json format pizzas can have multiple entries in single order
   ```json
   {
    "pizzas": [
        {
            "base": "thin-crust",
            "cheese": "mozzarella",
            "topping1": "pepperoni",
            "topping2": "mushrooms",
            "topping3": "onions",
            "topping4": "sausage",
            "topping5": "bacon"
        },
        {
            "base": "normal",
            "cheese": "cheddar",
            "topping1": "olives",
            "topping2": "bell peppers",
            "topping3": "mushrooms",
            "topping4": "sausage",
            "topping5": "bacon"
        }
    ]
   }
   ```
Choises of base, cheese and toppings are specific and case sencitive

    base_choices = 'thin-crust', 'normal', 'cheese-burst'
    cheese_choices = 'mozzarella', 'cheddar', 'parmesan', 'provolone'
    topping_choices = 'pepperoni', 'mushrooms', 'onions', 'sausage', 'bacon', 'olives', 'bell peppers'
    
create_order on successfully placing an order will give following response with corresponding order_id
   ```json
   {
       "message": "Order placed successfully!",
       "order_id": 36
   }
   ```
4. For Tracking an order [http://localhost:8000/track_order/order_id/](http://localhost:8000/track_order/order_id/)  Place an integer order_id you got as a response of creating an order.
   status will change like this
   ```bash
   Placed--->10sec gap--->Accepted--->50sec gap--->Preparing--->120sec gap--->Dispatched--->120sec gap--->Delivered
   ```

## Technologies Used

- Django
- Django REST Framework
- Celery
- Redis
- Docker



