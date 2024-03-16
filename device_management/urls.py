from django.urls import path
from .views import CompanyView, EmployeeView, DeviceView, CheckingLogView

urlpatterns = [
      path('company/', CompanyView.as_view(), name='company'),
      path('employee/', EmployeeView.as_view(), name = 'employee'),
      path('employee/<int:company_id>/', EmployeeView.as_view(), name = 'employee-list'),
      path('device/', DeviceView.as_view(), name= 'device'),
      path('device_log/hand_out/', CheckingLogView.as_view(), name= 'device_log'),
      
]  