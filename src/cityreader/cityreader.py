# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).

class City:
  def __init__(self,name,lat,lon):
    self.name = name
    self.lat = lat
    self.lon = lon

  def __str__(self):
    return f"Name: {self.name} Lat: {self.lat} Lon: {self.lon}"

# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
import csv
cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list

    with open('cities.csv') as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      line_count = 0
      for row in csv_reader:
          if line_count == 0:
              lat_index = row.index("lat")
              lon_index = row.index("lng")
              name_index = row.index("city")
              line_count += 1
          else:
              cities.append(City(row[name_index],float(row[lat_index]),float(row[lon_index])))
              line_count += 1
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

print("What are the coordinates of the corners of the square area you want to search?")
print("Insert latitude and longitude values separated by a comma")
print("IE. 33.4443,-134.6456")
coord1 = input("Coordinate1 >> ").split(",")
coord2 = input("Coordinate2 >> ").split(",")
lat1,lon1 = [float(num) for num in coord1]
lat2,lon2 = [float(num) for num in coord2]

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # within will hold the cities that fall within the specified region
    within = []

    #Group the lat and lon together
    lat = tuple((lat1,lat2))
    lon = tuple((lon1,lon2))
    
    
    # Go through each city and check to see if it falls within 
    # the specified coordinates.
    within = [city for city in cities if city.lat > min(lat) and city.lat < max(lat) and city.lon > min(lon) and city.lon < max(lon)]    

    return within

for city in cityreader_stretch(lat1, lon1, lat2, lon2, cities):
  print(city)