# Generated by Django 4.2.6 on 2023-10-31 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base', models.CharField(choices=[('thin-crust', 'Thin Crust'), ('normal', 'Normal'), ('cheese-burst', 'Cheese Burst')], max_length=20)),
                ('cheese', models.CharField(choices=[('mozzarella', 'Mozzarella'), ('cheddar', 'Cheddar'), ('parmesan', 'Parmesan'), ('provolone', 'Provolone')], max_length=20)),
                ('topping1', models.CharField(choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('olives', 'Olives'), ('bell peppers', 'Bell Peppers')], max_length=20)),
                ('topping2', models.CharField(choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('olives', 'Olives'), ('bell peppers', 'Bell Peppers')], max_length=20)),
                ('topping3', models.CharField(choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('olives', 'Olives'), ('bell peppers', 'Bell Peppers')], max_length=20)),
                ('topping4', models.CharField(choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('olives', 'Olives'), ('bell peppers', 'Bell Peppers')], max_length=20)),
                ('topping5', models.CharField(choices=[('pepperoni', 'Pepperoni'), ('mushrooms', 'Mushrooms'), ('onions', 'Onions'), ('sausage', 'Sausage'), ('bacon', 'Bacon'), ('olives', 'Olives'), ('bell peppers', 'Bell Peppers')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(default='Placed', max_length=20)),
                ('pizzas', models.ManyToManyField(to='pizzeria_app.pizza')),
            ],
        ),
    ]