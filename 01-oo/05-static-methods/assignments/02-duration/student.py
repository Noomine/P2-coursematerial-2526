class Duration: 
    def __init__(self, seconds):
        self._seconds = seconds

    
    @property 
    def seconds(self):
        return self._seconds
    
    @property 
    def hours(self):
        return (self.seconds / 3600)
    
    @staticmethod
    def from_seconds(seconds):
        duration = Duration(seconds)
        return duration
    

    # def from_hours
    @staticmethod
    def from_minutes(minutes):
        return Duration(minutes * 60)
    
    @staticmethod
    def from_hours(hours):
        return Duration(hours * 3600)

