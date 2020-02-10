#Life calculator
from datetime import datetime
import numpy as np 
from PIL import Image
class LifeCalc():
    def __init__(self, my_bday):
        self.my_age = 25
        year, month, day = my_bday[2], my_bday[0], my_bday[1]
        self.my_bday = datetime.date(datetime(year, month, day))
        self.todays_date = datetime.date(datetime.now())
        self.calendar_dict = {"Jan":(1, 31),  "Feb":(2, 28), "Mar":(3, 31),
                              "Apr":(4, 30),  "May":(5, 31), "Jun":(6, 30),
                              "Jul":(7, 31),  "Aug":(8, 31), "Sep":(9, 30), 
                              "Oct":(10, 31), "Nov":(11, 30),"Dec":(12, 31) 
                              }
    def time_alive(self, time_unit):
        time_alive = self.todays_date - self.my_bday
        
        if time_unit == 'Year':
            years = time_alive.days//365
            _remain = time_alive.days%365
            weeks = _remain//7
            days = _remain%7

        if time_unit == 'Week':
            years = None
            weeks = time_alive.days//7
            days = time_alive.days%7

        if time_unit == "Day":
            years = None
            weeks = None
            days = time_alive.days
        return years, weeks, days

    def build_array(self, death_age, time_unit):
        if time_unit == 'Day':
            squares = death_age * 365
            cols = 183
            rows = (squares//cols)+1
            calendar = np.zeros((rows,cols))
            return calendar
        if time_unit == 'Week':
            squares = death_age * 52
            cols = 52
            rows = (squares//cols)+1
            calendar = np.zeros((rows,cols))
            return calendar
        if time_unit == 'Year':
            #does squares 1/2 decade per row by number of rows til death
            squares = death_age
            cols = 5
            rows = (squares//cols)+1
            calendar = np.zeros((rows,cols))
            return calendar
    def fill_array(self, death_age = 90, time_unit = 'Week'):
        array = self.build_array(death_age, time_unit)
        alive_for = self.time_alive(time_unit)
        if time_unit == 'Day':
            alive_for = self.time_alive(time_unit)[2]
        if time_unit == 'Week':
            alive_for = self.time_alive(time_unit)[1]
        if time_unit == 'Year':
            alive_for = self.time_alive(time_unit)[0]
        block_counter = 0
        for i in range(array.shape[0]):
            for j in range(array.shape[1]):
                if block_counter<alive_for:
                    array[i, j] = 1
                    block_counter +=1
                else:
                    return array
    def create_image_from_array(self, array):
        if cell == past:
            color = (77, 28, 0)
        if cell == present:
            color = (3, 52, 11)
        if cell == future:
            color = (0, 207, 189)
        one_square = Image.new("RGB", (12, 12), color)

if __name__=="__main__":
    a = LifeCalc([5, 19, 1994], )
    # yrs = a.time_alive('Years')
    # wks = a.time_alive('Weeks')
    # dys = a.time_alive('Days')
    
    arry = a.fill_array()
    print(arry)