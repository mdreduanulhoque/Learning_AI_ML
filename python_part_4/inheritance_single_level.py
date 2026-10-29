"""
Three types:
-> Single Level (Mentioned Below)
-> Multi-level 
-> Multiple
"""

class employee:
    start_time = "9 AM"
    end_time = "4 PM"

class teacher(employee):
    def __init__(self, subject):
        self.subject = subject

t1 = teacher("English")
print(t1.subject, t1.start_time)

