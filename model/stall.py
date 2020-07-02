class Food:
    def __init__(self, name, img, cost, status):
        self.name = name
        self.foodID = 0
        self.stallID = None
        self.img = img
        self.cost = cost
        self.status = status

class Stall:
    def __init__(self, name, img, status):
        self.name = name
        self.stallID = 0
        self.img = img
        self.foodlist = []
        self.status = status
        self.next = None
        self.min = 0
        self.max = 0

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
        food.stallID = self.stallID
        if self.foodlist is None:
            food.foodID = 1
        else:
            food.foodID = len(self.foodlist)+1
        self.foodlist.append(food)
        
class StallList:
    def __init__(self, stall):
        if stall is not None:
            stall.stallID = 1
        self.head = stall
        self.tail = stall

    def push(self, stall):
        if self.head is None:
            stall.stallID = 1
        else:
            stall.stallID = self.tail.stallID+1
        self.tail.next = stall
        self.tail = stall
    
    def findbyID(self, ID):
        tmp = self.head
        while tmp is not None:
            if tmp.stallID == ID:
                return tmp
            tmp = tmp.next
        return None

    def findfoodbyID(self, ID):
        tmp = self.findbyID(ID[0]).foodlist
        for f in tmp:
            if f.foodID == ID[1]:
                return f
        return None
    
    def findbyName(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            if string.lower() in tmp.name.lower():
                result.append(tmp)
            tmp = tmp.next
        return result
    
    def findfood(self, string):
        result = []
        tmp = self.head
        while tmp is not None:
            for f in tmp.foodlist:
                if string.lower() in f.name.lower():
                    dic = {"stall": tmp.name, "food": f}
                    result.append(dic)
            tmp = tmp.next
        return result

    def remove(self, ID):
        tmp = self.head
        if tmp.stallID == ID:
            self.head = tmp.next
            return
        while tmp is not None:
            if tmp.next.stallID == ID:
                tmp.next = tmp.next.next
                return

    def clear(self):
        self.__init__(None)