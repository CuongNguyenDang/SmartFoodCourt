class Food:
    def __init__(self, ID, name, stallID, img, cost, status):
        self.foodID = ID
        self.name = name
        self.stallID = stallID
        self.img = img
        self.cost = cost
        self.status = status
        self.next = None

class FoodList:
    def __init__(self, food):
        self.head = food
        self.tail = food

    def push(self, food):
        if self.head is None:
            self.__init__(food)
            return
        self.tail.next = food
        self.tail = food
    
    def findbyID(self, ID):
        tmp = self.head
        while tmp is not None:
            if tmp.foodID == ID:
                return tmp
            tmp = tmp.next
        return None
    
    def findbyName(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            if string.lower() in tmp.name.lower():
                result.append(tmp)
            tmp = tmp.next
        return result

    def clear(self):
        self.__init__(None)

class Stall:
    def __init__(self, ID, name, img, status):
        self.stallID = ID
        self.name = name
        self.img = img
        self.foodlist = []
        self.status = status
        self.min = 0
        self.max = 0
        self.next = None

    def addfood(self, food):
        if not self.foodlist:
            self.min = food.cost
            self.max = food.cost
        else:
            for f in self.foodlist:
                if f.cost > self.max:
                    self.max = f.cost
                if f.cost < self.min:
                    self.min = f.cost
        self.foodlist.append(food)
        
class StallList:
    def __init__(self, stall):
        self.head = stall
        self.tail = stall

    def push(self, stall):
        if self.head is None:
            self.__init__(stall)
            return
        self.tail.next = stall
        self.tail = stall
    
    def findbyID(self, ID):
        tmp = self.head
        while tmp is not None:
            if tmp.stallID == ID:
                return tmp
            tmp = tmp.next
        return None
    
    def findbyName(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            if string.lower() in tmp.name.lower():
                result.append(tmp)
            tmp = tmp.next
        return result

    def clear(self):
        self.__init__(None)