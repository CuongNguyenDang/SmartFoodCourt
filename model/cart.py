class Cart:
    def __init__(self):
        self.list=[]
        self.count=[]
        self.total=0

    def addtoCart(self,food):
        if food in self.list:
            self.count[self.list.index(food)]+=1
        else:
            self.list.append(food)
            self.count.append(1)
        self.total+=food.cost

    def remove(self,food):
        self.total-=self.count[self.list.index(food)]*food.cost
        self.count.pop(self.list.index(food))
        self.list.remove(food)

    def less(self,food):
        if self.count[self.list.index(food)]==1:
            self.remove(food)
        else:
            self.total-=food.cost
            self.count[self.list.index(food)]-=1

    def cancel(self):
        self.list.clear()
        self.total=0