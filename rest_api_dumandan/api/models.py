from django.db import models

class Car(models.Model):
    brand = models.CharField(max_length=100, null=True, blank=True)
    model = models.CharField(max_length=100, null=True, blank=True)
    year = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)  
    transmission = models.CharField(max_length=20, null=True, blank=True, choices=[("MT", "Manual"), ("AT", "Automatic")])
    fuel_type = models.CharField(max_length=20, null=True, blank=True, choices=[("Gasoline", "Gasoline"), ("Diesel", "Diesel"), ("Electric", "Electric"), ("Hybrid", "Hybrid")])
    mileage = models.PositiveIntegerField(default=0)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__ (self):
        return self.model
    
    class Meta:
        db_table_comment = "Cars Table"
