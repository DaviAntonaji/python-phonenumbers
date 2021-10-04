import phonenumbers
from phonenumbers import geocoder, carrier, timezone



phone = input("Enter the mobile number: ")
phone = phone.replace("+", "")
phone = phone.replace(" ", "")
phone = phone.replace("-", "")

phone_number = phonenumbers.parse(phone, 'US')

print(geocoder.description_for_number(phone_number, 'US'))
print(carrier.name_for_number(phone_number, 'US'))
print(timezone.time_zones_for_number(phone_number))