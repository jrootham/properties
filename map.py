import sys
import parameters
import properties

def main(arglist):
	if (len(arglist) == 3):
		current = parameters.get(arglist[1])
		data = properties.get(arglist[2]) 

		print(len(data))
		
	else:
		print("Usage: map.py parameters.json data.geojson")

main(sys.argv)
