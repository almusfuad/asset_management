from django.shortcuts import render
from rest_framework import status, views, permissions, response, generics
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, CheckOutLogSerializer
from .models import Employee, Company, Device, CheckOutLog

from .utils import get_device_by_serial_number

# Create your views here.
class CompanyView(views.APIView):
      permission_classes = []
      
      def post(self, request, *args, **kwargs):
            company_serializer = CompanySerializer(data=request.data)
            if company_serializer.is_valid():
                  company_serializer.save()
                  return response.Response(company_serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(company_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      

class EmployeeView(views.APIView):
      permission_classes = []
      
      
      def get(self, request, *args, **kwargs):
            queryset = self.get_queryset()
            serializer = EmployeeSerializer(queryset, many = True)
            return response.Response(serializer.data)
      
      def get_queryset(self):
            company_id = self.kwargs.get('company_id')
            if company_id is not None:
                  return Employee.objects.filter(company_id = company_id)
            return []
      
      def post(self, request):
            employee_serializer = EmployeeSerializer(data=request.data)
            if employee_serializer.is_valid():
                  employee_serializer.save()
                  return response.Response(employee_serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(employee_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DeviceView(views.APIView):
      permission_classes = []
      
      def post(self, request):
            device_serializer = DeviceSerializer(data = request.data)
            if device_serializer.is_valid():
                  device_serializer.save()
                  return response.Response(device_serializer.data, status=status.HTTP_201_CREATED)
            return response.Response(device_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
      
      
class CheckingLogView(views.APIView):
      permission_classes = []
      
      def post(self, request):
            checking_log_serializer = CheckOutLogSerializer(data = request.data)
            if checking_log_serializer.is_valid():
                  serial_number = checking_log_serializer.validated_data['device_serial_number']
                  device = get_device_by_serial_number(serial_number)
                  if device:
                        checking_log_serializer.save()
                        return response.Response(checking_log_serializer.data, status=status.HTTP_201_CREATED)
                  else:
                        return response.Response({"error": "A device with this serial number does not exist."}, status=status.HTTP_400_BAD_REQUEST)
            return response.Response(checking_log_serializer.errors, status=status.HTTP_400_BAD_REQUEST)