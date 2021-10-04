import phonenumbers
from phonenumbers import geocoder, carrier, timezone



phone = input("Enter the mobile number: ")
phone = phone.replace("+", "")
phone = phone.replace(" ", "")
phone = phone.replace("-", "")

phone_number = phonenumbers.parse(phone, 'GB')

print(geocoder.description_for_number(phone_number, 'GB'))
print(carrier.name_for_number(phone_number, 'GB'))
print(timezone.time_zones_for_number(phone_number))