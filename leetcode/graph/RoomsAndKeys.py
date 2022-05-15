'''
Given a list of rooms (roomList) and each room has n keys
Find out if it is possible to travel to all rooms in given that you
start out in the first room
'''

'''
Example:

roomList = [[1,2],[3],[3],[0]]
Output = True

roomList = [[1],[3],[4],[0]]
Output = False
'''

#This function will return whether we can move to every room in the list
#Staring from the zero indexed room
'''
#Time Complexity: O(V+E) V is the rooms in the rooms list and E are the keys in each room
#Space Complexity: O(V) which is a travelled list to keep track of things we've visited

'''

def connectRooms(rooms)->bool:

    #Iterate preprocessing to determine what rooms beginning
    #should be travelled true or False empty rooms are always true
    travelled = []
    for i in range(len(rooms)):
        if len(rooms[i]) != 0:
            travelled.append(False)
        else:
            travelled.append(True)
    
    q = []
    q.append([rooms[0], 0])

    while q:
        keys, currentRoom = q.pop(0)
        for i in range(0, len(keys)):

            #if key is bigger than than the rooms in the list then ignore
            if keys[i] > len(rooms) - 1:
                continue
            
            if keys[i] != currentRoom and travelled[keys[i]] == False:
                q.append([rooms[keys[i]], keys[i]])
                travelled[keys[i]] = True

    return True if False not in travelled else False

def main () -> bool:
    rooms = [[1,2],[0],[3,4],[0]]
    return connectRooms(rooms)

print(main())