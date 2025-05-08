import math
import geojson
import geopandas
import area
import statistics

def getProperties(name):
	with open(name, "r") as file:
		return geojson.load(file)

def getSmall():
	return getProperties("small.json")

def getLarge():
	return getProperties("properties.json")

def dist(a,b):
	dx = a[0] - b[0]
	dy = a[1] - b[1]
	return math.sqrt(dx*dx + dy*dy)

def getLengths(lot):
	result = []
	fromPoint = None
# 
	for point in lot:
		if not fromPoint is None:
			result.append(dist(point, fromPoint))
		fromPoint = point
#
	return result

def scanProperties(propertyList, function, accumulatorStart):
#
	accumulator = accumulatorStart
#
	for feature in propertyList.features:
		accumulator = function(feature, accumulator)
#
	return accumulator

def attribute(feature, accumulator):
	pointList = list(geojson.utils.coords(feature))
#
	if len(pointList) > 2 :
		lengthList = getLengths(pointList)
		accumulator.append(sorted(lengthList)[-2])
#
	return accumulator 

def getArea(feature, accumulator):
	accumulator.append(round(area.area(feature.geometry)))
	return accumulator

def stats(p, n):
	f=scanProperties(p, getArea, [])
	s=statistics.quantiles(f, n=n)
	print(s)
