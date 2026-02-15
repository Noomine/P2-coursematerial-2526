class Time: 
    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds 
    
    @property
    def hours(self):
        return self.__hours 
    
    @hours.setter
    def hours(self, hours):
        if hours > 23 or hours < 0:
            raise ValueError('hours out of bounds')
        
        self.__hours = hours 
    

    @property
    def minutes(self):
        return self.__minutes 
    
    @minutes.setter
    def minutes(self, minutes):
        if minutes > 59 or minutes < 0:
            raise ValueError
        
        else: 
            self.__minutes = minutes 
    

    @property
    def seconds(self):
        return self.__seconds 
    
    @seconds.setter
    def seconds(self, seconds):
        if seconds > 59 or seconds < 0:
            raise ValueError
        
        else: 
            self.__seconds = seconds 

# time = Time(23, 0, 0)