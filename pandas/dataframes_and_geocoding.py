from geopy.geocoders import ArcGIS

nom=ArcGIS()

address = input("Please input your address: ")
location = nom.geocode(address)
print(location)