# Generated by Django 2.0.3 on 2018-03-16 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddOn',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dish_id', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('meal_time', models.CharField(blank=True, max_length=3, null=True)),
                ('user_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'add_on',
            },
        ),
        migrations.CreateModel(
            name='Allergens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allergen_id', models.IntegerField()),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'allergens',
            },
        ),
        migrations.CreateModel(
            name='CalorieFormulae',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField()),
                ('num_bfst', models.IntegerField()),
                ('num_lunch', models.IntegerField()),
                ('num_snacks', models.IntegerField()),
                ('num_dinner', models.IntegerField()),
                ('code_bfst', models.IntegerField()),
                ('code_lunch', models.IntegerField()),
                ('code_snacks', models.IntegerField()),
                ('code_dinner', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'calorie_formulae',
            },
        ),
        migrations.CreateModel(
            name='CompletedOrders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('address', models.CharField(max_length=500)),
                ('price', models.IntegerField()),
                ('delivery_cost', models.IntegerField(blank=True, null=True)),
                ('dishes_delivered', models.CharField(max_length=500)),
                ('number_of_dishes', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'completed_orders',
            },
        ),
        migrations.CreateModel(
            name='Coupons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=32, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('terms_and_conditions', models.TextField(blank=True, null=True)),
                ('expiration_time', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'coupons',
            },
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('time_of_delivery', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=500)),
                ('geocode', models.CharField(max_length=500)),
                ('instructions', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'delivery_address',
            },
        ),
        migrations.CreateModel(
            name='DeliveryZones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pincode', models.CharField(blank=True, max_length=6, null=True)),
                ('kitchen_id', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'delivery_zones',
            },
        ),
        migrations.CreateModel(
            name='DietDish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'diet_dish',
            },
        ),
        migrations.CreateModel(
            name='DietPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diet_name', models.CharField(max_length=255)),
                ('goal', models.CharField(max_length=255)),
            ],
            options={
                'managed': False,
                'db_table': 'diet_plan',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=3)),
                ('meal_plan', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=2000, null=True)),
                ('calories', models.IntegerField(blank=True, null=True)),
                ('carbohydrates', models.IntegerField(blank=True, null=True)),
                ('fats', models.IntegerField(blank=True, null=True)),
                ('protein', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'dish',
            },
        ),
        migrations.CreateModel(
            name='DishAllergens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'dish_allergens',
            },
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(blank=True, null=True)),
                ('question', models.CharField(blank=True, max_length=1000, null=True)),
                ('answer', models.CharField(blank=True, max_length=1000, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'feedback',
            },
        ),
        migrations.CreateModel(
            name='Holidays',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'holidays',
            },
        ),
        migrations.CreateModel(
            name='MealPrefChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('meal_time', models.CharField(blank=True, max_length=3, null=True)),
                ('type', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'meal_pref_change',
            },
        ),
        migrations.CreateModel(
            name='Measurements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField()),
                ('parameter', models.CharField(max_length=500)),
                ('value', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'measurements',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('meal_time', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'menu',
            },
        ),
        migrations.CreateModel(
            name='Payments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_id', models.IntegerField()),
                ('timestamp', models.DateTimeField()),
                ('transaction_number', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'payments',
            },
        ),
        migrations.CreateModel(
            name='Pricing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('calories', models.IntegerField()),
                ('num_mng_meals', models.IntegerField()),
                ('num_evg_meals', models.IntegerField()),
                ('num_days', models.IntegerField()),
                ('price', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'pricing',
            },
        ),
        migrations.CreateModel(
            name='SkipMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('meal_time', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'skip_meal',
            },
        ),
        migrations.CreateModel(
            name='UpgradePlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(blank=True, null=True)),
                ('num_days', models.IntegerField()),
                ('num_bfst', models.IntegerField()),
                ('num_lunch', models.IntegerField()),
                ('num_snacks', models.IntegerField()),
                ('num_dinner', models.IntegerField()),
                ('status', models.CharField(blank=True, max_length=32, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'upgrade_plan',
            },
        ),
        migrations.CreateModel(
            name='UserAllergens',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'managed': False,
                'db_table': 'user_allergens',
            },
        ),
        migrations.CreateModel(
            name='UserFoodPref',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(blank=True, max_length=3, null=True)),
                ('meal_time', models.CharField(blank=True, max_length=3, null=True)),
                ('type', models.CharField(blank=True, max_length=3, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 'user_food_pref',
            },
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(max_length=255)),
                ('calories', models.IntegerField()),
                ('breakfast', models.IntegerField(blank=True, null=True)),
                ('lunch', models.IntegerField(blank=True, null=True)),
                ('snacks', models.IntegerField(blank=True, null=True)),
                ('dinner', models.IntegerField(blank=True, null=True)),
                ('default_address_1', models.CharField(blank=True, max_length=500, null=True)),
                ('geocode_1', models.CharField(blank=True, max_length=500, null=True)),
                ('instructions_1', models.CharField(blank=True, max_length=500, null=True)),
                ('default_address_2', models.CharField(blank=True, max_length=500, null=True)),
                ('geocode_2', models.CharField(blank=True, max_length=500, null=True)),
                ('instructions_2', models.CharField(blank=True, max_length=500, null=True)),
                ('default_address_3', models.CharField(blank=True, max_length=500, null=True)),
                ('geocode_3', models.CharField(blank=True, max_length=500, null=True)),
                ('instructions_3', models.CharField(blank=True, max_length=500, null=True)),
                ('default_address_4', models.CharField(blank=True, max_length=500, null=True)),
                ('geocode_4', models.CharField(blank=True, max_length=500, null=True)),
                ('instructions_4', models.CharField(blank=True, max_length=500, null=True)),
                ('price_per_meal', models.FloatField(blank=True, null=True)),
                ('total_cost', models.FloatField(blank=True, null=True)),
                ('sunday_meals', models.IntegerField(blank=True, null=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('meal_tokens', models.IntegerField(blank=True, null=True)),
                ('height', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('weight', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('fat_percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True)),
                ('total_calorie_intake', models.IntegerField(blank=True, null=True)),
                ('meal_preference', models.CharField(max_length=3)),
                ('email_id', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=12)),
            ],
            options={
                'managed': False,
                'db_table': 'user_profile',
            },
        ),
    ]
