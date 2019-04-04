from Trip import Trip
import datetime

class GTFSReader:
	__instance = None

	@staticmethod
	def reader():
		if GTFSReader.__instance == None:
			GTFSReader()
		return GTFSReader.__instance

	def __init__(self):
		if GTFSReader.__instance != None:
			raise Exception("This class is a singleton!")
		else:
			GTFSReader.__instance = self

	def read_frequencies(self, file):
		trips_dict = {}
		with open(file) as f:
			f.readline()
			for line in f:
				# line = f.readlines()
				split_line = [x.replace('"', '').strip() for x in line.split(',')]
				trip_info = self._convert_split_line(split_line)

				trip_id = trip_info["trip_id"]
				if trip_id in trips_dict:
					trips_dict[trip_id].add(trip_info)
				else:
					trips_dict[trip_id] = Trip(trip_info)
		f.close()

		return trips_dict

	def read_stop_times(self, file):
		stops_dict = {}
		with open(file) as f:
			f.readline()
			for line in f:
				split_line = [x.replace('"', '').strip() for x in line.split(',')]
				stop_id = split_line[3]
				trip_id = split_line[0]
				if stop_id in stops_dict:
					stops_dict[stop_id].append(trip_id)
				else:
					stops_dict[stop_id] = [trip_id]
		f.close()

		return stops_dict

	def _convert_split_line(self, split_line):
		line_dict = {}
		line_dict["trip_id"] = split_line[0]
		line_dict["start_time"] = self._str_to_timedelta(split_line[1])
		line_dict["end_time"] = self._str_to_timedelta(split_line[2])
		line_dict["headway_secs"] = self._str_to_timedelta(split_line[3])
		return line_dict

	def _str_to_timedelta(self, t_str):
		t_split = [int(x) for x in t_str.split(":")]

		if len(t_split) == 1:
			return datetime.timedelta(seconds = t_split[0])

		return datetime.timedelta(hours = t_split[0], minutes = t_split[1], seconds = t_split[2])