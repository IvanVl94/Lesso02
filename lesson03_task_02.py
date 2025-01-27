from smartphone import Smartphone

catalog = [
    Smartphone(" Айфон", "Х", "+78949494949"),
    Smartphone(" Айфон", "11", "+78949704949"),
    Smartphone(" Самсунг", "с23", "+78949494949"),
    Smartphone(" Ксяоми", "нова", "+78946664949"),
    Smartphone(" Айфон", "12", "+78949411949"),
]

for smartphone in catalog:
    print (f"{smartphone.phone_brand}, {smartphone.phone_model}.  {smartphone.subscriber_number}")