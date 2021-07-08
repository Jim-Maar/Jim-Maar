from turtle import *
import math

def dist(x1,x2,y1,y2):
    return((y1-y2)**2+(x1-x2)**2)**0.5

def collision(x1,x2,x3,x4,y1,y2,y3,y4):
    if ((x1 != x3 or y1 != y3) and (x2 != x3 or y2 != y3)) and ((x1 != x4 or y1 != y4) and (x2 != x4 or y2 != y4)):
        den = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
        if den != 0:
            t = ((x1-x3)*(y3-y4)-(y1-y3)*(x3-x4))/den
            u = -((x1-x2)*(y1-y3)-(y1-y2)*(x1-x3))/den
            if (0<=t and t<=1) and (0<=u and u<=1):
                Px = x1 + t*(x2-x1)
                Py = y1 + t*(y2-y1)
                return True
    return False

def allcollisions(x3,x4,y3,y4):
    for stone in file:
        for corner in range(0,len(stone)):
            x1 = stone[corner]["x"]
            y1 = stone[corner]["y"]
            if corner == len(stone)-1:
                x2 = stone[0]["x"]
                y2 = stone[0]["y"]
            else:       
                x2 = stone[corner+1]["x"]
                y2 = stone[corner+1]["y"]
            if collision(x1,x2,x3,x4,y1,y2,y3,y4):
                return True
    return False

def couldbereachable(prevx,prevy,nexx,nexy,stonenum,cornernum,hull,maxcornernum):
    if stonenum == -2 and cornernum == -2:
        return True
    
    if cornernum < maxcornernum:
        curr1x = file[stonenum][cornernum+1]["x"]
        curr1y = file[stonenum][cornernum+1]["y"]
    else:
        curr1x = file[stonenum][0]["x"]
        curr1y = file[stonenum][0]["y"]
    curr2x = file[stonenum][cornernum-1]["x"]
    curr2y = file[stonenum][cornernum-1]["y"]
    
    if is_ccw(prevx,curr1x,curr2x,prevy,curr1y,curr2y) == 0:
        return False
    if is_ccw(prevx,curr1x,curr2x,prevy,curr1y,curr2y) == is_ccw(curr2x,prevx,nexx,curr2y,prevy,nexy) and is_ccw(prevx,curr2x,curr1x,prevy,curr2y,curr1y) == is_ccw(curr1x,prevx,nexx,curr1y,prevy,nexy):
        if hull:
            return False
        else:
           return True
    if hull:
        return True
    else:
        return False

def is_ccw(ax,bx,cx,ay,by,cy):
    area = (bx-ax)*(cy-ay) - (by-ay) * (cx-ax)
    if area < 0:
        #clockwise
        return -1
    if area > 0:
        #counterclockwise
        return 1
    #collinear
    return 0

def fakeGrahamScan(file):
    for stone in file:
        recordy = stone[0]["y"]
        pos = -1
        for corner in stone:
            pos += 1
            if corner["y"] <= recordy:
                recordy = corner["y"]
                recordypos = pos
        neighbor1 = stone[recordypos-1]
        if recordypos == len(stone)-1:
            neighbor2 = stone[0]
        else:
            neighbor2 = stone[recordypos+1]
        startcorner = stone[recordypos]
        
        turn = is_ccw(startcorner["x"],neighbor1["x"],neighbor2["x"],startcorner["y"],neighbor1["y"],neighbor2["y"])
        for i in range(recordypos-len(stone)+1,recordypos):
            startcorner = stone[i]
            neighbor1 = stone[i-1] 
            neighbor2 = stone[i+1]
            if is_ccw(startcorner["x"],neighbor1["x"],neighbor2["x"],startcorner["y"],neighbor1["y"],neighbor2["y"]) != turn:
                startcorner["hull"] = False
    return file         

def GrahamScan(file):
    stonenum = -1
    for stone in file:
        stonenum +=1
        #Ancor
        Ancory = 99999
        cornernum = -1
        for corner in stone:
            if corner["y"] <= Ancory:
                Ancory = corner["y"]
                Ancor = corner
        sortedanglelist = []
        for corner in stone:
            cornernum += 1
            if corner["x"]-Ancor["x"] != 0:
                sortangle = math.atan((corner["y"]-Ancory) /abs(corner["x"]-Ancor["x"]))
                if corner["x"]-Ancor["x"] < 0:
                    sortangle = math.pi/2 - sortangle + math.pi/2
            elif corner["y"]-Ancory == 0:
                sortangle = 0
            else:
                sortangle = 90
            sortedanglelist += [{"sortangle":sortangle,"stonenum":stonenum,"cornernum":cornernum,"corner":corner}]
        sortedanglelist = sorted(sortedanglelist, key=lambda cornerangle: cornerangle["sortangle"])
        #print(sortedanglelist)
        innies = []
        outies = [0,1]
        for sortedcornernum in range(1,len(sortedanglelist)):
            if sortedanglelist[sortedcornernum]["sortangle"] == sortedanglelist[sortedcornernum-1]["sortangle"]:
                x11 = stone[sortedanglelist[sortedcornernum]["cornernum"]]["x"]
                y11 = stone[sortedanglelist[sortedcornernum]["cornernum"]]["y"]
                x12 = stone[sortedanglelist[sortedcornernum-1]["cornernum"]]["x"]
                y12 = stone[sortedanglelist[sortedcornernum-1]["cornernum"]]["y"]
                if dist(x11,Ancor["x"],y11,Ancor["y"]) < dist(x12,Ancor["x"],y12,Ancor["y"]):
                    innies += [sortedcornernum]
                else:
                    innies += [sortedcornernum-1]
        #Algorithm
        nex = 2
        while nex < len(sortedanglelist)-1:
            prev = outies[-2]
            curr = outies[-1]
            nex = curr + 1
            while nex in innies:
                nex += 1
            prevx = stone[sortedanglelist[prev]["cornernum"]]["x"]
            currx = stone[sortedanglelist[curr]["cornernum"]]["x"]
            nexx = stone[sortedanglelist[nex]["cornernum"]]["x"]
            prevy = stone[sortedanglelist[prev]["cornernum"]]["y"]
            curry = stone[sortedanglelist[curr]["cornernum"]]["y"]
            nexy = stone[sortedanglelist[nex]["cornernum"]]["y"]
            
            if is_ccw(prevx,currx,nexx,prevy,curry,nexy) >= 0:
                outies += [nex]
            else:
                innies += [curr]
                outies = outies[:-1]
        for i in innies:
            stone[sortedanglelist[i]["cornernum"]]["hull"] = False
    return file

def filetolist(file):
    global x
    global y
    file = file.readlines()
    letzteZahl = int(file[-1][-1])
    file = [i[0:-1].split() for i in file]
    file = [[int(ii) for ii in i] for i in file]
    file[-1][-1] = file[-1][-1]*10 + letzteZahl
    Anzahl = file[0]
    x = file[-1][0]
    y = file[-1][1]
    file = file[1:-1]
    file = [i[1:] for i in file]
    newfile = []
    for i in file:
        newi = [] 
        for ii in range(0,len(i)):
            if ii%2 == 0:
                newi += [{"x":i[ii],"y":i[ii+1],"distance":99999,"hull":True,"history":[[i[ii],i[ii+1]]]}]
        newfile += [[i for i in newi]]
    file = [i for i in newfile]
    return file

def drawstones():
    for stone in file:
        Lisa.up()
        Lisa.goto(stone[0]["x"],stone[0]["y"])
        Lisa.down()
        for corner in stone:
            Lisa.goto(corner["x"],corner["y"])
            if corner["hull"]:
                Lisa.dot(8,"green")
            else:
                Lisa.dot(8,"red")
        Lisa.goto(stone[0]["x"],stone[0]["y"])

file = filetolist(open("bwnf Lisa rennttxt2.txt"))
file = fakeGrahamScan(file)
#print(file)

def addlastmove(endcorners):
    for corner in endcorners:
        b = corner["x"]
        a = math.tan(alpha)*b
        c = (a**2 + b**2)**0.5
        corner["history"].reverse()
        corner["history"] += [[0,corner["history"][-1][1]+a]]
        corner["distance"] += c
    return endcorners
        
def drawpaths(endcorners):
    for cornerpath in endcorners:
        Mark.up()
        path = cornerpath["history"]
        Mark.goto(path[0][0],path[0][1])
        Mark.down()
        Mark.color("red")
        for corner in path:
            Mark.goto(corner[0],corner[1])

#values
alpha = math.radians(30)

#algorithm
#vorbereitung
endcorners = []
for stone in file:
    for corner in range(0,len(stone)):
        x3 = stone[corner]["x"]
        y3 = stone[corner]["y"]
        x4 = 0
        y4 = math.tan(alpha)*x3 + y3 
        if not allcollisions(x3,x4,y3,y4):
            endcorners += [stone[corner]]

listforlater = []

def run(activecorner,last):
    global listforlater
    global file
    #print(file)
    corner = activecorner["corner"]
    stonenum = -1
    #Mark.goto(corner["x"],corner["y"])
    #Mark.dot(10,"yellow")
    for stone in file:
        stonenum += 1
        corner2num = -1
        for corner2 in stone:
            #Mark.goto(corner2["x"],corner2["y"])
            corner2num += 1
            if couldbereachable(corner["x"],corner["y"],corner2["x"],corner2["y"],activecorner["stonenum"],activecorner["cornernum"],corner["hull"],len(file[activecorner["stonenum"]])-1):
                #Mark.dot(10,"green")
                if corner["distance"] + dist(corner["x"],corner2["x"],corner["y"],corner2["y"]) < corner2["distance"]:
                    if not allcollisions(corner["x"],corner2["x"],corner["y"],corner2["y"]):
                        corner2["distance"] = corner["distance"] + dist(corner["x"],corner2["x"],corner["y"],corner2["y"])
                        #print(corner2["history"],"(",corner2["history"][0],")  + ",corner["history"],"=")
                        corner2["history"] = [corner2["history"][0]] + corner["history"]
                        #print(corner2["history"])
                        listforlater = [i for i in listforlater if i["stonenum"] != stonenum or i["cornernum"] != corner2num]
                        listforlater += [{"stonenum":stonenum,"cornernum":corner2num,"corner":corner2}]
    if last:
        listforlaterlocal = [i for i in listforlater]
        listforlater = []
        #print(listforlaterlocal)
        for i in range(0,len(listforlaterlocal)):
            if i == len(listforlaterlocal)-1:
                run(listforlaterlocal[i],True)
            else:
                run(listforlaterlocal[i],False)

def Lisarennt(endcorners):
    global x
    global y
    rekordwartestrecke = -99999
    for corner in endcorners:
        Busstrecke = corner["history"][-1][1]
        Lisastrecke = corner["distance"]
        wartestrecke = (Lisastrecke - Busstrecke/2)*-1
        if wartestrecke > rekordwartestrecke:
            rekordLisastrecke = Lisastrecke
            rekordwartestrecke = wartestrecke
            rekordhistory = corner["history"]
    
    print("Startzeit: 7:30",rekordwartestrecke/(25/6),"Sekunden")
    print("Zielzeit: 7:30 + ",rekordhistory[-1][1]/(25/3),"Sekunden")
    print("y-koordinate:",rekordhistory[-1][1],"Meter")
    print("Dauer:",rekordLisastrecke/(25/6),"Sekunden")
    print("Länge:",rekordLisastrecke,"Meter")
    print("Weg:", rekordhistory)
    
    if rekordwartestrecke < 0:
        time = rekordwartestrecke/(25/6)
    else:
        time = 0
    t = time

    for corner in rekordhistory:
        if y == corner[1] and x == corner[0]:
            continue
        a = corner[1]-y
        b = corner[0]-x
        c = (a**2+b**2)**0.5
        if a == 0:
            alpha = 180
        else:
            alpha = math.degrees(math.atan(b/a))
        t += c/(25/6)
        x = corner[0]
        y = corner[1]
        #print(recordpath,cords, a,b,c,alpha,tt)
        if a == 0:
            Lisa.setheading(alpha)
        elif a < 0:
            Lisa.setheading(270-alpha)
        else:
            Lisa.setheading(90-alpha)
        while time <= t:
            if time >= rekordwartestrecke/(25/6):
                Lisa.forward(25/6/5)
            if time >= 0:
                Bus.forward(25/3/5)
            time += 0.2

#visualization
screen = Screen()
screen.setworldcoordinates(0, 0, screen.window_width(), screen.window_height())
Bus = Turtle()
Lisa = Turtle()
Mark = Turtle()
Mark.speed(10)
Mark.up()
Lisa.speed(10)
Bus.speed(10)
Bus.setheading(90)
screen.setup (width=0.9999, height=0.9999, startx=0, starty=0)
drawstones()
Lisa.up()
Lisa.goto(x,y)
Lisa.down()

run({"stonenum":-2,"cornernum":-2,"corner":{"x":x,"y":y,"distance":0,"hull":True,"history":[[x,y]]}},True)
#print(endcorners)
endcorners = addlastmove(endcorners)
drawpaths(endcorners)
Lisa.color("green")
Lisarennt(endcorners)
