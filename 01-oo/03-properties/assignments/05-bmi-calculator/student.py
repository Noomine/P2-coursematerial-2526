class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight = weight_in_kg 
        self.height = height_in_m

    @property 
    def category(self):
        if self.bmi > 25:
            return  "overweight"
        elif self.bmi < 18.5:
            return  "underweight"
        else:
            return  "normal"
    
    @property
    def bmi(self):
        return  self.weight / (self.height* self.height)
