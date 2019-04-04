import sys
from GTFSReader import GTFSReader

if __name__ == '__main__':
	if len(sys.argv) < 3:
		raise Exception("Número de argumentos inválido.\n"
						"Para rodar esse programa use:\n"
						"\tpython main.py [arquivo de frequencies] [arquivo de stop_times]")
	reader = GTFSReader.reader()
	trips_dict = reader.read_frequencies(sys.argv[1])

	for _, trip in trips_dict.items():
		# print("*********************************************")
		# print("Trip:", trip.id)
		# print("*********************************************")
		departures = trip.departures_per_day()
		# print("Trip:", trip.id + ": ", departures, "departures per day\n\n")
		# print(trip.id + "," + str(departures))

	stops_dict = reader.read_stop_times(sys.argv[2])
	for stop, trips in stops_dict.items():
		print("*********************************************")
		print("Stop:", stop)
		print("*********************************************")
		buses_on_stop = 0
		trains_on_stop = 0

		for trip in trips:
			if (trips_dict[trip].isTrain()):
				trains_on_stop += trips_dict[trip].departures_per_day()
				# print("\t\t{:8}: {:4d} trains".format(trip, trips_dict[trip].departures_per_day()))
			else:
				buses_on_stop += trips_dict[trip].departures_per_day()
				print("\t\t{:8}: {:4d} buses".format(trip, trips_dict[trip].departures_per_day()))

		# if (trains_on_stop > 0):
		# 	# print("Stop: {:12} {:4d} trains per day".format(stop, trains_on_stop))
		# 	print(stop + "," + str(trains_on_stop))
		if (buses_on_stop > 0):
			print("Stop: {:12} {:4d} buses per day\n\n".format(stop, buses_on_stop))
			# print(stop + "," + str(buses_on_stop))
