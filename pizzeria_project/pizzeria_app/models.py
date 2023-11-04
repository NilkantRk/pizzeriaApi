from django.db import models

class Pizza(models.Model):
    base_choices = (
        ('thin-crust', 'Thin Crust'),
        ('normal', 'Normal'),
        ('cheese-burst', 'Cheese Burst')
    )
    cheese_choices = (
        ('mozzarella', 'Mozzarella'),
        ('cheddar', 'Cheddar'),
        ('parmesan', 'Parmesan'),
        ('provolone', 'Provolone')
    )
    topping_choices = (
        ('pepperoni', 'Pepperoni'),
        ('mushrooms', 'Mushrooms'),
        ('onions', 'Onions'),
        ('sausage', 'Sausage'),
        ('bacon', 'Bacon'),
        ('olives', 'Olives'),
        ('bell peppers', 'Bell Peppers')
    )

    base = models.CharField(max_length=20, choices=base_choices)
    cheese = models.CharField(max_length=20, choices=cheese_choices)
    topping1 = models.CharField(max_length=20, choices=topping_choices)
    topping2 = models.CharField(max_length=20, choices=topping_choices)
    topping3 = models.CharField(max_length=20, choices=topping_choices)
    topping4 = models.CharField(max_length=20, choices=topping_choices)
    topping5 = models.CharField(max_length=20, choices=topping_choices)

    def __str__(self):
        return f"{self.base} Pizza with {self.cheese} and toppings: {self.topping1}, {self.topping2}, {self.topping3}, {self.topping4}, {self.topping5}"


# Pizza will be stored in Order 


class Order(models.Model):
    pizzas = models.ManyToManyField(Pizza)
    status = models.CharField(max_length=20, default='Placed')

    def __str__(self):
        return f"Order {self.id} - {self.status}"
