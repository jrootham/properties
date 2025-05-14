import geojson
import geopandas

def get(name):
	with open(name, "r") as file:
		return geojson.load(file)

def filter(value, limits):
	return value < limits.minimum or value > limits.maximum

def makeFilterFrontage(parameters):

	def filterFrontage(row)
		box = row.loc("box")

		l0 = box[0].distance(box[1])
		l1 = box[1].distance(box[2])

		frontage = min(l0, l1)
		depth = max(l0, l1)

		if filter(frontage, parameters.frontage) or filter(depth, parameters.depth):
			frontage = None

		return frontage

	return filterFrontage

def makeFrame(name, parameters):
	properties = get(name)
	frame = geopandas.GeoDataFrame.from_features(properties, crs=LATLONG)
	frame = frame.to_crs(crs=METERS)
	frame['box'] = frame.minimum_rotated_rectangle()
	frame['clipped'] = frame.apply(makeFilterFrontage(parameters))
	