from django.db import models

# Create your models here.
class Company(models.Model):
      name = models.CharField(max_length=100)
      
      def __str__(self):
            return self.name
      
class Employee(models.Model):
      company = models.ForeignKey(Company, on_delete=models.CASCADE)
      name = models.CharField(max_length=100)
      email = models.EmailField()
      phone = models.CharField(max_length=15)
      
      def __str__(self):
            return self.name
      
      
class Device(models.Model):
      PHONE = 'Phone'
      TABLET = 'Tablet'
      LAPTOP = 'Laptop'
      OTHER_GEAR = 'Other Gear'
      
      
      DEVICE_TYPE_CHOICES = [
        (PHONE, 'Phone'),
        (TABLET, 'Tablet'),
        (LAPTOP, 'Laptop'),
        (OTHER_GEAR, 'Other Gear'),
    ]
      
      
      company = models.ForeignKey(Company, on_delete=models.CASCADE)
      device_type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)
      condition = models.CharField(max_length=100)
      serial_number = models.CharField(max_length=50, null=True, blank=True)
      
      def __str__(self):
            return str(self.serial_number)
      
      class Meta:
            ordering = ['serial_number']
 
      

class CheckOutLog(models.Model):
      device = models.ForeignKey(Device, on_delete=models.CASCADE)
      employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
      checkout_date = models.DateTimeField(auto_now_add=True)
      return_date = models.DateTimeField(null=True, blank=True)
      checkout_condition = models.CharField(max_length=100)
      return_condition = models.CharField(max_length=100, null=True, blank=True)
      
      def __str__(self):
            return f"{self.device} - {self.employee}"
      
      def return_device(self, return_date, return_condition):
            self.return_date = return_date
            self.return_condition = return_condition
            self.save()