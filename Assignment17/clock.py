class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds
    
    def str_update(self, timeString):
        self.hours = int(timeString[0] + timeString[1])
        self.minutes = int(timeString[3] + timeString[4])
        self.seconds = int(timeString[6] + timeString[7])

    def __str__(self):
        return "{} hours, {} minutes and {} seconds".format(self.hours, self.minutes, self.seconds)

    def add_clocks(self, clockObject):
        clockHours = (self.hours + clockObject.hours)
        clockMinutes = (self.minutes + clockObject.minutes)
        clockSeconds = (self.seconds + clockObject.seconds)

        clockMinutes += divmod(clockSeconds, 60)[0]
        clockHours += divmod(clockMinutes, 60)[0]
        clockSeconds = divmod(clockSeconds, 60)[1]
        clockMinutes = divmod(clockMinutes, 60)[1]
        clockHours = divmod(clockHours, 24)[1]
        return Clock(clockHours, clockMinutes, clockSeconds)