#
# date_class.py - Problem Set 7, Problem 3
#
# A class to represent calendar dates       
#

class Date:
    """ A class that stores and manipulates dates that are
        represented by a day, month, and year.
    """

    # The constructor for the Date class.
    def __init__(self, init_month, init_day, init_year):
        """ constructor that initializes the three attributes  
            in every Date object (month, day, and year)
        """
        # add the necessary assignment statements below
        self.month = init_month
        self.day = init_day
        self.year = init_year
        

    # The function for the Date class that returns a string
    # representation of a Date object.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this *can* be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year, and False otherwise.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, and year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date
    
    #### Put your code for problem 2 below. ####
    #### Make sure that it is indented by an appropriate amount. ####


    # function 3
    def advance_one(self):
        """ changes the called object so that it represents the
        day after the date that it originally represented
        No return! """
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
        if self.day == days_in_month[self.month]:
            if self.month == 12:
                self.year += 1
                self.month = 1
                self.day = 1
            else:
                self.month += 1
                self.day = 1
        else:
            self.day += 1
            
    # function 4
    def advance_n(self, n):
        """ changes the calling object so that it represents 
        n days after the date it originally represented
        No return! """
        print(self)
        for i in range(n):
            self.advance_one()
            print(self)
            
    # function 5
    def __eq__(self, other):
        """ returns True if called object(self) and the argument
        (other) represent the same date and if not, return False """
        if self.year == other.year and self.month == other.month \
            and self.day == other.day:
            return True
        else:
            return False
        
    # function 6
    def is_before(self, other):
        """ returns True if the called object represents a date
        before the date that is represented by other """
        if self.year < other.year:
            return True
        elif self.year == other.year and self.month < other.month:
            return True
        elif self.year == other.year and self.month == other.month\
        and self.day < other.day:
            return True
        else:
            return False
        
    # function 7
    def is_after(self, other):
        """ returns True if the calling object represents a date
        that occurs after the date that is represented by other """
        if self.year > other.year:
            return True
        elif self.year == other.year and self.month > other.month:
            return True
        elif self.year == other.year and self.month == other.month\
        and self.day > other.day:
            return True
        else:
            return False
        
    # function 8
    def days_between(self, other):
        """ returns an integer that represents the number of days
        between self and other """
        self_copy = self.copy()
        other_copy = other.copy()
        count = 0
        if self.is_after(other) == True:
            while True:
                count += 1
                other_copy.advance_one()
                if self_copy == other_copy:
                    break
            return count
        elif self.is_before(other) == True:
            while True:
                count -= 1
                self_copy.advance_one()
                if self_copy == other_copy:
                    break
            return count
        elif self.__eq__(other):
            return count 
        
    # function 9
    def day_name(self):
        """ returns a string that indicates the name of the day
        of the week of the date object that calls it
        (e.g. Monday, Tuesday,...) """
        day_names = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        d = Date(11, 8, 2021) # monday
        n = self.days_between(d)
        return day_names[n%7]
        
        
                    
# test
'''
d1 = Date(11, 14, 2021)
print(d1.month)
print(d1.year)
print(d1.day)
print(d1)
print(d1.is_leap_year())
d1 = Date(2, 21, 2024)
d2 = d1
d3 = d1.copy()
d1 = Date(2, 23, 2021)
d2 = Date(11, 12, 2021)
#d1.advance_one()
d1.advance_n(4)
#print(d1)
print(d1.is_before(d2))
print(d1.is_after(d2))
print(d1.days_between(d2))
print(d1.day_name())
'''
