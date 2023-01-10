#
# board.py (Final project)
#
# A Board class for the Eight Puzzle
#
# name: Peiyang Liu
# email: nickpliu@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

# a 2-D list that corresponds to the tiles in the goal state
GOAL_TILES = [['0', '1', '2'],
              ['3', '4', '5'],
              ['6', '7', '8']]

class Board:
    """ A class for objects that represent an Eight Puzzle board.
    """
    def __init__(self, digitstr):
        """ a constructor for a Board object whose configuration
            is specified by the input digitstr
            input: digitstr is a permutation of the digits 0-9
        """
        # check that digitstr is 9-character string
        # containing all digits from 0-9
        assert(len(digitstr) == 9)
        for x in range(9):
            assert(str(x) in digitstr)

        self.tiles = [[''] * 3 for x in range(3)]
        self.blank_r = -1
        self.blank_c = -1

        # Put your code for the rest of __init__ below.
        # Do *NOT* remove our code above.
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                self.tiles[r][c] = digitstr[3*r+c]
                if self.tiles[r][c] == '0':
                    self.blank_r = r
                    self.blank_c = c
                

    ### Add your other method definitions below. ###
    
    
    def __repr__(self):
        """rewrite the __repr__ method"""
        
        s = ''
        s2 = ''
        
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c] == '0':
                    s2 = '_'
                else:
                    s2 = self.tiles[r][c]
                if (c+1)%3 == 0:
                    s += s2+' \n'
                else:
                    s += s2+' '                
        return s
    
    
    def move_blank(self, direction):
        """ move the blank, return Flase if the move was not possible"""
        a = ''
        if direction == 'up':
            if self.blank_r == 0:
                return False
            else:
                a = self.tiles[self.blank_r-1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = a
                self.tiles[self.blank_r-1][self.blank_c] = '0'
                self.blank_r -=1
                return True
                
        if direction == 'down':
            if self.blank_r == 2:
                return False
            else:
                a = self.tiles[self.blank_r+1][self.blank_c]
                self.tiles[self.blank_r][self.blank_c] = a
                self.tiles[self.blank_r+1][self.blank_c] = '0'
                self.blank_r +=1
                return True
        
        if direction == 'right':
            if self.blank_c == 2:
                return False
            else:
                a = self.tiles[self.blank_r][self.blank_c+1]
                self.tiles[self.blank_r][self.blank_c] = a
                self.tiles[self.blank_r][self.blank_c+1] = '0'
                self.blank_c +=1
                return True
        
        if direction == 'left':
            if self.blank_c == 0:
                return False
            else:
                a = self.tiles[self.blank_r][self.blank_c-1]
                self.tiles[self.blank_r][self.blank_c] = a
                self.tiles[self.blank_r][self.blank_c-1] = '0'
                self.blank_c -=1
                return True
        else:
            return False
    
    
    def digit_string(self):
        """ creates and returns a string of digits that corresponds to the 
        current contents of the called Board object’s tiles attribute"""
        s = ''
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                s += self.tiles[r][c]
 
        return s
    
    def copy(self):
        """returns a newly-constructed Board object that is a deep 
        copy of the called object"""
        return Board(self.digit_string())
    
    
    def num_misplaced(self):
        """counts and returns the number of tiles in the called Board object 
        that are not where they should be in the goal state"""
        count = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])):
                if self.tiles[r][c]!='0' and self.tiles[r][c]!=GOAL_TILES[r][c]:
                        count+=1
        return count   
    
    
    def  __eq__(self, other):
        """the == operator is used to compare two Board objects"""
        if self.tiles == other.tiles:
            return True
        else:
            return False
        
        
        


    
    def distance(self):
        """return the avg of differences between actual value and the goal
            value in each postion"""
            
        sum_diff = 0
        for r in range(len(self.tiles)):
            for c in range(len(self.tiles[0])): 
                if self.tiles[r][c]!='0' and self.tiles[r][c]!=GOAL_TILES[r][c]:
                    diff = abs(int(GOAL_TILES[r][c])-int(self.tiles[r][c]))
                    sum_diff += diff
                    
        if self.num_misplaced()!=0:
            return sum_diff/self.num_misplaced()
        else:
            return 0
    
  
            
                
    


    
    
    
    
    
    
    
    
    
    
