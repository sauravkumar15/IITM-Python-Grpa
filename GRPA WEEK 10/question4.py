'''
GRPA 4 - Time Conversion Class - GRADED

Problem statement:
Implement a class `Time` that takes input in seconds and provides methods to 
convert the time into minutes, hours, and days.

Class Specifications:

1. class Time:
    __init__(self, time):
        Initializes the object with time in seconds.

    second_to_minutes(self):
        Converts seconds into minutes and seconds.
        Returns a formatted string like "X min Y sec".

    second_to_hours(self):
        Converts seconds into hours, minutes, and seconds.
        Returns a formatted string like "X hrs Y min Z sec".

    second_to_days(self):
        Converts seconds into days, hours, minutes, and seconds.
        Returns a formatted string like "X days Y hrs Z min W sec".
'''

# Solution

class Time:
    def __init__(self, time):
        self.time = time

    def second_to_minutes(self):
        minutes = self.time // 60
        seconds = self.time % 60
        return f"{minutes} min {seconds} sec"

    def second_to_hours(self):
        hours = self.time // 3600
        minutes = (self.time % 3600) // 60
        seconds = self.time % 60
        return f"{hours} hrs {minutes} min {seconds} sec"

    def second_to_days(self):
        days = self.time // 86400
        hours = (self.time % 86400) // 3600
        minutes = (self.time % 3600) // 60
        seconds = self.time % 60
        return f"{days} days {hours} hrs {minutes} min {seconds} sec"


# Example usage
t1 = Time(3661)
print(t1.second_to_minutes())  # 61 min 1 sec
print(t1.second_to_hours())    # 1 hrs 1 min 1 sec
print(t1.second_to_days())     # 0 days 1 hrs 1 min 1 sec
