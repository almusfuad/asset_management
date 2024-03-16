from .models import Device


def get_device_by_serial_number(serial_number):
      try:
            return Device.objects.get(serial_number=serial_number)
      except Device.DoesNotExist:
            return None