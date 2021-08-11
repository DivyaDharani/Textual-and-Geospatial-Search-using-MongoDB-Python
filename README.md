# Textual and Geospatial Search using MongoDB and Python

**Input Data:** testData.json
* Contains details about businesses such as Name, Address, Location Coordinates (Latitude and Longitude), Categories, etc.

**Two search options for finding businesses:**
* Search based on City - for searching businesses present in a particular city => **Textual Search**
* Search based on Geospatial Location - to find all the businesses present within a max distance from the given location => **Geospatial Search**

#### Distance Algorithm used:
Given two pair of latitude and longitude as [lat2, lon2] and [lat1, lon1], you can calculate the distance between them using the formula given below:

```
DistanceFunction(lat2, lon2, lat1, lon1):

  var R = 3959; // miles
  var φ1 = lat1.toRadians();
  var φ2 = lat2.toRadians();
  var Δφ = (lat2-lat1).toRadians();
  var Δλ = (lon2-lon1).toRadians();
  var a = Math.sin(Δφ/2) * Math.sin(Δφ/2) +
  Math.cos(φ1) * Math.cos(φ2) *
  Math.sin(Δλ/2) * Math.sin(Δλ/2);
  var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1-a));
  var d = R * c;
```
d is the distance between the given pair of latitude and longitude. The distance is in
miles. Reference: http://www.movable-type.co.uk/scripts/latlong.html

