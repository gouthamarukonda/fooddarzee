from __future__ import print_function
from django.contrib import admin
import django.forms as forms
from django.db import models
from django.shortcuts import render,render_to_response
from django.http import HttpResponseRedirect
from datetime import date
import datetime
from decimal import *
# Register your models here.
from .models import ActivityFactor, AddOn, AddOnOrders, Allergens, CalorieFormulae, CompletedOrders, Coupons, DeliveryAddress, DeliveryTime, DeliveryZones, DietGoalMealPlan, DietGoalMealPlanDish, DietPlan, Dish, DishAllergens, Exercise, Feedback, Goal, Holidays, MealPlan, MealPrefChange, Measurements, Menu, NewPlan, OrderTime, Payments, Pricing, Referals, ReferalConstraints, SkipMeal, StartDate, UpgradePlan, UpgardePlanPricing, UserAllergens, UserFoodPref, UserProfile, WalletConstraints
from .views import order
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django import forms
from admin_views.admin import AdminViews
from django.shortcuts import redirect
from django.db import connection
from django.template import loader, Context
from django.http import HttpResponse
from django.core.exceptions import ValidationError

def days_between(u,start,end):
    count=0
    l=[u.monday_meals,u.tuesday_meals,u.wednesday_meals,u.thursday_meals,u.friday_meals,u.saturday_meals,u.sunday_meals]
    while start<end:
        if l[start.weekday()]==1 and Holidays.objects.filter(date=start).count()==0:
            count+=1
        start+=datetime.timedelta(1)
    return count

class ActivityFactorResource(resources.ModelResource):
    class Meta:
        model = ActivityFactor
        report_skipped = False
    def skip_row(self, instance, original):
        if instance.activity is not None:
            return False
        return True
class AddOnResource(resources.ModelResource):
    class Meta:
        model = AddOn
        report_skipped = False
    def skip_row(self, instance, original):
        if instance.name is not None:
            return False
        return True
class AddOnOrdersResource(resources.ModelResource):
    class Meta:
        model = AddOnOrders
class AllergensResource(resources.ModelResource):
    class Meta:
        model = Allergens
        report_skipped = False
    def skip_row(self, instance, original):
        if instance.activity is not None:
            return False
        return True
class CalorieFormulaeResource(resources.ModelResource):
    class Meta:
        model = CalorieFormulae
class CompletedOrdersResource(resources.ModelResource):
    class Meta:
        model = CompletedOrders
class CouponsResource(resources.ModelResource):
    class Meta:
        model = Coupons
class DeliveryAddressResource(resources.ModelResource):
    class Meta:
        model = DeliveryAddress
    def before_save_instance(self,instance, using_transactions, dry_run):
        if DeliveryAddress.objects.filter(date=instance.date,user=instance.user,time_of_delivery=instance.time_of_delivery).count()>0:
            raise ValidationError('It is already changed for this user. Try and change the id = %s ' %DeliveryAddress.objects.get(date=instance.date,user=instance.user,time_of_delivery=instance.time_of_delivery).id)
        if instance.date<date.today():
            raise ValidationError('Date should be >= today')
        if Holidays.objects.filter(date=instance.date):
            raise ValidationError('Delivery address cannot be changed on a holiday')
        l = [instance.monday_meals,instance.tuesday_meals,instance.wednesday_meals,instance.thursday_meals,instance.friday_meals,instance.saturday_meals,instance.sunday_meals]
        if l[date.weekday()]==0:
            raise ValidationError('Meals are not delivered to this user on this weekday')
        if SkipMeal.objects.filter(date=instance.date,user=instance.user,meal_time=instance.time_of_delivery).count()==1:
            raise ValidationError('Meal was skipped for this user')
        instance.by='admin'
        m=[instance.user.pincode_monday_1,instance.user.pincode_tuesday_1,instance.user.pincode_wednesday_1,instance.user.pincode_thursday_1,instance.user.pincode_friday_1,instance.user.pincode_saturday_1]
        m2=[instance.user.pincode_monday_2,instance.user.pincode_tuesday_2,instance.user.pincode_wednesday_2,instance.user.pincode_thursday_2,instance.user.pincode_friday_2,instance.user.pincode_saturday_2]
        k=[instance.user.kitchen_id_monday_1,instance.user.kitchen_id_tuesday_1,instance.user.kitchen_id_wednesday_1,instance.user.kitchen_id_thursday_1,instance.user.kitchen_id_friday_1,instance.user.kitchen_id_saturday_1]
        k2=[instance.user.kitchen_id_monday_2,instance.user.kitchen_id_tuesday_2,instance.user.kitchen_id_wednesday_2,instance.user.kitchen_id_thursday_2,instance.user.kitchen_id_friday_2,instance.user.kitchen_id_saturday_2]
        if time_of_delivery=='Morning':
            if instance.user.breakfast+instance.user.lunch==0:
                raise ValidationError('Meals are not delivered to this user in the morning')
            else:
                t=DeliveryZones.objects.get(pincode=instance.pincode,kitchen_id=instance.kitchen).delivery_cost-DeliveryZones.objects.get(pincode=m[date.weekday()],kitchen_id=k[date.weekday()])
                instance.user.delivery_cost+=t
                instance.user.delivery_due_amount+=t
                instance.user.save()
        else:
            if instance.user.dinner+instance.user.snacks==0:
                raise ValidationError('Meals are not delivered to this user in the evening')
            else:
                t=DeliveryZones.objects.get(pincode=instance.pincode,kitchen_id=instance.kitchen).delivery_cost-DeliveryZones.objects.get(pincode=m2[date.weekday()],kitchen_id=k2[date.weekday()])
                instance.user.delivery_cost+=t
                instance.user.delivery_due_amount+=t
                instance.user.save()
class DeliveryZonesResource(resources.ModelResource):
    class Meta:
        model = DeliveryZones
class DietGoalMealPlanResource(resources.ModelResource):
    class Meta:
        model = DietGoalMealPlan
class DietGoalMealPlanDishResource(resources.ModelResource):
	class Meta:
		model = DietGoalMealPlanDish
class DietPlanResource(resources.ModelResource):
    class Meta:
        model = DietPlan
class DishResource(resources.ModelResource):
    class Meta:
        model = Dish
class DishAllergensResource(resources.ModelResource):
    class Meta:
        model = DishAllergens
class ExerciseResource(resources.ModelResource):
    class Meta:
        model = Exercise
class FeedbackResource(resources.ModelResource):
    class Meta:
        model = Feedback
class GoalResource(resources.ModelResource):
	class Meta:
		model = Goal
class HolidaysResource(resources.ModelResource):
    class Meta:
        model = Holidays
class MealPlanResource(resources.ModelResource):
	class Meta:
		model = MealPlan
class MealPrefChangeResource(resources.ModelResource):
    class Meta:
        model = MealPrefChange
class MeasurementsResource(resources.ModelResource):
    class Meta:
        model = Measurements
class MenuResource(resources.ModelResource):
    class Meta:
        model = Menu
class NewPlanResource(resources.ModelResource):
    class Meta:
        model = NewPlan
class PaymentsResource(resources.ModelResource):
    class Meta:
        model = Payments
class PricingResource(resources.ModelResource):
    class Meta:
        model = Pricing
class ReferalResource(resources.ModelResource):
    class Meta:
        model = Referals
class SkipMealResource(resources.ModelResource):
    class Meta:
        model = SkipMeal
    def skip_row(self, instance, original):
        if SkipMeal.objects.filter(user=self.user,date=self.date,meal_time=self.meal_time).count()>0:
            return False
        return True
    def before_import_row(self,row,**kwargs):
        if row['by']=='':
            row['by']='admin'
        return row
    def before_save_instance(self,instance, using_transactions, dry_run):
        instance.by='admin'
        if SkipMeal.objects.filter(user=instance.user,date=instance.date,meal_time=instance.meal_time).count()>0:
            raise ValidationError('Already skipped the meal')
        if instance.date<date.today() and CompletedOrders.objects.filter(date=instance.date,time_of_delivery=instance.meal_time,user=instance.user).count()>0 and SkipMeal.objects.filter(user=instance.user,date=instance.date,meal_time=instance.meal_time).count()==0:
            if instance.meal_time=='Morning':
                instance.user.meal_tokens=(instance.user.breakfast)+(instance.user.lunch)+(instance.user.meal_tokens)
            else:
                instance.user.meal_tokens=(instance.user.snacks)+(instance.user.dinner)+(instance.user.meal_tokens)
            instance.user.save()
        p=[instance.user.pincode_monday_1,]
        if instance.date>=date.today():
            da = int(instance.user.meal_tokens/(instance.user.breakfast+instance.user.lunch+instance.user.snacks+instance.user.dinner))
            if da*(instance.user.breakfast+instance.user.lunch+instance.user.snacks+instance.user.dinner)!=instance.user.meal_tokens:
                da=2*da+1
            else:
                da=2*da
            today = date.today()
            l=[instance.user.monday_meals,instance.user.tuesday_meals,instance.user.wednesday_meals,instance.user.thursday_meals,instance.user.friday_meals,instance.user.saturday_meals,instance.user.sunday_meals]
            while da>1:
                if l[today.weekday()]==1 and Holidays.objects.filter(date=today).count()==0:
                        da=da-2
                today=today+datetime.timedelta(days=1)
            while l[today.weekday()]==0:
                today+=datetime.timedelta(days=1)
            m=[instance.user.pincode_monday_1,instance.user.pincode_tuesday_1,instance.user.pincode_wednesday_1,instance.user.pincode_thursday_1,instance.user.pincode_friday_1,instance.user.pincode_saturday_1]
            m2=[instance.user.pincode_monday_2,instance.user.pincode_tuesday_2,instance.user.pincode_wednesday_2,instance.user.pincode_thursday_2,instance.user.pincode_friday_2,instance.user.pincode_saturday_2]
            k=[instance.user.kitchen_id_monday_1,instance.user.kitchen_id_tuesday_1,instance.user.kitchen_id_wednesday_1,instance.user.kitchen_id_thursday_1,instance.user.kitchen_id_friday_1,instance.user.kitchen_id_saturday_1]
            k2=[instance.user.kitchen_id_monday_2,instance.user.kitchen_id_tuesday_2,instance.user.kitchen_id_wednesday_2,instance.user.kitchen_id_thursday_2,instance.user.kitchen_id_friday_2,instance.user.kitchen_id_saturday_2]
            if today.weekday()!=6 and instance.date.weekday()!=6:
                if DeliveryAddress.objects.filter(user=instance.user,date=instance.date,time_of_delivery=instance.meal_time).count()==0:
                    if instance.meal_time=='Morning':
                        temp = DeliveryZones.objects.get(pincode=m[instance.date.weekday()],kitchen_id=k[instance.date.weekday()]).delivery_cost
                    else:
                        temp = DeliveryZones.objects.get(pincode=m2[instance.date.weekday()],kitchen_id=k2[instance.date.weekday()]).delivery_cost
                else:
                    temp_1 = DeliveryAddress.objects.get(user=instance.user,date=instance.date,time_of_delivery=instance.meal_time)
                    temp=DeliveryZones.objects.get(pincode=temp1.pincode,kitchen_id=temp_1.kitchen).delivery_cost
                if da==1:
                    diff=DeliveryZones.objects.get(pincode=m[today.weekday()],kitchen_id=k[today.weekday()]).delivery_cost-temp
                    instance.user.delivery_cost+=diff
                    instance.user.delivery_due_amount+=diff
                    instance.user.save()
                else:   
                    diff=DeliveryZones.objects.get(pincode=m2[today.weekday()],kitchen_id=k2[today.weekday()]).delivery_cost-temp
                    instance.user.delivery_cost+=diff
                    instance.user.delivery_due_amount+=diff  
                    instance.user.save()
class UpgradePlanResource(resources.ModelResource):
    class Meta:
        model = UpgradePlan
class UpgardePlanPricingResource(resources.ModelResource):
    class Meta:
        model = UpgardePlanPricing
class UserAllergensResource(resources.ModelResource):
    class Meta:
        model = UserAllergens
class UserFoodPrefResource(resources.ModelResource):
    class Meta:
        model = UserFoodPref
class UserProfileResource(resources.ModelResource):
    class Meta:
        model = UserProfile
    def before_save_instance(self,instance, using_transactions, dry_run):
        if instance.total_calorie_intake is None:
            instance.total_calorie_intake = 0            
        if instance.calories is None:
            today = date.today()
            dob=instance.dob
            instance.height=Decimal(instance.height)
            instance.weight=Decimal(instance.weight)
            instance.total_calorie_intake=Decimal(instance.total_calorie_intake)
            age = today.year - dob.year - ((today.month, today.day)<(dob.month,dob.day))
            if instance.dexa==True:
                instance.fat_percentage=Decimal(instance.fat_percentage)
            if instance.dexa == False and instance.fat_percentage is not None:
                instance.fat_percentage = Decimal(instance.fat_percentage)*Decimal(1.2)
            if instance.dexa == False and instance.fat_percentage is None:
                bmi = (instance.weight/((instance.height/100)*(instance.height/100)))
                instance.fat_percentage=(Decimal(1.2)*bmi)+(Decimal(0.23)*age)-Decimal(5.4)
                if instance.gender == 'Male':
                    instance.fat_percentage = instance.fat_percentage-Decimal(10.8)
            lean_body_mass = instance.weight*(1-(Decimal(instance.fat_percentage)/100))
            bmr = 370+(Decimal(21.6)*lean_body_mass)
            total_expenditure = bmr*Decimal(1.2)
            total_calorie = total_expenditure*Decimal((100+(instance.diet_goal_meal_plan).percentage)/100)
            if instance.whey_protien_suppl == True:
                total_calorie = total_calorie-100
            if total_calorie<950:
                instance.calories = 925
            elif total_calorie>2650:
                instance.calories = 2700
            elif total_calorie == 950:
                instance.calories = 1000
            else:
                instance.calories=int((total_calorie+49)/100)*100
            instance.calories=instance.calories-instance.total_calorie_intake
        if instance.total_cost is None:
            if Pricing.objects.filter(calories=instance.calories,num_mng_meals=(instance.breakfast+instance.lunch),num_evg_meals=(instance.snacks+instance.dinner),num_days=instance.num_days,diet_goal_meal_plan=instance.diet_goal_meal_plan).count()==1:
                q = Pricing.objects.get(calories=instance.calories,num_mng_meals=(instance.breakfast+instance.lunch),num_evg_meals=(instance.snacks+instance.dinner),num_days=instance.num_days,diet_goal_meal_plan=instance.diet_goal_meal_plan)
                instance.total_cost = q.price
            else:
                da = instance.num_days-1
                while Pricing.objects.filter(calories=instance.calories,num_mng_meals=(instance.breakfast+instance.lunch),num_evg_meals=(instance.snacks+instance.dinner),num_days=da,diet_goal_meal_plan=instance.diet_goal_meal_plan)==0:
                    da=da-1
                if da!=0:
                    q = Pricing.objects.get(calories=instance.calories,num_mng_meals=(instance.breakfast+instance.lunch),num_evg_meals=(instance.snacks+instance.dinner),num_days=da,diet_goal_meal_plan=instance.diet_goal_meal_plan)
                    instance.total_cost = q.price    
        if instance.price_per_meal is None:
            instance.price_per_meal = instance.total_cost/(instance.num_days*(instance.breakfast+instance.lunch+instance.snacks+instance.dinner))
        if instance.meal_tokens is None:
            today=date.today()
            if today.weekday()==6:
                today+=datetime.timedelta(1)
            instance.meal_tokens = (instance.num_days-days_between(instance,instance.start_date,today))*(instance.breakfast+instance.lunch+instance.snacks+instance.dinner)
        if instance.end_date is None :
            if instance.start_date.date()>date.today():
                da = instance.num_days
                today = instance.start_date
            else:
                da = instance.meal_tokens/(instance.breakfast+instance.lunch+instance.snacks+instance.dinner)
                today = date.today()
            while da>0:
                if instance.sunday_meals == 1:
                    if Holidays.objects.filter(date=today).count()==0:
                        da=da-1
                    today=today+datetime.timedelta(days=1)
                else:
                    if Holidays.objects.filter(date=today).count()==0 and today.weekday()<6 :
                        da=da-1
                    today=today+datetime.timedelta(days=1)                    
            instance.end_date = today
        if instance.delivery_cost is None:
            t=instance.num_days
            tod = instance.start_date
            l=[instance.pincode_monday_1,instance.pincode_tuesday_1,instance.pincode_wednesday_1,instance.pincode_thursday_1,instance.pincode_friday_1,instance.pincode_saturday_1]
            l2=[instance.pincode_monday_2,instance.pincode_tuesday_2,instance.pincode_wednesday_2,instance.pincode_thursday_2,instance.pincode_friday_2,instance.pincode_saturday_2]
            k=[instance.kitchen_id_monday_1,instance.kitchen_id_tuesday_1,instance.kitchen_id_wednesday_1,instance.kitchen_id_thursday_1,instance.kitchen_id_friday_1,instance.kitchen_id_saturday_1]
            k2=[instance.kitchen_id_monday_2,instance.kitchen_id_tuesday_2,instance.kitchen_id_wednesday_2,instance.kitchen_id_thursday_2,instance.kitchen_id_friday_2,instance.kitchen_id_saturday_2]
            m=[instance.monday_meals,instance.tuesday_meals,instance.wednesday_meals,instance.thursday_meals,instance.friday_meals,instance.saturday_meals]
            instance.delivery_cost=0
            while t>0:
                if Holidays.objects.filter(date=tod).count()==0:
                    if tod.weekday()!=6 and m[tod.weekday()]==1:
                        if instance.breakfast+instance.lunch>0:
                            if DeliveryZones.objects.filter(pincode=l[tod.weekday()]).count()>1:
                                instance.delivery_cost+=DeliveryZones.objects.get(pincode=l[tod.weekday()],kitchen_id=k[tod.weekday()]).delivery_cost
                            else:
                                instance.delivery_cost+=DeliveryZones.objects.get(pincode=l[tod.weekday()]).delivery_cost
                        if instance.snacks+instance.dinner>0:
                            if DeliveryZones.objects.filter(pincode=l2[tod.weekday()]).count()>1:
                                instance.delivery_cost+=DeliveryZones.objects.get(pincode=l2[tod.weekday()],kitchen_id=k2[tod.weekday()]).delivery_cost
                            else:
                                instance.delivery_cost+=DeliveryZones.objects.get(pincode=l2[tod.weekday()]).delivery_cost
                    t-=1
                tod+=datetime.timedelta(1)
        if instance.delivery_due_amount is None:
            instance.delivery_due_amount=instance.delivery_cost
        return instance
    def after_import_instance(self,instance, new, **kwargs):
        if instance.mind_egg_bread==True:
            temp=UserAllergens(user=instance,allergen=Allergens.objects.get(name='Egg in bread'))
            temp.save()
        if UserFoodPref.objects.filter(user=instance.id).count()==0:
            if instance.breakfast is None:
                instance.breakfast=0
            if instance.lunch is None:
                instance.lunch=0
            if instance.snacks is None:
                instance.snacks=0
            if instance.dinner is None:
                instance.dinner=0
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
class CustomActivityFactorChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s-%s" % (obj.activity, obj.description)
class CustomAddOnChoiceField(forms.ModelChoiceField):
	def label_from_instance(self,obj):
		return "%d-%s" % (obj.id,obj.name)
class CustomAllergenChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s" % (obj.name)
class CustomDietGoalMealPlanChoiceField(forms.ModelChoiceField):
	def label_from_instance(self,obj):
		return "%d-%s-%s-%s" % (obj.id, obj.diet_plan() , obj.goal_desc(), obj.meal_plan_desc())
class CustomDietChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%d-%s" % (obj.id, obj.diet_name)
class CustomDishChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%d-%s" % (obj.id, obj.name)
class CustomGoalChoiceField(forms.ModelChoiceField):
	def label_from_instance(self,obj):
		return "%d-%s" % (obj.id, obj.description)
class CustomKitchenIdField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%s - %s" % (obj.pincode,obj.kitchen_id)
class CustomMealPlanChoiceField(forms.ModelChoiceField):
	def label_from_instance(self,obj):
		return "%d-%s" % (obj.id, obj.description)
class CustomUserChoiceField(forms.ModelChoiceField):
    def label_from_instance(self,obj):
        return "%d- %s %s" % (obj.id,obj.first_name,obj.last_name)

class AddOnOrdersForm(forms.ModelForm):
	user = CustomUserChoiceField(queryset=UserProfile.objects.all())
	add_on = CustomAddOnChoiceField(queryset=AddOn.objects.all())
	class Meta:
		model = AddOnOrders
		fields = '__all__'
class CalorieFormulaeForm(forms.ModelForm):
    diet_goal_meal_plan = CustomDietGoalMealPlanChoiceField(queryset=DietGoalMealPlan.objects.all())
    class Meta:
        model = CalorieFormulae
        fields = '__all__'
class CompletedOrdersForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = CompletedOrders
        fields = '__all__'
class DeliveryAddressForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    kitchen = CustomKitchenIdField(queryset=DeliveryZones.objects.all())
    class Meta:
        model = DeliveryAddress
        fields = '__all__'
class DietGoalMealPlanForm(forms.ModelForm):
	diet = CustomDietChoiceField(queryset=DietPlan.objects.all())
	goal = CustomGoalChoiceField(queryset=Goal.objects.all())
	meal_plan = CustomMealPlanChoiceField(queryset=MealPlan.objects.all())
	class Meta:
		model = DietGoalMealPlan
		fields = '__all__'
class DietGoalMealPlanDishForm(forms.ModelForm):
	dish = CustomDishChoiceField(queryset=Dish.objects.all())
	diet_goal_meal_plan = CustomDietGoalMealPlanChoiceField(queryset=DietGoalMealPlan.objects.all())
	class Meta:
		model = DietGoalMealPlanDish
		fields = '__all__'
class DishAllergensForm(forms.ModelForm):
    dish = CustomDishChoiceField(queryset=Dish.objects.all())
    allergen = CustomAllergenChoiceField(queryset=Allergens.objects.all())
    class Meta:
        model = DishAllergens
        fields = '__all__'
class ExerciseForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    activity = CustomActivityFactorChoiceField(queryset=ActivityFactor.objects.all())
    class Meta:
        model = Exercise
        fields = '__all__'
class FeedbackForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = Feedback
        fields = '__all__'
class MealPrefChangeForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = MealPrefChange
        fields = '__all__'
class MeasurementsForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = Measurements
        fields = '__all__'
class MenuForm(forms.ModelForm):
    diet_goal_meal_plan = CustomDietGoalMealPlanChoiceField(queryset=DietGoalMealPlan.objects.all())
    dish = CustomDishChoiceField(queryset=Dish.objects.all())
    class Meta:
        model = Menu
        fields = '__all__'
class PaymentsForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = Measurements
        fields = '__all__'
class PricingForm(forms.ModelForm):
    diet_goal_meal_plan = CustomDietGoalMealPlanChoiceField(queryset=DietGoalMealPlan.objects.all())
    class Meta:
        model = Pricing
        fields = '__all__'
class ReferalForm(forms.ModelForm):
    referee_user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    referer_user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = Referals
        fields = '__all__'
class SkipMealForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = SkipMeal
        fields = '__all__'
class UpgradePlanForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = UpgradePlan
        fields = '__all__'
class UserAllergensForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    allergen = CustomAllergenChoiceField(queryset=Allergens.objects.all())
    class Meta:
        model = UserAllergens
        fields = '__all__'
class UserFoodPrefForm(forms.ModelForm):
    user = CustomUserChoiceField(queryset=UserProfile.objects.all())
    class Meta:
        model = UserFoodPref
        fields = '__all__'
class UserProfileForm(forms.ModelForm):
    diet_goal_meal_plan = CustomDietGoalMealPlanChoiceField(queryset=DietGoalMealPlan.objects.all())
    class Meta:
        model = UserProfile
        fields = '__all__'

class ActivityFactorAdmin(ImportExportModelAdmin):
    list_display= ('id', 'activity','description')
    resource_class= ActivityFactorResource
class AddOnAdmin(ImportExportModelAdmin):
	list_display = ('id','name','type')
	resource_class = AddOnResource
class AddOnOrdersAdmin(ImportExportModelAdmin):
	form = AddOnOrdersForm
	list_display = ('id','add_on_name','user_id')
	resource_class = AddOnOrdersResource
class AllergensAdmin(ImportExportModelAdmin):
    list_display = ('id','name','type')
    resource_class = AllergensResource
class CalorieFormulaeAdmin(ImportExportModelAdmin):
    form = CalorieFormulaeForm
    list_display = ('id','calories','diet_plan','goal_desc','meal_plan_desc')
    resource_class = CalorieFormulaeResource
class CompletedOrdersAdmin(ImportExportModelAdmin):
    form = CompletedOrdersForm
    list_display = ('id','user_desc','date','time_of_delivery')
    resource_class = CompletedOrdersResource
class CouponsAdmin(ImportExportModelAdmin):
    list_display = ('id','code','expiration_time')
    resource_class = CouponsResource
class DeliveryAddressAdmin(ImportExportModelAdmin):
    form = DeliveryAddressForm
    list_display = ('id','date','user_desc')
    resource_class = DeliveryAddressResource
    exclude =['by']
class DeliveryTimeAdmin(ImportExportModelAdmin):
    list_display = ('morning_time','morning_day','evening_time','evening_day')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(DeliveryTimeAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
class DeliveryZonesAdmin(ImportExportModelAdmin):
    list_display = ('pincode','kitchen_id')
    resource_class = DeliveryZonesResource
class DietGoalMealPlanAdmin(ImportExportModelAdmin):
	list_display = ('id','diet_plan','goal_desc','meal_plan_desc')
	form = DietGoalMealPlanForm
	resource_class = DietGoalMealPlanResource
class DietGoalMealPlanDishAdmin(ImportExportModelAdmin):
	list_display = ('id','diet_plan','goal_desc','meal_plan_desc','dish_desc')
	form = DietGoalMealPlanDishForm
	resource_class = DietGoalMealPlanDishResource
class DietPlanAdmin(ImportExportModelAdmin):
    list_display = ('id','diet_name')
    resource_class = DietPlanResource
class DishAdmin(ImportExportModelAdmin):
    list_display=('id','name','type')
    resource_class = DishResource
class DishAllergensAdmin(ImportExportModelAdmin):
    form = DishAllergensForm
    list_display = ('id','dish_desc','allergen_desc')
    resource_class = DishAllergensResource
class ExerciseAdmin(ImportExportModelAdmin):
    form = ExerciseForm
    list_display = ('id','activity_desc','user_desc')
    resource_class = ExerciseResource
class FeedbackAdmin(ImportExportModelAdmin):
    form = FeedbackForm
    list_display = ('id','user_desc','question','answer')
    resource_class = FeedbackResource
class GoalAdmin(ImportExportModelAdmin):
	list_display = ('id','description')
	resource_class = GoalResource
class HolidaysAdmin(ImportExportModelAdmin):
    list_display = ('id','name','date')
    exclude = ['weekday']
    resource_class = HolidaysResource
class MealPlanAdmin(ImportExportModelAdmin):
	list_display = ('id','description')
	resource_class = MealPlanResource
class MealPrefChangeAdmin(ImportExportModelAdmin):
    form = MealPrefChangeForm
    list_display = ('id','user_desc','type')
    resource_class = MealPrefChangeResource
    exclude =['by']
class MeasurementsAdmin(ImportExportModelAdmin):
    form = MeasurementsForm
    list_display = ('id','user_desc','value','parameter')
    resource_class = MeasurementsResource
class MenuAdmin(ImportExportModelAdmin):
    form = MenuForm
    list_display = ('id','date','meal_time','dish_desc','type')
    resource_class = MenuResource
class NewPlanAdmin(ImportExportModelAdmin):
    resource_class = NewPlanResource
    list_display = ('id','user_desc','diet_plan','goal_desc','meal_plan_desc','start_date')
class OrderTimeAdmin(admin.ModelAdmin):
	list_display = ('morning_time','morning_day','evening_time','evening_day')
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	def get_actions(self, request):
		actions = super(OrderTimeAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions
class PaymentsAdmin(ImportExportModelAdmin):
    form = PaymentsForm
    list_display = ('id','user_desc','timestamp')
    resource_class = PaymentsResource
class PricingAdmin(ImportExportModelAdmin):
    form = PricingForm
    list_display = ('id','calories','num_mng_meals','num_evg_meals','num_days','price')
    resource_class = PricingResource
class ReferalsAdmin(ImportExportModelAdmin):
    form = ReferalForm
    list_display = ('referer_user','referee_user')
    resource_class = ReferalResource
class ReferalConstraintsAdmin(admin.ModelAdmin):
    list_display=('referee','referer')
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(ReferalConstraintsAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
class SkipMealAdmin(ImportExportModelAdmin):
    form = SkipMealForm
    list_display = ('id','user_desc','date','meal_time')
    resource_class = SkipMealResource
    exclude =['by']
class StartDateAdmin(ImportExportModelAdmin):
    list_display = ('day',)
    def has_add_permission(self, request):
        return False
    def has_delete_permission(self, request, obj=None):
        return False
    def get_actions(self, request):
        actions = super(StartDateAdmin, self).get_actions(request)
        if 'delete_selected' in actions:
            del actions['delete_selected']
        return actions
class UpgradePlanAdmin(ImportExportModelAdmin):
    form = UpgradePlanForm
    list_display = ('id','user_desc','num_days_extended','upgrade_status','payment_status')
    resource_class = UpgradePlanResource
class UpgardePlanPricingAdmin(ImportExportModelAdmin):
    list_display = ('id','num_days_initial','num_days_extended_to','price_diff')
    resource_class = UpgardePlanPricingResource
class UserAllergensAdmin(ImportExportModelAdmin):
    form = UserAllergensForm
    list_display = ('id','user_desc','allergen_desc')
    resource_class = UserAllergensResource
class UserFoodPrefAdmin(ImportExportModelAdmin):
    form = UserFoodPrefForm
    list_display = ('id','user_desc','weekday','meal_time','type')
    resource_class = UserFoodPrefResource
class UserProfileAdmin(ImportExportModelAdmin,AdminViews):
    form = UserProfileForm
    list_display=('id','first_name','last_name','status')
    search_fields = ('first_name','id','last_name','email_id','phone')
    list_filter = ('status',)
    exclude =['price_per_meal']
    resource_class = UserProfileResource
    actions = ['skip_meals_for_a_day']
    admin_views = (
                    ('Orders', 'order'),
                    ('Delivery', 'order_address')
        )
    class CustomForm(forms.Form):
        _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    def skip_meals_for_a_day(self,request,queryset):
        form = None
        if request.POST.get('apply'):
            d = request.POST.get('date')
            ti = request.POST.get('ti')
            for q in queryset:
            	s = SkipMeal(user=q,date=d,meal_time=ti)
            	s.save()
            self.message_user(request,"Skipped meals for the selected users")
            return HttpResponseRedirect(request.get_full_path())
        if not form:
        	form = self.CustomForm(initial={'_selected_action': request.POST.getlist(admin.ACTION_CHECKBOX_NAME)})
        return render(request,'management/skip_meals.html',context={'SkipMeals':queryset,'form':form})
    skip_meals_for_a_day.short_description = "Skip meals for selected users"

class WalletConstraintsAdmin(admin.ModelAdmin):
	list_display = ('max_amount','percentage')
	def has_add_permission(self, request):
		return False
	def has_delete_permission(self, request, obj=None):
		return False
	def get_actions(self, request):
		actions = super(WalletConstraintsAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

admin.site.register(ActivityFactor,ActivityFactorAdmin)
admin.site.register(AddOn,AddOnAdmin)
admin.site.register(AddOnOrders,AddOnOrdersAdmin)
admin.site.register(Allergens,AllergensAdmin)
admin.site.register(CalorieFormulae,CalorieFormulaeAdmin)
admin.site.register(CompletedOrders,CompletedOrdersAdmin)
admin.site.register(Coupons,CouponsAdmin)
admin.site.register(DeliveryAddress,DeliveryAddressAdmin)
admin.site.register(DeliveryTime,DeliveryTimeAdmin)
admin.site.register(DeliveryZones,DeliveryZonesAdmin)
admin.site.register(DietGoalMealPlan,DietGoalMealPlanAdmin)
admin.site.register(DietGoalMealPlanDish,DietGoalMealPlanDishAdmin)
admin.site.register(DietPlan,DietPlanAdmin)
admin.site.register(Dish,DishAdmin)
admin.site.register(DishAllergens,DishAllergensAdmin)
admin.site.register(Exercise,ExerciseAdmin)
admin.site.register(Feedback,FeedbackAdmin)
admin.site.register(Goal,GoalAdmin)
admin.site.register(Holidays,HolidaysAdmin)
admin.site.register(MealPlan,MealPlanAdmin)
admin.site.register(MealPrefChange,MealPrefChangeAdmin)
admin.site.register(Measurements,MeasurementsAdmin)
admin.site.register(Menu,MenuAdmin)
admin.site.register(NewPlan,NewPlanAdmin)
admin.site.register(OrderTime,OrderTimeAdmin)
admin.site.register(Payments,PaymentsAdmin)
admin.site.register(Pricing,PricingAdmin)
admin.site.register(Referals,ReferalsAdmin)
admin.site.register(ReferalConstraints,ReferalConstraintsAdmin)
admin.site.register(SkipMeal,SkipMealAdmin)
admin.site.register(StartDate,StartDateAdmin)
admin.site.register(UpgradePlan,UpgradePlanAdmin)
admin.site.register(UpgardePlanPricing,UpgardePlanPricingAdmin)
admin.site.register(UserAllergens,UserAllergensAdmin)
admin.site.register(UserFoodPref,UserFoodPrefAdmin)
admin.site.register(UserProfile,UserProfileAdmin)
admin.site.register(WalletConstraints,WalletConstraintsAdmin)

