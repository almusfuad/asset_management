from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Company, Employee, Device, CheckOutLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, CheckOutLogSerializer
from datetime import datetime

# Create your tests here.
class CompanyViewTest(TestCase):
      def setUp(self):
            self.client = APIClient()
            
      def test_create_company(self):
            data = {'name': 'Test Company'}
            response = self.client.post('/device_management/company/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Company.objects.count(), 1)
            self.assertEqual(Company.objects.get().name, 'Test Company')
            
class EmployeeViewTest(TestCase):
      def setUp(self):
            self.client = APIClient()
            self.company = Company.objects.create(name='Test Company')

      def test_create_company(self):
            data = {'company': self.company.id, 'name': 'Test Employee', 'email': 'test@example.com', 'phone': '1234567890'}
            response = self.client.post('/device_management/employee/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Employee.objects.count(), 1)
            self.assertEqual(Employee.objects.get().name, 'Test Employee')
            

class DeviceViewTest(TestCase):
      def setUp(self):
            self.client = APIClient()
            self.company = Company.objects.create(name='Test Company')
            
      def test_create_device(self):
            data = {'company': 1, 'device_type': 'Phone', 'condition': 'Good', 'serial_number': 'ABC123'}
            response = self.client.post('/device_management/device/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(Device.objects.count(), 1)
            self.assertEqual(Device.objects.get().serial_number, 'ABC123')
            

class CheckingLogView(TestCase):
      def setUp(self):
            self.client = APIClient()
            self.company = Company.objects.create(name = 'Test Company')
            self.employee = Employee.objects.create(company = self.company, name = 'Test Employee', email = 'test@example.com', phone='1234567890')
            self.device = Device.objects.create(company = self.company, device_type = 'Phone', condition='Good', serial_number='ABC123')
            
      def test_checking_log(self):
            data = {'device_serial_number': 'ABC123', 'employee': self.employee.id, 'checkout_date': datetime.now().isoformat(), 'checkout_condition': 'Good', 'return_condition': ''}
            response = self.client.post('/device_management/device_log/hand_out/', data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(CheckOutLog.objects.count(), 1)
            