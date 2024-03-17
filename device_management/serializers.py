from rest_framework import serializers
from .models import Company, Employee, Device, CheckOutLog
from .utils import get_device_by_serial_number

class CompanySerializer(serializers.ModelSerializer):
      class Meta:
            model = Company
            fields = '__all__'
            
            
class EmployeeSerializer(serializers.ModelSerializer):
      class Meta:
            model = Employee
            fields = ['company', 'name', 'email', 'phone']
            
class DeviceSerializer(serializers.ModelSerializer):
      class Meta:
            model = Device
            fields = ['company', 'device_type', 'condition', 'serial_number']
            
            
class CheckOutLogSerializer(serializers.ModelSerializer):
      device_serial_number = serializers.CharField(write_only = True)
      
      class Meta:
            model = CheckOutLog
            fields = ['device_serial_number', 'employee', 'checkout_date', 'return_date', 'checkout_condition', 'return_condition']
      
      
      # Do validation by checking ou the device by serial number 
      def create(self, validated_data):
            device_serial_number = validated_data.pop('device_serial_number')
            device = get_device_by_serial_number(device_serial_number)
            if not device:
                  raise serializers.ValidationError({'device_serial_number': ['Device with this serial number does not exist.']})
            validated_data['device'] = device
            return super().create(validated_data)