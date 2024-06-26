# Uncomment the following imports before adding the Model code

from django.db import models
from django.utils.timezone import now
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object

class CarMake(models.Model):
    name = models.CharField(null=False, max_length=128)
    description = models.TextField()
    country = models.CharField(max_length=128)

    def __str__(self):
        return self.name


# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many
# Car Models, using ForeignKey field)
# - Name
# - Type (CharField with a choices argument to provide limited choices
# such as Sedan, SUV, WAGON, etc.)
# - Year (IntegerField) with min value 2015 and max value 2023
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object

class CarModel(models.Model):
    car_make = models.ForeignKey(CarMake, on_delete=models.CASCADE, null=False)
    name = models.CharField(null=False, max_length=128)

    CAR_TYPE_CHOICES = [
        ('SEDAN', 'Sedan'),
        ('SUV', 'SUV'),
        ('WAGON', 'Wagon'),
        ('TRUCK', 'Truck'),
        ('CONVERTIBLE', 'Convertible')
    ]
    car_type = models.CharField(max_length=64, choices=CAR_TYPE_CHOICES, default = 'SEDAN')

    year = models.IntegerField(null=False, default=2024,
            validators=[
                    MinValueValidator(2015),
                    MaxValueValidator(2024) 
                ]
            )

    MOTOR_TYPE_CHOICES = [
        ('GAS', 'Gasoline'),
        ('DIESEL', 'Diesel'),
        ('ELECTRIC', 'Electric')
    ]
    motor_type = models.CharField(max_length=64, choices=MOTOR_TYPE_CHOICES, default = 'GAS')

    # Extended car model description
    description = models.TextField()

    # True if the car model is still in production, False if no brand-new models ara available from the maker
    in_production = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.car_make}-{self.name} {self.year}"

