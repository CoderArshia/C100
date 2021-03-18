class Car(object):
    def __init__(self,model,color,company,speed_limit):
        self.model=model
        self.color=color
        self.company=company
        self.speed_limit=speed_limit

    def start(self):
        print("Started")

    def stop(self):
        print("Stopped")

    def accelerate(self):
        print("Accelerated")

    def change_gear(self):
        print("Gear Changed")

tesla = Car ("A5","Pearl","Tesla",80)

print(tesla.speed_limit)
print(tesla.color)
print(tesla.company)
print(tesla.model)
print(tesla.start())
print(tesla.change_gear())
print(tesla.accelerate())
print(tesla.stop())




    
