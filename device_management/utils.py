from .models import Device


# function for getting device by serial number
def get_device_by_serial_number(serial_number):
      try:
            return Device.objects.get(serial_number=serial_number)
      except Device.DoesNotExist:
            return None