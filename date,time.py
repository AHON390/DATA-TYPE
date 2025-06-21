
'''

from datetime import date,time,datetime
today=date.today()
now=datetime.now()
print("today's date is : ",today)
print("date time is: ",now)
'''
'''
import random
import time
def getRandomDate(startDate,endDate):
    randomgenerator=random.random()
    dateFormat="%m/%d/%y"
    startime=time.mktime(time.strptime(startDate,endDate))
    endtime=time.mktime(time.strptime(endDate,dateFormat))
    randomtime=startime+ randomgenerator*(endtime-startime)
    randomDate=time.strftime(dateFormat,time.localtime(randomtime))
    return randomDate
print("random date=",getRandomDate("1/1/2016","12/12/2018"))
'''
def hotel_cost(nigths):
    return 140*nigths
def plane_ride_cost(city):
    if "charlotte"==city:
        return 183
    elif "Tampa"==city:
        return 200
    elif "pittsburgh"==city:
        return 222
    elif "los angles"==city:
        return 400
def rental_car_cost(days):
    if days>=7:
        return 40*days - 50
    elif days>3:
        return 40*days - 20
    else:
        return 40*days
def trip_cost(city,days,spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("cost of car rental: ",rental_car_cost(5))
print("cost of plane ride: ",plane_ride_cost("los_angles"))
print("cost of hotel room: ",hotel_cost(7))
print("total cost of the trip: ",trip_cost("los_angles",7,500))
print(trip_cost("Tampa",6,500))
