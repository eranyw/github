import pytest as pytest
import pytest
import logging


class Date:

 def __init__ (self, day: int , month : int , year : int):#initalize and verify that the input is in int
        if not isinstance(day, int):
           raise TypeError("day must be int")
        if not isinstance(month, int):
           raise TypeError("month must be int.")
        if not isinstance(year, int):
           raise TypeError ("year must be int.")

        self._day  = day
        self._month = month
        self._year = year

 def __str__(self):
  return f'{self._day}/{self._month}/{self._year}'



 """
     checking valdion of days in  month 
      January,March,May,July,August,October,December-31 days
      April,June,September,November                 -30 days
      February    leap year                         -29 days
      February    not a leap year                   -28 days
     :param _day: 
     :param _month: 
     :param _year: 
     :return: 
     """

 @pytest.mark.parametrize("x", [0, 1])
 def isValid(self):
  if(self._year >1000 and self._year < 9999) and  (self._day > 0 and self._day <=31)  and (self._month> 0 and self._month <13):
         if self._month ==1 or self._month==3 or self._month==5 or self._month==7 or self._month==8 or self._month==10 or self._month==12:
             day_update=31
             if day_update >= self._day:
                 print("is valid")
                 return True


         else:
          if self._month == 4 or self._month ==6 or self._month == 9 or self._month == 11:
              day_update = 30
              if day_update >= self._day:
                  print("is valid")
                  return True
          else:
                         if  self._year % 4 ==0:
                             day_update = 29
                             if day_update >= self._day:
                                 print("is valid")
                                 return True
                         else:
                             day_update = 28
                             if day_update >= self._day:
                                print("is valid")
                                return True
  else:
       print("you have enterd invalid date")
       return  False

  def test_isValid(self):
      yield self.isValid, 999, 32, -1
      yield self.isValid, 2000, 9, 10
  """
     #checking the nextday by isvalid functuon and return the next day date

     :return:
   """
 def getNextday(self):
     self._day+=1
     if Date.isValid(self)==True   :
             print(f'{self._day}/{self._month}/{self._year}')
             return self,self._day,self._month,self._year
     else:
         if self._month < 12:
            self._month += 1
            self._day = 1
            print(f'{self._day}/{self._month}/{self._year}')
            return self,self. _day, self._month, self._year
         else:
             if self._month == 12:
              self._month = 1
              self._day = 1
              self._year +=1
              print(f'{self._day}/{self._month}/{self._year}')
              return self, self._day, self._month, self._year

 """
   # writing the date by adding number to day given
   """
 def getNextDays(self,daysToAdd :int):

     self._day += daysToAdd
     if Date.isValid(self) == True:
         print(f'{self._day}/{self._month}/{self._year}')
         return self, self._day, self._month, self._year
     else:
         if self._month < 12:
             self._month += 1
             self._day = 1
             print(f'{self._day}/{self._month}/{self._year}')
             return self, self._day, self._month, self._year
         else:
             if self._month == 12:
                 self._month = 1
                 self._day = 1
                 self._year += 1
                 print(f'{self._day}/{self._month}/{self._year}')
                 return self, self._day, self._month, self._year

             def test_getNextDays(self):
                 yield self.getNextDays, 2
                 yield self.getNextDays, 2000
 """
   # checking two dates who is Greater 
  """
 def __gt__(self,date_gt_func):#checkig if the date gerater than the other
     if self._year>date_gt_func._year :
         print ("the first date is the bigger than the other")
     if  self._year<date_gt_func._year  :
         print(self._year, date_gt_func._year )
         print("the second date is the bigger than the other")
     else:
      if self._month>date_gt_func._month  :
         print("the first date is the bigger than the other")
      if self._month<date_gt_func._month :
         print("the second date is the bigger than the other")
      else:
           if self._day > date_gt_func._day:
             print("the first date is the bigger than the other")
           if self._day < date_gt_func._day:
             print("the second date is the bigger than the other")
 """
   # checking two dates who is Less than the other
  """
 def __lt__(self,date_lt_func): #checkig if the date less than than the other
     if self._year< date_lt_func._year :
         print ("the first date is the less than the other")
     if  self._year>date_lt_func._year :
         print(self._year, date_lt_func._year)
         print("the second date is the less than the other")
     else:
      if self._month<date_lt_func._month :
         print("the first date is the less than the other")
      if self._month>date_lt_func._month :
         print("the second date is the less than the other")
      else:
           if self._day < date_lt_func._day:
             print("the first date is the less than the other")
           if self._day > date_lt_func._day:
             print("the second date is the less than the other")

 """
    # checking two dates if the are Equal
   """
 def __eq__(self,date_eq_func):#checkig if the date equal to the other
     if self._year==date_eq_func._year  and  self._month==date_eq_func._month  and self._day == date_eq_func._day :
         print ("the dates are equal")
     else:
         print("the dates are diffrent from one another")
 def __ne__(self,date_neq_func):#checkig if the date not equal to the other
     if  not self._year==date_neq_func._year and  self._month==date_neq_func._month  and self._day == date_neq_func._day :
         print ("the dates are not equal")
     else:
         print("the dates are equal from one another")

 """
     checking if the date Greater  or equal to the other
    """
 def __gtoe__(self,date_gote_func):
      if Date.__eq__(self,date_gote_func)== True and Date.__gt__(self,date_gote_func):
         print("the first date is the Greater  or equal than the other")
      else:
         print("the second date is the Greater  or equal than the other")

 """
      checking if the date smaller or equal to the other
     """
 def __ltoe__(self,date_lote_func ):
     if Date.__eq__(self,date_lote_func) == True and Date.__lt__(self, date_lote_func):
         print("the first date is the Less than or equal than the other")
     else:
         print("the second date is the Less than or equal than the other")

 """
      reutn the result of the days Subtraction
      """
 def __sub__(self, other):
        if self._day >other._day:
           return  self._day -other._day
        else:
            assert  other._day - self._day
            return other._day - self._day

 def __main__(self):
     return self

LOGGER = logging.getLogger(__name__)


def test_logs():
    LOGGER.info('eggs info')
    LOGGER.warning('eggs warning')
    LOGGER.error('eggs error')
    LOGGER.critical('eggs critical')
    assert True

day1 =Date(3,2,2001)
day2=Date(4,5,2002)
print(day1.__str__())
print(Date.isValid(day1))
print(Date.getNextday(day1))
print(Date.getNextDays(day1,2))
print(Date.__gt__(day1, day2))
print(Date.__lt__(day1, day2))
print(Date.__eq__(day1, day2))
print(Date.__gtoe__(day1, day2))
print(Date.__sub__(day1,day2))





LOGGER = logging.getLogger(__name__)


def test_log():
    LOGGER.info('info')
    LOGGER.warning('warning')
    LOGGER.error(' error')
    LOGGER.critical('critical')
    assert True

