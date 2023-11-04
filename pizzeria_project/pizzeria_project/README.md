# pizzeria_project
 create order and track order api

# Requirements
Django, Django-rest-framework, Python, redis, celery

# need to install  Redis application
```bash
pip install redis 
```
and 
```bash
pip install celery 
``` 

# Redis is a broker server 
Also you need to install Redis in your machine 
More details about redis [Redis](https://redis.io/)


# Run your broker server 
```bash
redis-server
```

# Next run your Django server
```bash
python manage.py runserver
``` 

# Next step run your Celery worker 
```bash
celery -A project_name worker -l info

```
you will get task list in your console 

# next run your scheduler 
```bash
celery -A project_name beat -l info
```
# To create order hit
```link
http://127.0.0.1:8000/create_order/
```
below is the order format
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
    ],
}
```
create superuser and see the created orders
# To track the order hit
```link
http://127.0.0.1:8000/track_order/11/
```
fill order id in-place of 11
