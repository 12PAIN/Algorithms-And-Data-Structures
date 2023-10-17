import random


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


class Airport:
    def __init__(self, apm):
        self.carrate = apm
        self.currentTask = None
        self.timeRemaining = 0

    def tick(self):
        if self.currentTask is not None:
            self.timeRemaining = self.timeRemaining - 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):
        if self.currentTask is not None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = newtask
        self.timeRemaining = newtask.getFly() * 60 / self.carrate


class Task:
    def __init__(self, time):
        self.timestamp = time
        self.plains = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getFly(self):
        return self.plains

    def waitTime(self, currenttime):
        return currenttime - self.timestamp


def simulation(numMinutes, airplainsPerHour):
    airport = Airport(airplainsPerHour)
    airplainsFly = Queue()
    waitingtimes = []

    for currentMinutes in range(numMinutes):

        if newFly():
            task = Task(currentMinutes)
            airplainsFly.enqueue(task)

        if (not airport.busy()) and (not airplainsFly.isEmpty()):
            nexttask = airplainsFly.dequeue()
            waitingtimes.append(nexttask.waitTime(currentMinutes))
            airport.startNext(nexttask)

        airport.tick()

    averageWait = (sum(waitingtimes) / len(waitingtimes)).__round__()
    print("Время, за которое самолет садится и взлетает %6.2f мин %3d самолетов остались в аэропорту." % (averageWait, airplainsFly.size()))


def newFly():
    num = random.randrange(1, 151)
    if num == 100:
        return True
    else:
        return False


# За час аэропорт может обслужить примерно 7 самолетов (по моим личным ощущениям, из Кемеровского аэропорта)
for i in range(10):
    simulation(3600, 7)