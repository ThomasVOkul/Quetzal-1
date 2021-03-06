class Date:
    def __init__(self, year, month, day):
        """ Initialize a new date object with the passed year, month and day.

        :param year: an integer
        :param month:
        :param day:
        """
        self.year = year
        self.month = month
        self.day = day

    def get_year(self):
        """ Return the year number. """
        return self.year

    def get_month(self):
        """ Return the month number. """
        return self.month

    def get_day(self):
        """ Return the day of month. """
        return self.day

    def __ge__(self, other):
        return not (self < other)

    def __lt__(self, other):
        """ Compare the date in self with another `Date` object and determine
        which comes before the other chronologically.

        :param other: the other `Date` object to compare with.
        :return: True if `self` comes before `other`, or False otherwise.
        """

        if not isinstance(other, Date):
            raise TypeError("")

        if self.year != other.year:
            return self.year < other.year
        elif self.month != other.month:
            return self.month < other.month
        elif self.day != other.day:
            return self.day < other.day
        else:
            return False

    def __eq__(self, other):
        """ Compare the date in self with another `Date` object and determine
        if they are equal to each other.

        :param other: the other `Date` object to compare with.
        :return: True if `self` equals `other`, or False otherwise.
        """
        if not isinstance(other, Date):
            raise TypeError("")

        return (self.year == other.year) and \
               (self.month == other.month) and \
               (self.day == other.day)

    def __str__(self):
        return "{} {} {}".format(self.year, self.month, self.day)
