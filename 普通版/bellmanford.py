class Vertex:
    def __init__(self, newName):
        self.name = newName
        self.d = 10000
        self.lastChange = None
        self.lastLine = -1
        self.changeTime = 0

    def __lt__(self, other):
        if(self.d != other.d):
            return self.d < other.d
        elif(self.changeTime < other.changeTime):
            return True
        else:
            return False


class Edge:
    def __init__(self, newU, newV, newW, newLine):
        self.u = newU
        self.v = newV
        self.w = newW
        self.line = newLine

    def __relaxCore(self):
        self.v.d = self.u.d + self.w
        if(self.u.lastLine == self.line):
            self.v.lastChange = self.u.lastChange
            self.v.lastLine = self.u.lastLine
            self.v.changeTime = self.u.changeTime
        else:
            self.v.lastChange = self.u
            self.v.lastLine = self.line
            self.v.changeTime = self.u.changeTime + 1

    def relax(self):
        if((self.u.d + self.w) < self.v.d):
            self.__relaxCore()
            return True
        elif((self.u.d + self.w) == self.v.d):
            if(self.u.lastLine == self.line):
                newChangeTime = self.u.changeTime
            else:
                newChangeTime = self.u.changeTime + 1
            if(newChangeTime < self.v.changeTime):
                self.__relaxCore()
            return True
        else:
            return False


class Graph:
    def __init__(self):
        self.vertices = []
        self.edges = []
        self.dic = {}
        self.readIn()

    def readIn(self):
        f = open("timetable.txt", "r")
        all = []
        thisLine = []
        for temp in f.readlines():
            temp = temp.rstrip().split()
            all.append(temp)
        for record in all:
            if(len(record) == 1):
                thisLine = []
                currentLine = int(record[0])
            else:
                station = []
                if(record[0] not in self.dic):
                    newVertex = Vertex(record[0])
                    self.dic[record[0]] = len(self.vertices)
                    self.vertices.append(newVertex)
                    self.edges.append([])
                else:
                    newVertex = self.vertices[self.dic[record[0]]]
                thisStation = record[0]
                thisT = int(record[1]) * 60 + int(record[2])
                station.append(thisStation)
                station.append(thisT)
                thisLine.append(station)
                for i in range(0, len(thisLine)-1):
                    preStation = thisLine[i][0]
                    preT = thisLine[i][1]
                    timeDiv = thisT - preT
                    lastVertex = self.vertices[self.dic[preStation]]
                    newEdge1 = Edge(lastVertex, newVertex,
                                    timeDiv, currentLine)
                    newEdge2 = Edge(newVertex, lastVertex,
                                    timeDiv, currentLine)
                    self.edges[self.dic[preStation]].append(newEdge1)
                    self.edges[self.dic[record[0]]].append(newEdge2)

    def initialize(self, name):
        s = self.vertices[self.dic[name]]
        for node in self.vertices:
            node.d = 10000
            node.lastChange = None
            node.lastLine = -1
        s.d = 0

    def bellmanFord(self, name):
        self.initialize(name)
        last = []
        last.append([])
        last.append([])
        last[0].append(name)
        for i in range(0, len(self.dic)):
            last[1 - (i % 2)] = []
            for aname in last[i % 2]:
                for edge in self.edges[self.dic[aname]]:
                    if(edge.relax() and edge.v.name not in last[1 - (i % 2)]):
                        last[1 - (i % 2)].append(edge.v.name)

    def dijkstra(self, name):
        self.initialize(name)
        a = []
        b = []
        b.append(self.vertices[self.dic[name]])
        while(len(b) > 0):
            b.sort()
            u = b[0]
            b.pop(0)
            a.append(u)
            for edge in self.edges[self.dic[u.name]]:
                if(edge.v not in a):
                    edge.relax()
                    if(edge.v not in b):
                        b.append(edge.v)

    def getRoute(self, endStation):
        k = self.dic[endStation]
        now = self.vertices[k]
        ans = now.name
        while(now.lastChange is not None):
            ans = now.lastChange.name + "-Line " + \
                str(now.lastLine) + "-" + ans
            now = now.lastChange
        return ans

    def getRouteContinue(self, endStation):
        k = self.dic[endStation]
        now = self.vertices[k]
        ans = now.name
        if(now.lastChange is None):
            ans = "-Line " + str(self.edges[self.dic[endStation]][0].line) + "-" + ans
        while(now.lastChange is not None):
            if(now.lastChange.lastChange is not None):
                ans = now.lastChange.name + "-Line " + \
                    str(now.lastLine) + "-" + ans
            else:
                ans = "-Line " + \
                    str(now.lastLine) + "-" + ans
            now = now.lastChange
        return ans

    def navigateBellmanFord(self, line):
        all = line.split()
        totalChangeTimes = 0
        totalTime = 0
        totalRoute = all[0]
        if(len(all) < 2):
            print("Please enter at least two stations!")
            return
        for i in range(0, len(all)-1):
            myGraph.bellmanFord(all[i])
            totalRoute = totalRoute + myGraph.getRouteContinue(all[i+1])
            totalTime = totalTime + myGraph.getTime(all[i+1])
            totalChangeTimes = totalChangeTimes + \
                myGraph.getChangeTimes(all[i+1])
        print(totalRoute)
        print("Expected time:", totalTime, "minutes")
        print("Expected to change:", totalChangeTimes, "times")

    def navigateDijstra(self, line):
        all = line.split()
        totalChangeTimes = 0
        totalTime = 0
        totalRoute = all[0]
        if(len(all) < 2):
            print("Please enter at least two stations!")
            return
        for i in range(0, len(all)-1):
            myGraph.dijkstra(all[i])
            totalRoute = totalRoute + myGraph.getRouteContinue(all[i+1])
            totalTime = totalTime + myGraph.getTime(all[i+1])
            totalChangeTimes = totalChangeTimes + \
                myGraph.getChangeTimes(all[i+1])
        print(totalRoute)
        print("Expected time:", totalTime, "minutes")
        print("Expected to change:", totalChangeTimes, "times")

    def getTime(self, endStation):
        k = self.dic[endStation]
        now = self.vertices[k]
        return now.d

    def getChangeTimes(self, endStation):
        k = self.dic[endStation]
        now = self.vertices[k]
        if(now.lastChange is None):
            return 0
        count = -1
        while(now.lastChange is not None):
            count = count + 1
            now = now.lastChange
        return count


myGraph = Graph()
myGraph.readIn()
all = input()
myGraph.navigateBellmanFord(all)
