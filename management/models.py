# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import date
import datetime
from decimal import *
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ValidationError

food_pref_choice = (
    ('Vegetarian','Vegetarian'),
    ('Non-Vegetarian','Non-Vegetarian'),
    ('Eggetarian','Eggetarian'),
)
weekday_choice = (
    ('Sunday','Sunday'),
    ('Monday','Monday'),
                  ('Tuesday','Tuesday'),
                  ('Wednesday','Wednesday'),
                  ('Thursday','Thursday'),
                  ('Friday','Friday'),
                  ('Saturday','Saturday'),
)
delivery_time_choice = (
                        ('Morning','Morning'),
                        ('Evening','Evening'),
)
Meal_time_choice = (
                    ('Breakfast','Breakfast'),
                    ('Lunch','Lunch'),
                    ('Snacks','Snacks'),
                    ('Dinner','Dinner'),
)
parameter_choice = (
                    ('Weight','Weight'),
                    ('Height','Height'),

    )
status_choice=(
                ('Active','Active'),
                ('Inactive','Inactive'),
                ('Stopped','Stopped'),
    )
gender_choice=(
    ('Male','Male'),
    ('Female','Female')
    )
payment_status_choice=(
                        ('Paid','Paid'),
                        ('Due','Due'),
                        ('Partially Paid','Partially Paid')
    )
upgrade_status_choice=(
                        ('Upgraded','Upgraded'),
                        ('Not upgraded','Not upgraded')
    )
new_plan_status_choice=(
                        ('Started','Started'),
                        ('Not started','Not started')
    )
bool_choice=(
            (True,'Yes'),
            (False,'No'),
    )
sunday_meals_choice=(
                    (1,'Yes'),
                    (0,'No'),
    )
replace_choice = (
                    (1,'Yes'),
                    (0,'No'),
)
state_choice =(
                ('Active','Active'),
                ('Inactive','Inactive'),
    )
class ActivityFactor(models.Model):
    activity = models.CharField(max_length=20,null=True)
    description = models.CharField(max_length=30, blank=True, null=True)
    met = models.FloatField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'activity_factor'


class AddOn(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    description = models.CharField(max_length=2000, blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    spice_level = models.IntegerField(blank=True, null=True)
    replace_breakfast = models.CharField(max_length=4,choices=replace_choice, blank=True, null=True,default=0)
    replace_lunch = models.CharField(max_length=4,choices=replace_choice, blank=True, null=True,default=0)
    replace_snacks = models.CharField(max_length=4,choices=replace_choice, blank=True, null=True,default=0)
    replace_dinner = models.CharField(max_length=4,choices=replace_choice, blank=True, null=True,default=0)
    cost = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=255,choices=status_choice,default='Active')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'add_on'
        verbose_name_plural = 'Add on products'


class AddOnOrders(models.Model):
    add_on = models.ForeignKey(AddOn, models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    replace = models.CharField(max_length=10, null=True,choices=replace_choice,default='None')
    meal_time = models.CharField(max_length=255,choices=delivery_time_choice,default='Morning')  # This field type is a guess.
    def add_on_name(self):
        return '%d-%s' % (self.add_on.id,self.add_on.name)

    class Meta:
        managed = False
        db_table = 'add_on_orders'

class Allergens(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    status = models.CharField(max_length=12,choices=state_choice,default='Inactive')
    def __unicode__(self):
        return u'%s' % (self.name)
    
    class Meta:
        managed = False
        db_table = 'allergens'
        verbose_name_plural = 'Allergens'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class CalorieFormulae(models.Model):
    calories = models.IntegerField()
    num_bfst = models.IntegerField()
    num_lunch = models.IntegerField()
    num_snacks = models.IntegerField()
    num_dinner = models.IntegerField()
    code_bfst = models.IntegerField()
    code_lunch = models.IntegerField()
    code_snacks = models.IntegerField()
    code_dinner = models.IntegerField()
    diet_goal_meal_plan = models.ForeignKey('DietGoalMealPlan', models.DO_NOTHING, blank=True, null=True)
    def diet_plan(self):
        return self.diet_goal_meal_plan.diet.diet_name
    diet_plan.short_description = 'Diet Plan'
    def goal_desc(self):
        return self.diet_goal_meal_plan.goal.description
    def meal_plan_desc(self):
        return self.diet_goal_meal_plan.meal_plan.description
    class Meta:
        managed = False
        db_table = 'calorie_formulae'
        verbose_name_plural = 'Calorie Formulae'


class CompletedOrders(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    date = models.DateField()
    address = models.CharField(null=True,blank=True,max_length=500)
    price = models.FloatField(blank=True, null=True)
    delivery_cost = models.IntegerField(blank=True, null=True)
    dishes_delivered = models.CharField(max_length=500)
    number_of_dishes = models.IntegerField()
    time_of_delivery = models.CharField(max_length=15,choices=delivery_time_choice, blank=True, null=True,default='Morning')
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'completed_orders'
        verbose_name_plural = 'Completed Orders'


class Coupons(models.Model):
    code = models.CharField(max_length=32)
    description = models.CharField(max_length=255, blank=True, null=True)
    terms_and_conditions = models.TextField(blank=True, null=True)
    expiration_date = models.DateField(blank=True, null=True)
    expiration_time = models.TimeField(blank=True, null=True)
    max_money = models.IntegerField(blank=True, null=True)
    min_order = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'coupons'
        verbose_name_plural = 'Coupons'


class DeliveryAddress(models.Model):
    date = models.DateField(blank=True, null=True)
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    address = models.CharField(max_length=500)
    geocode = models.CharField(max_length=500,blank=True,null=True)
    instructions = models.CharField(max_length=500, blank=True, null=True)
    time_of_delivery = models.CharField(max_length=255,choices=delivery_time_choice,default='Morning')  # This field type is a guess.
    kitchen = models.ForeignKey('DeliveryZones', models.DO_NOTHING,default=1)
    by = models.CharField(max_length=20, blank=True, null=True,default='admin')
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    def clean(self):
        if DeliveryAddress.objects.filter(date=self.date,user=self.user,time_of_delivery=self.time_of_delivery).count()>0:
            raise ValidationError('It is already changed for this user. Try and change the id = %s' % DeliveryAddress.objects.get(date=self.date,user=self.user,time_of_delivery=self.time_of_delivery).id)
        if self.date<date.today():
            raise ValidationError('Date should be >= today')
        if Holidays.objects.filter(date=self.date):
            raise ValidationError('Delivery address cannot be changed on a holiday')
        l = [self.user.monday_meals,self.user.tuesday_meals,self.user.wednesday_meals,self.user.thursday_meals,self.user.friday_meals,self.user.saturday_meals,self.user.sunday_meals]
        if l[self.date.weekday()]==0:
            raise ValidationError('Meals are not delivered to this user on this weekday')
        if (SkipMeal.objects.filter(date=self.date,user=self.user,meal_time=self.time_of_delivery).count()==1 and l[6]==0) or (self.date.weekday()==5 and l[6]==1 and SkipMeal.objects.filter(date=self.date,user=self.user,meal_time=self.time_of_delivery).count()+SkipMeal.objects.filter(date=self.date+datetime.timedelta(1),user=self.user,meal_time=self.time_of_delivery).count()==2):
            raise ValidationError('Meal was skipped for this user')
        if self.date.weekday()==6:
            raise ValidationError('Cannot select a sunday')
        self.by='admin'
        m=[self.user.pincode_monday_1,self.user.pincode_tuesday_1,self.user.pincode_wednesday_1,self.user.pincode_thursday_1,self.user.pincode_friday_1,self.user.pincode_saturday_1]
        m2=[self.user.pincode_monday_2,self.user.pincode_tuesday_2,self.user.pincode_wednesday_2,self.user.pincode_thursday_2,self.user.pincode_friday_2,self.user.pincode_saturday_2]
        k=[self.user.kitchen_id_monday_1,self.user.kitchen_id_tuesday_1,self.user.kitchen_id_wednesday_1,self.user.kitchen_id_thursday_1,self.user.kitchen_id_friday_1,self.user.kitchen_id_saturday_1]
        k2=[self.user.kitchen_id_monday_2,self.user.kitchen_id_tuesday_2,self.user.kitchen_id_wednesday_2,self.user.kitchen_id_thursday_2,self.user.kitchen_id_friday_2,self.user.kitchen_id_saturday_2]
        if self.time_of_delivery=='Morning':
            if self.user.breakfast+self.user.lunch==0:
                raise ValidationError('Meals are not delivered to this user in the morning')
            else:
                t=DeliveryZones.objects.get(pincode=self.kitchen.pincode,kitchen_id=self.kitchen.kitchen_id).delivery_cost-DeliveryZones.objects.get(pincode=m[self.date.weekday()],kitchen_id=k[self.date.weekday()]).delivery_cost
                self.user.delivery_cost+=t
                self.user.delivery_due_amount+=t
                self.user.save()
        else:
            if self.user.dinner+self.user.snacks==0:
                raise ValidationError('Meals are not delivered to this user in the evening')
            else:
                t=DeliveryZones.objects.get(pincode=self.kitchen.pincode,kitchen_id=self.kitchen.kitchen_id).delivery_cost-DeliveryZones.objects.get(pincode=m2[self.date.weekday()],kitchen_id=k2[self.date.weekday()]).delivery_cost
                self.user.delivery_cost+=t
                self.user.delivery_due_amount+=t
                self.user.save()

    class Meta:
        managed = False
        db_table = 'delivery_address'
        verbose_name_plural = 'Delivery Addressess'

class DeliveryTime(models.Model):
    morning_time = models.TimeField()
    evening_time = models.TimeField()
    morning_day = models.IntegerField(default=-1)
    evening_day = models.IntegerField(default=-1)
    class Meta:
        managed = True
        db_table = 'delivery_time'

class DeliveryZones(models.Model):
    pincode = models.CharField(max_length=6)
    kitchen_id = models.CharField(max_length=255, blank=True, null=True)
    delivery_cost = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'delivery_zones'
        verbose_name_plural = 'Delivery zones'


class DietGoalMealPlan(models.Model):
    goal = models.ForeignKey('Goal', models.DO_NOTHING, db_column='goal', blank=True, null=True)
    diet = models.ForeignKey('DietPlan', models.DO_NOTHING, db_column='diet', blank=True, null=True)
    meal_plan = models.ForeignKey('MealPlan', models.DO_NOTHING, db_column='meal_plan', blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    carbs_percentage= models.IntegerField()
    protiens_percentage=models.IntegerField()
    fat_percentage= models.IntegerField()
    carbs_weight =models.IntegerField()
    protiens_weight=models.IntegerField()
    fat_weight=models.IntegerField()
    def diet_plan(self):
        return self.diet.diet_name
    def goal_desc(self):
        return self.goal.description
    def meal_plan_desc(self):
        return self.meal_plan.description
    class Meta:
        managed = False
        db_table = 'diet_goal_meal_plan'

class DietGoalMealPlanDish(models.Model):
    diet_goal_meal_plan = models.ForeignKey(DietGoalMealPlan, models.DO_NOTHING, db_column='diet_goal_meal_plan', blank=True, null=True)
    dish = models.ForeignKey('Dish', models.DO_NOTHING, blank=True, null=True)
    def diet_plan(self):
        return self.diet_goal_meal_plan.diet.diet_name
    diet_plan.short_description = 'Diet Plan'
    def goal_desc(self):
        return self.diet_goal_meal_plan.goal.description
    def meal_plan_desc(self):
        return self.diet_goal_meal_plan.meal_plan.description
    def dish_desc(self):
        return self.dish.name    
    class Meta:
        managed = False
        db_table = 'diet_goal_meal_plan_dish'

class DietPlan(models.Model):
    diet_name = models.CharField(max_length=255)
    status = models.CharField(max_length=255,choices=status_choice,default='Active')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'diet_plan'
        verbose_name_plural = 'Diet Plans'


class Dish(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=2000, blank=True, null=True)
    carbohydrates = models.IntegerField(blank=True, null=True)
    fats = models.IntegerField(blank=True, null=True)
    protein = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    instructions = models.CharField(max_length=255, blank=True, null=True)
    spice_level = models.IntegerField(blank=True, null=True)
    contains = models.CharField(max_length=255, blank=True, null=True)
    photo = models.ImageField(upload_to='dishes',default='dishes/none.jpg')
    class Meta:
        managed = False
        db_table = 'dish'
        verbose_name_plural = 'Dishes'


class DishAllergens(models.Model):
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    allergen = models.ForeignKey(Allergens, models.DO_NOTHING)
    def dish_desc(self):
        return self.dish.name
    def allergen_desc(self):
        return self.allergen.name

    class Meta:
        managed = False
        db_table = 'dish_allergens'
        verbose_name_plural = 'Dish-Allergens'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

class Exercise(models.Model):
    activity = models.ForeignKey(ActivityFactor, models.DO_NOTHING, blank=True, null=True)
    minutes = models.IntegerField()
    days = models.IntegerField(blank=True, null=True)
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    def clean(self):
        self.user.calories=30
    def activity_desc(self):
        return '%s-%s' % (self.activity.activity,self.activity.description)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'exercise'

class Feedback(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    timestamp = models.DateTimeField(blank=True, null=True)
    question = models.CharField(max_length=1000)
    answer = models.CharField(max_length=1000, blank=True, null=True)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'feedback'
        verbose_name_plural = 'Feedbacks'

class Goal(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255,choices=status_choice,default='Active')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'goal'

class Holidays(models.Model):
    date = models.DateField()
    name = models.CharField(max_length=255, blank=True, null=True)
    weekday = models.IntegerField(blank=True, null=True)
    def clean(self):
        week = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
        self.weekday=self.date.weekday()
    class Meta:
        managed = False
        db_table = 'holidays'
        verbose_name_plural = 'Holidays'

class MealPlan(models.Model):
    description = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255,choices=status_choice,default='Active')  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'meal_plan'


class MealPrefChange(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    meal_time = models.CharField(max_length=255,choices=Meal_time_choice,default='Breakfast')  # This field type is a guess.
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    by = models.CharField(max_length=20, blank=True, null=True,default='admin')
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    def clean(self):
        self.by='admin'
        if SkipMeal.objects.filter(date=self.date,user=self.user,meal_time=self.meal_time).count()==1:
            raise ValidationError('Order was skipped')
    class Meta:
        managed = False
        db_table = 'meal_pref_change'
        verbose_name_plural = 'Meal Preference Change of users'


class Measurements(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    parameter = models.CharField(max_length=500,choices=parameter_choice,default='weight')
    value = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)        
    class Meta:
        managed = False
        db_table = 'measurements'
        verbose_name_plural = 'Measurements'


class Menu(models.Model):
    date = models.DateField()
    dish = models.ForeignKey(Dish, models.DO_NOTHING)
    meal_time = models.CharField(max_length=255,choices=Meal_time_choice,default='Breakfast')  # This field type is a guess.
    diet_goal_meal_plan = models.ForeignKey(DietGoalMealPlan, models.DO_NOTHING, db_column='diet_goal_meal_plan', blank=True, null=True)
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')
    def diet_plan(self):
        return self.diet_goal_meal_plan.diet.diet_name
    diet_plan.short_description = 'Diet Plan'
    def goal_desc(self):
        return self.diet_goal_meal_plan.goal.description
    def meal_plan_desc(self):
        return self.diet_goal_meal_plan.meal_plan.description
    def dish_desc(self):
        return self.dish.name
    def clean(self):
        if self.date.weekday()==5:
            s=Menu(date=self.date+datetime.timedelta(1),dish=self.dish,meal_time=self.meal_time,diet_goal_meal_plan=self.diet_goal_meal_plan,type=self.type)
            s.save()
    class Meta:
        managed = False
        db_table = 'menu'
        verbose_name_plural = 'Menu'

class NewPlan(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    start_date = models.DateField(blank=True, null=True)
    num_days = models.IntegerField(blank=True, null=True)
    diet_goal_meal_plan = models.ForeignKey(DietGoalMealPlan, models.DO_NOTHING, blank=True, null=True)
    bft = models.IntegerField(blank=True, null=True)
    lnch = models.IntegerField(blank=True, null=True)
    snk = models.IntegerField(blank=True, null=True)
    dnr = models.IntegerField(blank=True, null=True)
    new_plan_status = models.CharField(max_length=15, choices=new_plan_status_choice,default='Not started')
    payment_status = models.CharField(max_length=10, choices=payment_status_choice,default='Due')
    due_amount = models.FloatField(blank=True, null=True)
    total_price = models.FloatField(blank=True, null=True)
    calories = models.IntegerField(blank=True, null=True)
    total_calorie_intake = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sunday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    monday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    tuesday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    wednesday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    thursday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    friday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    saturday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    default_address_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    dexa = models.BooleanField(choices = bool_choice,default=False)
    schedule_dexa = models.BooleanField(choices = bool_choice,default=True)
    def clean(self):
        if self.calories is None:
            today = date.today()
            k= self.user.dob
            age = today.year - k.year - ((today.month, today.day)<(k.month,k.day))
            if self.dexa == False and self.fat_percentage is not None:
                self.fat_percentage = self.fat_percentage*Decimal(1.2)
            if self.dexa == False and self.fat_percentage is None:
                bmi = (self.weight/((self.height/100)*(self.height/100)))
                self.fat_percentage=(Decimal(1.2)*bmi)+(Decimal(0.23)*age)-Decimal(5.4)
                if self.user.gender == 'Male':
                    self.fat_percentage = self.fat_percentage-Decimal(10.8)
            lean_body_mass = self.weight*(1-(self.fat_percentage/100))
            bmr = 370+(Decimal(21.6)*lean_body_mass)
            total_expenditure = bmr*Decimal(1.2)
            if Exercise.objects.filter(user = self.id).count()>1:
                q = Exercise.objects.get(user = self.id)
                cal =0
                for i in q:
                    l = ActivityFactor.objects.get(id = i.activity)
                    cal=cal+((l.met*35*83*i.minutes*i.days)/200)
                total_expenditure = total_expenditure+Decimal(cal/7)
            elif Exercise.objects.filter(user = self.id).count()==1:
                cal=0
                q = Exercise.objects.get(user = self.id)
                l = ActivityFactor.objects.get(id = q.activity.id)
                cal=cal+(Decimal(l.met*3.5*q.minutes*q.days)*self.weight)/200
                total_expenditure = total_expenditure+Decimal(cal/7)
            total_calorie = total_expenditure*Decimal((100+self.diet_goal_meal_plan.percentage)/100)
            if self.user.whey_protien_suppl == True:
                total_calorie = total_calorie-100
            if total_calorie<950:
                self.calories = 925
            elif total_calorie>2650:
                self.calories = 2700
            elif total_calorie == 950:
                self.calories = 1000
            else:
                self.calories=int((total_calorie+49)/100)*100
        if self.total_price is None:
            if Pricing.objects.filter(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=self.num_days,diet_goal_meal_plan=self.diet_goal_meal_plan).count()==1:
                q = Pricing.objects.get(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=self.num_days,diet_goal_meal_plan=self.diet_goal_meal_plan)
                self.total_price = q.price
            else:
                da = self.num_days-1
                while Pricing.objects.filter(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=da,diet_goal_meal_plan=self.diet_goal_meal_plan)==0:
                    da=da-1
                if da!=0:
                    q = Pricing.objects.get(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=da,diet_goal_meal_plan=self.diet_goal_meal_plan)
                    self.total_price = q.price
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    def diet_plan(self):
        return self.diet_goal_meal_plan.diet.diet_name
    diet_plan.short_description = 'Diet Plan'
    def goal_desc(self):
        return self.diet_goal_meal_plan.goal.description
    def meal_plan_desc(self):
        return self.diet_goal_meal_plan.meal_plan.description
    class Meta:
        managed = False
        db_table = 'new_plan'

class OrderTime(models.Model):
    morning_time = models.TimeField(blank=True, null=True)
    evening_time = models.TimeField(blank=True, null=True)
    morning_day = models.IntegerField(default=-1)
    evening_day = models.IntegerField(default=-1)
    class Meta:
        managed = True
        db_table = 'order_time'


class Payments(models.Model):
    payment_id = models.IntegerField()
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    transaction_number = models.IntegerField()
    status = models.CharField(max_length=32, blank=True, null=True)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'payments'
        verbose_name_plural = 'Payments recorded'


class Pricing(models.Model):
    calories = models.IntegerField()
    num_mng_meals = models.IntegerField()
    num_evg_meals = models.IntegerField()
    num_days = models.IntegerField()
    price = models.FloatField(blank=True, null=True)
    diet_goal_meal_plan = models.ForeignKey(DietGoalMealPlan, models.DO_NOTHING, db_column='diet_goal_meal_plan', blank=True, null=True)
    def diet_plan(self):
        return self.diet_goal_meal_plan.diet.diet_name
    diet_plan.short_description = 'Diet Plan'
    def goal_desc(self):
        return self.diet_goal_meal_plan.goal.description
    def meal_plan_desc(self):
        return self.diet_goal_meal_plan.meal_plan.description
    class Meta:
        managed = False
        db_table = 'pricing'
        verbose_name_plural = 'Pricing'

class Referals(models.Model):
    referee_user = models.ForeignKey('UserProfile', models.DO_NOTHING,related_name='referee', blank=True, null=True)
    referer_user = models.ForeignKey('UserProfile', models.DO_NOTHING,related_name='referer', blank=True, null=True)
    class Meta:
        managed = True
        db_table = 'referal'

class ReferalConstraints(models.Model):
    referee = models.IntegerField()
    referer = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'referal_constraints'
        
class SkipMeal(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    date = models.DateField()
    meal_time = models.CharField(max_length=255,choices=delivery_time_choice,default='Morning')  # This field type is a guess.
    by = models.CharField(max_length=20, blank=True, null=True,default='admin')
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    def clean(self):
        self.by='admin'
        if SkipMeal.objects.filter(user=self.user,date=self.date,meal_time=self.meal_time).count()>0:
            raise ValidationError('Already skipped the meal')
        if self.date<date.today() and CompletedOrders.objects.filter(date=self.date,time_of_delivery=self.meal_time,user=self.user).count()>0 and SkipMeal.objects.filter(user=self.user,date=self.date,meal_time=self.meal_time).count()==0:
            if self.meal_time=='Morning':
                self.user.meal_tokens=(self.user.breakfast)+(self.user.lunch)+(self.user.meal_tokens)
            else:
                self.user.meal_tokens=(self.user.snacks)+(self.user.dinner)+(self.user.meal_tokens)
            self.user.save()
        p=[self.user.pincode_monday_1,]
        if self.date>=date.today():
            da = int(self.user.meal_tokens/(self.user.breakfast+self.user.lunch+self.user.snacks+self.user.dinner))
            if da*(self.user.breakfast+self.user.lunch+self.user.snacks+self.user.dinner)!=self.user.meal_tokens:
                da=2*da+1
            else:
                da=2*da
            today = date.today()
            l=[self.user.monday_meals,self.user.tuesday_meals,self.user.wednesday_meals,self.user.thursday_meals,self.user.friday_meals,self.user.saturday_meals,self.user.sunday_meals]
            while da>1:
                if l[today.weekday()]==1 and Holidays.objects.filter(date=today).count()==0:
                        da=da-2
                today=today+datetime.timedelta(days=1)
            while l[today.weekday()]==0:
                today+=datetime.timedelta(days=1)
            m=[self.user.pincode_monday_1,self.user.pincode_tuesday_1,self.user.pincode_wednesday_1,self.user.pincode_thursday_1,self.user.pincode_friday_1,self.user.pincode_saturday_1]
            m2=[self.user.pincode_monday_2,self.user.pincode_tuesday_2,self.user.pincode_wednesday_2,self.user.pincode_thursday_2,self.user.pincode_friday_2,self.user.pincode_saturday_2]
            k=[self.user.kitchen_id_monday_1,self.user.kitchen_id_tuesday_1,self.user.kitchen_id_wednesday_1,self.user.kitchen_id_thursday_1,self.user.kitchen_id_friday_1,self.user.kitchen_id_saturday_1]
            k2=[self.user.kitchen_id_monday_2,self.user.kitchen_id_tuesday_2,self.user.kitchen_id_wednesday_2,self.user.kitchen_id_thursday_2,self.user.kitchen_id_friday_2,self.user.kitchen_id_saturday_2]
            if today.weekday()!=6 and self.date.weekday()!=6:
                if DeliveryAddress.objects.filter(user=self.user,date=self.date,time_of_delivery=self.meal_time).count()==0:
                    if self.meal_time=='Morning':
                        temp = DeliveryZones.objects.get(pincode=m[self.date.weekday()],kitchen_id=k[self.date.weekday()]).delivery_cost
                    else:
                        temp = DeliveryZones.objects.get(pincode=m2[self.date.weekday()],kitchen_id=k2[self.date.weekday()]).delivery_cost
                else:
                    temp_1 = DeliveryAddress.objects.get(user=self.user,date=self.date,time_of_delivery=self.meal_time)
                    temp=DeliveryZones.objects.get(pincode=temp1.pincode,kitchen_id=temp_1.kitchen).delivery_cost
                if da==1:
                    diff=DeliveryZones.objects.get(pincode=m[today.weekday()],kitchen_id=k[today.weekday()]).delivery_cost-temp
                    self.user.delivery_cost+=diff
                    self.user.delivery_due_amount+=diff
                    self.user.save()
                else:   
                    diff=DeliveryZones.objects.get(pincode=m2[today.weekday()],kitchen_id=k2[today.weekday()]).delivery_cost-temp
                    self.user.delivery_cost+=diff
                    self.user.delivery_due_amount+=diff  
                    self.user.save()

    class Meta:
        managed = False
        db_table = 'skip_meal'
        verbose_name_plural = 'Skip Meal'


class StartDate(models.Model):
    day = models.IntegerField()
    class Meta:
        managed = True
        db_table = 'start_date'

class UpgradePlan(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    num_days_extended = models.IntegerField()
    upgrade_status = models.CharField(max_length=15, choices=upgrade_status_choice,default='Not upgraded')
    payment_status = models.CharField(max_length=10, choices=payment_status_choice,default='Due')
    due_amount = models.FloatField(blank=True, null=True)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'upgrade_plan'
        verbose_name_plural = 'Updgrade plans of users'

class UpgardePlanPricing(models.Model):
    num_days_initial = models.IntegerField()
    num_days_extended_to = models.IntegerField()
    price_diff = models.IntegerField()
    status = models.CharField(max_length=12,choices=state_choice,default='Inactive')
    class Meta:
        managed = True
        db_table = 'upgrade_plan_pricing'

class UserAllergens(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING)
    allergen = models.ForeignKey(Allergens, models.DO_NOTHING)
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    def allergen_desc(self):
        return self.allergen.name
    class Meta:
        managed = False
        db_table = 'user_allergens'
        verbose_name_plural = 'Allergens of users'


class UserFoodPref(models.Model):
    user = models.ForeignKey('UserProfile', models.DO_NOTHING, blank=True, null=True)
    meal_time = models.CharField(max_length=255,choices=Meal_time_choice,default='Breakfast')  # This field type is a guess.
    weekday = models.CharField(max_length=255,choices=weekday_choice,default='Monday')  # This field type is a guess.
    type = models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    def user_desc(self):
        return '%d- %s %s' % (self.user.id,self.user.first_name,self.user.last_name)
    class Meta:
        managed = False
        db_table = 'user_food_pref'
        verbose_name_plural = 'User food preferences'

def days_between(u,start,end):
    count=0
    l=[u.monday_meals,u.tuesday_meals,u.wednesday_meals,u.thursday_meals,u.friday_meals,u.saturday_meals,u.sunday_meals]
    while start<end:
        if l[start.weekday()]==1 and Holidays.objects.filter(date=start).count()==0:
            count+=1
        start+=datetime.timedelta(1)
    return count

class UserProfile(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255,choices=status_choice,default='Active')
    calories = models.IntegerField(blank=True)
    breakfast = models.IntegerField(blank=True, null=True)
    lunch = models.IntegerField(blank=True, null=True)
    snacks = models.IntegerField(blank=True, null=True)
    dinner = models.IntegerField(blank=True, null=True)
    price_per_meal = models.FloatField(blank=True, null=True)
    total_cost = models.FloatField(blank=True, null=True)
    sunday_meals = models.IntegerField(choices=sunday_meals_choice,default=0,blank=True, null=True)
    monday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    tuesday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    wednesday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    thursday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    friday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    saturday_meals = models.IntegerField(choices=sunday_meals_choice,default=1,blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    meal_tokens = models.IntegerField(blank=True, null=True)
    height = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fat_percentage = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    total_calorie_intake = models.IntegerField(blank=True, null=True)
    delivery_zone = models.ForeignKey(DeliveryZones, models.DO_NOTHING, db_column='delivery_zone', blank=True, null=True)
    diet_goal_meal_plan = models.ForeignKey(DietGoalMealPlan, models.DO_NOTHING, db_column='diet_goal_meal_plan', blank=True, null=True)
    email_id = models.CharField(max_length=255)
    phone = models.CharField(max_length=12)
    meal_preference =models.CharField(max_length=255,choices=food_pref_choice,default='Vegetarian')  # This field type is a guess.
    gender = models.TextField(max_length=255,choices=gender_choice,default='male')  # This field type is a guess.
    referal = models.CharField(max_length=8, blank=True, null=True)
    wallet_amount = models.IntegerField(blank=True, null=True)
    payment_status = models.CharField(max_length=10, choices= payment_status_choice, default='Paid')
    due_amount = models.FloatField(blank=True, null=True)
    whey_protien_suppl = models.BooleanField(choices = bool_choice,default=False)
    dexa = models.BooleanField(choices = bool_choice,default=False)
    schedule_dexa = models.BooleanField(choices = bool_choice,default=True)
    mind_egg_bread = models.BooleanField(choices = bool_choice,default=False)
    medical_history = models.CharField(max_length=1000, blank=True, null=True)
    num_days = models.IntegerField(blank=True, null=True)
    default_address_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_monday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_tuesday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_wednesday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_thursday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_friday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    geocode_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    instructions_saturday_1 = models.CharField(max_length=500, blank=True, null=True)
    default_address_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_monday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_tuesday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_wednesday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_thursday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_friday_2 = models.CharField(max_length=500, blank=True, null=True)
    default_address_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    geocode_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    instructions_saturday_2 = models.CharField(max_length=500, blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    kitchen_id_monday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_monday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_tuesday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_tuesday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_wednesday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_wednesday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_thursday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_thursday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_friday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_friday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_saturday_1 = models.CharField(max_length=10, blank=True, null=True)
    pincode_saturday_1 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_monday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_monday_2 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_tuesday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_tuesday_2 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_wednesday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_wednesday_2 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_thursday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_thursday_2 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_friday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_friday_2 = models.CharField(max_length=6, blank=True, null=True)
    kitchen_id_saturday_2 = models.CharField(max_length=10, blank=True, null=True)
    pincode_saturday_2 = models.CharField(max_length=6, blank=True, null=True)
    delivery_cost = models.IntegerField(blank=True, null=True)
    delivery_due_amount = models.IntegerField(blank=True, null=True)
    def clean(self):
        if self.total_calorie_intake is None:
            self.total_calorie_intake = 0            
        if self.calories is None:
            today = date.today()
            age = today.year - self.dob.year - ((today.month, today.day)<(self.dob.month,self.dob.day))
            if self.dexa == False and self.fat_percentage is not None:
                self.fat_percentage = self.fat_percentage*Decimal(1.2)
            if self.dexa == False and self.fat_percentage is None:
                bmi = (self.weight/((self.height/100)*(self.height/100)))
                self.fat_percentage=(Decimal(1.2)*bmi)+(Decimal(0.23)*age)-Decimal(5.4)
                if self.gender == 'Male':
                    self.fat_percentage = self.fat_percentage-Decimal(10.8)
            lean_body_mass = self.weight*(1-(self.fat_percentage/100))
            bmr = 370+(Decimal(21.6)*lean_body_mass)
            total_expenditure = bmr*Decimal(1.2)
            if Exercise.objects.filter(user = self.id).count()>1:
                q = Exercise.objects.get(user = self.id)
                cal =0
                for i in q:
                    l = ActivityFactor.objects.get(id = i.activity)
                    cal=cal+((l.met*35*83*i.minutes*i.days)/200)
                total_expenditure = total_expenditure+Decimal(cal/7)
            elif Exercise.objects.filter(user = self.id).count()==1:
                cal=0
                q = Exercise.objects.get(user = self.id)
                l = ActivityFactor.objects.get(id = q.activity.id)
                cal=cal+(Decimal(l.met*3.5*q.minutes*q.days)*self.weight)/200
                total_expenditure = total_expenditure+Decimal(cal/7)
            total_calorie = total_expenditure*Decimal((100+self.diet_goal_meal_plan.percentage)/100)
            if self.whey_protien_suppl == True:
                total_calorie = total_calorie-100
            if total_calorie<950:
                self.calories = 925
            elif total_calorie>2650:
                self.calories = 2700
            elif total_calorie == 950:
                self.calories = 1000
            else:
                self.calories=int((total_calorie+49)/100)*100
            self.calories=self.calories-self.total_calorie_intake
        if self.total_cost is None:
            if Pricing.objects.filter(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=self.num_days,diet_goal_meal_plan=self.diet_goal_meal_plan).count()==1:
                q = Pricing.objects.get(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=self.num_days,diet_goal_meal_plan=self.diet_goal_meal_plan)
                self.total_cost = q.price
            else:
                da = self.num_days-1
                while Pricing.objects.filter(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=da,diet_goal_meal_plan=self.diet_goal_meal_plan)==0:
                    da=da-1
                if da!=0:
                    q = Pricing.objects.get(calories=self.calories,num_mng_meals=(self.breakfast+self.lunch),num_evg_meals=(self.snacks+self.dinner),num_days=da,diet_goal_meal_plan=self.diet_goal_meal_plan)
                    self.total_cost = q.price    
        if self.price_per_meal is None:
            self.price_per_meal = self.total_cost/(self.num_days*(self.breakfast+self.lunch+self.snacks+self.dinner))
        if self.meal_tokens is None:
            today=date.today()
            if today.weekday()==6:
                today+=datetime.timedelta(1)
            self.meal_tokens = (self.num_days-days_between(self,self.start_date,today))*(self.breakfast+self.lunch+self.snacks+self.dinner)
        if self.end_date is None:
            if self.start_date>date.today():
                da = self.num_days
                today = self.start_date
            else:
                da = self.meal_tokens/(self.breakfast+self.lunch+self.snacks+self.dinner)
                today = date.today()
            m=[self.monday_meals,self.tuesday_meals,self.wednesday_meals,self.thursday_meals,self.friday_meals,self.saturday_meals,self.sunday_meals]
            while da>0:
                if m[today.weekday()]==1 and Holidays.objects.filter(date=today).count()==0:
                        da=da-1
                today=today+datetime.timedelta(days=1)                    
            self.end_date = today
        if self.delivery_cost is None:
            t=self.num_days
            tod = self.start_date
            l=[self.pincode_monday_1,self.pincode_tuesday_1,self.pincode_wednesday_1,self.pincode_thursday_1,self.pincode_friday_1,self.pincode_saturday_1]
            l2=[self.pincode_monday_2,self.pincode_tuesday_2,self.pincode_wednesday_2,self.pincode_thursday_2,self.pincode_friday_2,self.pincode_saturday_2]
            k=[self.kitchen_id_monday_1,self.kitchen_id_tuesday_1,self.kitchen_id_wednesday_1,self.kitchen_id_thursday_1,self.kitchen_id_friday_1,self.kitchen_id_saturday_1]
            k2=[self.kitchen_id_monday_2,self.kitchen_id_tuesday_2,self.kitchen_id_wednesday_2,self.kitchen_id_thursday_2,self.kitchen_id_friday_2,self.kitchen_id_saturday_2]
            m=[self.monday_meals,self.tuesday_meals,self.wednesday_meals,self.thursday_meals,self.friday_meals,self.saturday_meals]
            self.delivery_cost=0
            while t>0:
                if Holidays.objects.filter(date=tod).count()==0:
                    if tod.weekday()!=6 and m[tod.weekday()]==1:
                        if self.breakfast+self.lunch>0:
                            if DeliveryZones.objects.filter(pincode=l[tod.weekday()]).count()>1:
                                self.delivery_cost+=DeliveryZones.objects.get(pincode=l[tod.weekday()],kitchen_id=k[tod.weekday()]).delivery_cost
                            else:
                                self.delivery_cost+=DeliveryZones.objects.get(pincode=l[tod.weekday()]).delivery_cost
                        if self.snacks+self.dinner>0:
                            if DeliveryZones.objects.filter(pincode=l2[tod.weekday()]).count()>1:
                                self.delivery_cost+=DeliveryZones.objects.get(pincode=l2[tod.weekday()],kitchen_id=k2[tod.weekday()]).delivery_cost
                            else:
                                self.delivery_cost+=DeliveryZones.objects.get(pincode=l2[tod.weekday()]).delivery_cost
                    t-=1
                tod+=datetime.timedelta(1)
        if self.delivery_due_amount is None:
            self.delivery_due_amount=self.delivery_cost
        if self.mind_egg_bread==True:
            temp=UserAllergens(user=self,allergen=Allergens.objects.get(name='Egg in bread'))
            temp.save()
    class Meta:
        managed = False
        db_table = 'user_profile'
        verbose_name_plural = 'Users Profile'

class WalletConstraints(models.Model):
    max_amount = models.IntegerField(blank=True, null=True)
    percentage = models.IntegerField(blank=True, null=True)
    max_amount.short_description='Maximum amount per order through wallet'
    percentage.short_description='Percentage of order amount through wallet'
    class Meta:
        managed = False
        db_table = 'wallet_constraints'

@receiver(post_save, sender=UserProfile)
def fill_pref(sender, instance, **kwargs):
    if UserFoodPref.objects.filter(user=instance.id).count()==0:
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Monday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Monday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Monday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Monday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Monday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Monday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Monday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Monday',type=instance.meal_preference)
                s.save()                        
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Sunday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Sunday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Sunday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Sunday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Sunday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Sunday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Sunday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Sunday',type=instance.meal_preference)
                s.save()
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Tuesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Tuesday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Tuesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Tuesday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Tuesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Tuesday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Tuesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Tuesday',type=instance.meal_preference)
                s.save()
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Wednesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Wednesday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Wednesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Wednesday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Wednesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Wednesday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Wednesday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Wednesday',type=instance.meal_preference)
                s.save()
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Thursday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Thursday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Thursday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Thursday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Thursday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Thursday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Thursday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Thursday',type=instance.meal_preference)
                s.save()
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Friday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Friday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Friday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Friday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Friday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Friday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Friday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Friday',type=instance.meal_preference)
                s.save()
        if instance.breakfast>=1:
            s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Saturday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Breakfast',weekday='Saturday',type=instance.meal_preference)
                s.save()                        
        if instance.lunch>=1:
            s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Saturday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Lunch',weekday='Saturday',type=instance.meal_preference)
                s.save()                        
        if instance.snacks>=1:
            s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Saturday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Snacks',weekday='Saturday',type=instance.meal_preference)
                s.save()                        
        if instance.dinner>=1:
            s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Saturday',type=instance.meal_preference)
            s.save()
            if instance.breakfast==2:
                s=UserFoodPref(user=instance,meal_time='Dinner',weekday='Saturday',type=instance.meal_preference)
                s.save() 