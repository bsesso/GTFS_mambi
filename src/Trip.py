class Trip:
	def __init__(self, info):
		self.infos = []
		self.infos.append(info)
		self.id = info["trip_id"]

	def add(self, info):
		self.infos.append(info)

	def departures_per_day(self):
		departures = 0

		for info in self.infos:
			time_interval = info["end_time"] - info["start_time"]
			if time_interval.seconds < 0:
				raise Exception("Deu ruim! tempo final < tempo inicial")

			departures += time_interval.seconds // info["headway_secs"].seconds + 1
			# print("\t(", info["end_time"], "-", info["start_time"], ") /", info["headway_secs"], "=", time_interval.seconds // info["headway_secs"].seconds + 1)

		return departures