class Thing:
    '''Fields: id (Nat),
               name (Str),
               description (Str)
    '''
    
    def __init__(self, id):
        self.id = id
        self.name = '???'
        self.description = ''
        
    def __repr__(self):
        return '<thing #{0}: {1}>'.format(self.id, self.name)
        
    def look(self):
        print(self.name)
        print(self.description)
        
class Player:
    '''Fields: id (Nat),
               name (Str), 
               description (Str),
               location (Room),
               inventory ((listof Thing))
    '''
    
    def __init__(self, id):
        self.id = id
        self.name = '???'
        self.description = ''
        self.location = None
        self.inventory = []
        
    def __repr__(self):
        return '<player #{0}: {1}>'.format(self.id, self.name)
        
    def look(self):
        print(self.name)
        print(self.description)
        if len(self.inventory) != 0:
            print('Carrying: {0}.'.format(
                ', '.join(map(lambda x: x.name,self.inventory))))
 
class Room:
    '''Fields: id (Nat),
               name (Str), 
               description (Str),
               contents ((listof Thing)),
               exits ((listof Exit))
    '''    
    
    def __init__(self, id):
        self.id = id
        self.name = '???'
        self.description = ''
        self.contents = []
        self.exits = []
        
    def __repr__(self):
        return '<room {0}: {1}>'.format(self.id, self.name)
        
    def look(self):
        print(self.name)
        print(self.description)
        if len(self.contents) != 0:
            print('Contents: {0}.'.format(
                ', '.join(map(lambda x: x.name, self.contents))))
        if len(self.exits) != 0:
            print('Exits: {0}.'.format(
                ', '.join(map(lambda x: x.name, self.exits)))) 
 
class Exit:
    '''Fields: name (Str), 
               destination (Room)
               key (Thing)
               message (Str)
    '''       
    
    def __init__(self,name,dest):
        self.name = name
        self.destination = dest
        self.key = None
        self.message = ''
        
    def __repr__(self):
        return '<exit {0}>'.format(self.name)

class World:
    '''Fields: rooms ((listof Room)), 
               player (Player)
    '''       
    
    msg_look_fail = "You don't see that here."
    msg_no_inventory = "You aren't carrying anything."
    msg_take_succ = "Taken."
    msg_take_fail = "You can't take that."
    msg_drop_succ = "Dropped."
    msg_drop_fail = "You aren't carrying that."
    msg_go_fail = "You can't go that way."
    
    msg_quit = "Goodbye."
    msg_verb_fail = "I don't understand that."
    
    def __init__(self, rooms, player):
        self.rooms = rooms
        self.player = player

    def look(self, noun):
        '''
        Accepts a noun argument, giving the name of the thing the user wants 
        to look at, & doesn’t return anything & prints the name & description 
        of the passed-in noun based on the requirements given.
        Effects: Prints the self name & description of the passed-in noun
        
        look: World Str -> None
        '''
        if noun== 'me':
            self.player.look()
            return None
        elif noun=='here':
            self.player.location.look()
            return None 
        for items in self.player.inventory:
            if noun == items.name:
                items.look() 
                return None
        for things_holder in self.player.location.contents:
            if noun == things_holder.name:
                things_holder.look()
                return None
        else:
            print(self.msg_look_fail)
     
    def inventory(self):
        '''
        Inventory doesn't take any arguments (other than self) & doesn’t return
        anything. However, it does print a formatted list of the names of the 
        things that the player is currently carrying or not carrying in  
        format given in the assignment.
        Effects: A message is printed either with an error or with inventory
        and the list of things in the inventory
        
        inventory: World -> None
        '''
        if self.player.inventory== []:
            print(self.msg_drop_fail) 
        else:
            print('Inventory: {0}'.format(', '.join(map(lambda element: 
                                        element.name,self.player.inventory))))
            
    def take(self, noun):
        '''
        Accepts noun argument, telling the name of the thing to pick up, & 
        doesn’t return anything. If the noun is in the thing of the player’s 
        current room, World is mutated by removing thing from room’s contents & 
        appending to the player’s inventory & printed "Taken.". If no such thing 
        is found in  player’s room, "You can’t take that." is printed
        
        Effects: Mutates the self if name is in thing, and prints "Taken" or
        else prints "You can’t take that."
        
        take: World Str -> None
        '''
        for objects in self.player.location.contents:
            if noun == objects.name: 
                self.player.location.contents.remove(objects)
                self.player.inventory.append(objects)
                print(self.msg_take_succ)
                return None
        print(self.msg_take_fail) 
          
    def drop(self, noun):
        '''
        Accepts a noun giving the name of the thing to put down, & doesn’t 
        return anything. If the noun is in the thing of the player’s inventory,
        World is mutated by removing thing from inventory & appended to contents
        of the player’s current room. "Dropped." is printed. If nothing is found 
        in the player’s inventory,"You aren’t carrying that." is printed
        
        Effects: Mutates the self if name is in thing, and prints "Dropped." or
        else prints "You aren’t carrying that."
        
        drop: World Str -> None
        
        '''
        for items in self.player.inventory:
            if items.name == noun: 
                self.player.inventory.remove(items)
                self.player.location.contents.append(items)
                print(self.msg_drop_succ)
                return None
        print(self.msg_drop_fail)
        
    def go(self, noun):
        '''
        Accepts a noun giving the name of the exit to go through, & doesn’t 
        return anything. If the noun is in the name of one of the exits in the 
        player’s current room, contents of the world are muated as defied in the
        assignment or else  prints "You can’t go that way."
        
        Effects: Mutates the self if name is in thing, or else prints "You can’t 
        go that way."
        
        go: World Str -> None
        
        '''
        for places in self.player.location.exits:
            if noun == places.name:
                if places.key == None:
                    self.player.location = places.destination
                    self.player.location.look() 
                    return None
                else:
                    if places.key in self.player.inventory:
                        self.player.location = places.destination
                        self.player.location.look()
                        return None
                    else:
                        print(places.message)
                        return None              
        print(self.msg_go_fail)
                
    def play(self):
        player = self.player
        
        player.location.look()
        
        while True:
            line = input( "- " )
            
            wds = line.split()
            verb = wds[0]
            noun = ' '.join( wds[1:] )
            
            if verb == 'quit':
                print( self.msg_quit )
                return
            elif verb == 'look':
                if len(noun) > 0:
                    self.look(noun)  
                else:
                    self.look('here')
            elif verb == 'inventory':
                self.inventory()     
            elif verb == 'take':
                self.take(noun)    
            elif verb == 'drop':
                self.drop(noun)
            elif verb == 'go':
                self.go(noun)   
            else:
                print( self.msg_verb_fail )

    ## Q3
    def save(self, fname):
        '''
        Reads a single file, fname, and saves a game in a new state in form of 
        a text file, after a user plays the game for a while, while the World is
        getting mutated. The user can later resume back to the game after saving
        the file. The file is saved in the same format described for loading as
        given in the assignment.
        
        Effects: Reads the file fname, and saves the mutated World in the form 
        of a text file as the user plays the game
        
        save: World Str -> None
        
        '''
        f = open(fname,"w")
        room_in = self.rooms
        inventory = self.player.inventory
        for item in inventory:
            f.write("thing #{0} {1}\n".format(item.id, item.name))
            f.write(item.description + "\n")
        for each_room in room_in:
            thing_1 = each_room.contents
            for object in thing_1:
                f.write("thing #{0} {1}\n".format(object.id, object.name))
                f.write(object.description + "\n")
        for indroom in room_in:
            f.write("room #{0} {1}\n".format(indroom.id, indroom.name))
            f.write(indroom.description + "\n")   
            contents = ''
            for content in indroom.contents:
                contents = contents + "#" + str(content.id) + ''
            f.write("contents " + contents + "\n")
        player = self.player
        f.write("player #{0} {1}\n".format(player.id,player.name))
        f.write(player.description + "\n")
        items = ''
        for item in player.inventory:
            items = items + "#" + str(item.id) + " "
        f.write("inventory " + items + "\n")
        location = self.player.location
        f.write("location #{0}\n".format(location.id))
        exit = self.rooms
        gate = ''
        for new_exit in exit:
            each_exit = new_exit.exits
            for one_exit in each_exit:
                if one_exit.key == None:
                    gate = "#" + str(new_exit.id) + " #" + \
                        str(one_exit.destination.id) + " " + str(one_exit.name)  
                    f.write("exit " + gate + "\n")
                else:
                    gate2 = "#" + str(new_exit.id) + " #" + \
                            str(one_exit.destination.id) + " " +\
                            str(one_exit.name)  
                    f.write("keyexit " + gate2 + "\n" + str(one_exit.message) \
                            + "\n")                    
        f.close()         
              

# Q2
def load(fname):
    '''
    Reads the name of a text file, fname and returns a World constructed from 
    the information in the text file following the instruction as stated in the 
    assignment
    
    Effects: Reads the file fname and mutates players,exits, thing and rooms as 
    per the instructions
    
    load: Str -> None
    
    '''
    f = open(fname ,"r")
    lines = f.readline()
    rooms = [] 
    things_holder = []
    while lines != "":
        lst = lines.split()
        if lst[0] == "room":
            room = Room(int(lst[1][1:]))
            room.name = " ".join(lst[2:])
            room.description = f.readline()[:-1]
            contents = f.readline()
            contents = list(map(lambda x: int(x[1:]), contents.split()[1:]))
            objects = []
            for material in things_holder:
                if material.id in contents:
                    objects.append(material)
            room.contents = objects
            room.exits = []
            rooms.append(room)
        elif lst[0] == "thing":
            thing = Thing(int(lst[1][1:])) 
            thing.name = " ".join(lst[2:])
            thing.description = f.readline()[:-1]
            things_holder.append(thing)
        elif lst[0] == "player":
            player = Player(int(lst[1][1:])) 
            player.name = " ".join(lst[2:])
            player.description = f.readline()[:-1]
            inventory = f.readline()
            inventory = list(map(lambda m: int(m[1:]), inventory.split()[1:]))
            objects = []
            for applications in things_holder:
                if applications.id in inventory:
                    objects.append(applications)
            player.inventory = objects
            location = f.readline()
            location = int(location.split()[1][1:])
            for ind_room in rooms:
                if ind_room.id == location:
                    player.location = ind_room
        elif lst[0] == "exit":
            for avail_room in rooms:
                if avail_room.id == int(lst[1][1:]):
                    for exit_room in rooms:
                        if exit_room.id == int(lst[2][1:]):
                            avail_room.exits.append(Exit(" ".join(lst[3:]),
                                                         exit_room)) 
        elif lst[0] == 'keyexit':
                    for new_room in rooms:
                        if new_room.id == int(lst[1][1:]):
                            for exit_room in rooms:
                                if exit_room.id == int(lst[2][1:]): 
                                    new_room.exits.append(Exit(" ".join(lst[3:]),
                                                               exit_room))
                            the_description = f.readline()
                            new_room.exits[-1].message = \
                                the_description[2:-1].strip()
                            the_desciption = the_description.split()
                            for items in things_holder:
                                if items.id == int(the_desciption[0][1:]):
                                    new_room.exits[-1].key = items
        lines = f.readline()
    f.close()
    return World(rooms,player)
                    
    

def makeTestWorld(usekey):
    wallet = Thing(1)
    wallet.name = 'wallet'
    wallet.description = 'A black leather wallet containing a WatCard.'
    
    keys = Thing(2)
    keys.name = 'keys'
    keys.description = 'A metal keyring holding a number of office and home keys.'
    
    phone = Thing(3)
    phone.name = 'phone'
    phone.description = 'A late-model smartphone in a Hello Kitty protective case.'
    
    coffee = Thing(4)
    coffee.name = 'cup of coffee'
    coffee.description = 'A steaming cup of black coffee.'
    
    hallway = Room(5)
    hallway.name = 'Hallway'
    hallway.description = 'You are in the hallway of a university building. \
Students are coming and going every which way.'
    
    c_and_d = Room(6)
    c_and_d.name = 'Coffee Shop'
    c_and_d.description = 'You are in the student-run coffee shop. Your mouth \
waters as you scan the room, seeing many fine foodstuffs available for purchase.'
    
    classroom = Room(7)
    classroom.name = 'Classroom'
    classroom.description = 'You are in a nondescript university classroom. \
Students sit in rows at tables, pointedly ignoring the professor, who\'s \
shouting and waving his arms about at the front of the room.'
    
    player = Player(8)
    player.name = 'Stu Dent'
    player.description = 'Stu Dent is an undergraduate Math student at the \
University of Waterloo, who is excelling at this studies despite the fact that \
his name is a terrible pun.'
    
    c_and_d.contents.append(coffee)
    player.inventory.extend([wallet,keys,phone])
    player.location = hallway
    
    hallway.exits.append(Exit('shop', c_and_d))
    ex = Exit('west', classroom)
    if usekey:
        ex.key = coffee
        ex.message = 'On second thought, it might be better to grab a \
cup of coffee before heading to class.'
    hallway.exits.append(ex)
    c_and_d.exits.append(Exit('hall', hallway))
    classroom.exits.append(Exit('hall', hallway))
    
    return World([hallway,c_and_d,classroom], player)

testworld = makeTestWorld(False)
testworld_key = makeTestWorld(True)