import phonenumbers
from phonenumbers import geocoder, carrier, timezone



phone = input("Digite o número de telefone: ")
phone = phone.replace("+", "")
phone = phone.replace(" ", "")
phone = phone.replace("-", "")

phone_number = phonenumbers.parse(phone, 'BR')

# Aqui diz a geolocalização da provedora
print(geocoder.description_for_number(phone_number, 'BR'))
# Aqui diz o nome da provedora
print(carrier.name_for_number(phone_number, 'BR'))
# Aqui diz o timezone
print(timezone.time_zones_for_number(phone_number))