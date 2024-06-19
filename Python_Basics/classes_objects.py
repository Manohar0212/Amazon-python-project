class home:

    def __init__(self,rooms, plan, place):
        self.rooms = rooms
        self.plan =  plan
        self.place = place


    def selection_place(self):
        print("Choose location",self.place)

h1 = home('3','2BHK','Bangalore')
h1.selection_place()

h2 = home('2','1BHK','Hyderabad')
h2.selection_place()









