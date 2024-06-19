class RateOfInterest:
    interest = 0.8
    def __init__(self,name,loan):
        self.name = name
        self.loan = loan
        # self. interest = interest

    def cal_interest(self):
         print("Total inerest", self.loan * self.interest)

    def cal_interest(self):
           print("Total inerest", self.loan * RateOfInterest.interest)


# p1=RateOfInterest('manish',500000)
# p1.cal_interest()
#
# p2=RateOfInterest("Joe",200000)
# p2.cal_interest()

p1=RateOfInterest('manish',500000)
p1.interest = 0.04
p1.cal_interest()

p2=RateOfInterest("Joe",200000)
p2.cal_interest()
