#
# searcher.py (Final project)
#
# classes for objects that perform state-space search on Eight Puzzles  
#
# name: Peiyang Liu 
# email: nickpliu@bu.edu
#
# If you worked with a partner, put their contact info below:
# partner's name:
# partner's email:
#

import random
from state import *

class Searcher:
    """ A class for objects that perform random state-space
        search on an Eight Puzzle.
        This will also be used as a superclass of classes for
        other state-space search algorithms.
    """
    ### Add your Searcher method definitions here. ###
    def __init__(self, depth_limit):
        """a constructor for a Searcher object"""
        self.states = []
        self.num_tested = 0
        self.depth_limit = depth_limit


    def __repr__(self):
        """ returns a string representation of the Searcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        if self.depth_limit == -1:
            s += 'no depth limit'
        else:
            s += 'depth limit = ' + str(self.depth_limit)
        return s
    
    
    def add_state(self, new_state):
        """add new state into states list """
        self.states += [new_state]
        
        
    
    def should_add(self, state):
        """eturns True if the called Searcher should add state to its list of 
        untested states, and False otherwise"""
        if self.depth_limit != -1 and state.num_moves > self.depth_limit:
            return False
        elif state.creates_cycle() == True:
            return False
        else:
            return True
         
            
    def add_states(self, new_states):
        """ takes a list State objects called new_states, and that processes
        the elements of new_states one at a time"""
        for s in new_states:
            if self.should_add(s) == True:
                self.add_state(s)
                
    
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, removing it from the list and returning it
        """
        s = random.choice(self.states)
        self.states.remove(s)
        return s
    
    
    def find_solution(self, init_state):
        """performs a full state-space search that begins at the specified 
        initial state init_state and ends when the goal state is found or when 
        the Searcher runs out of untested states"""
        self.add_state(init_state)
        while self.states != []:
            self.num_tested += 1
            s = self.next_state()
            if s.is_goal() == True:
                return s
            else:
                self.add_states(s.generate_successors())
            
        return None
        

### Add your BFSearcher and DFSearcher class definitions below. ###
class BFSearcher(Searcher):
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, remove the chosen state from the list of untested 
        states before returning it.
        """
        s = self.states[0]
        for i in self.states:
            if i.num_moves < s.num_moves:
                s = i
        self.states.remove(s)
        return s
    
class DFSearcher(Searcher):
    def next_state(self):
        """ chooses the next state to be tested from the list of 
        untested states, remove the chosen state from the list of untested 
        states before returning it.
        """
        s = self.states[-1]
        for i in self.states:
            if i.num_moves > s.num_moves:
                s = i
        self.states.remove(s)
        return s

def h0(state):
    """ a heuristic function that always returns 0 """
    return 0

### Add your other heuristic functions here. ###

def h1(state):
    """computes and returns an estimate of how many additional moves are needed
    to get from state to the goal state"""
    num = state.board.num_misplaced()
    return num

def h2(state):
    """a heuristic function that depends on the sum of abs differences between 
    actual value and the goal value in each postion"""
    num = state.board.distance()
    return num
    
    
    

class GreedySearcher(Searcher):
    """ A class for objects that perform an informed greedy state-space
        search on an Eight Puzzle.
    """
    ### Add your GreedySearcher method definitions here. ###
    def  __init__(self, heuristic):
        super().__init__(depth_limit = -1)
        self.heuristic = heuristic
        
        
        
    def __repr__(self):
        """ returns a string representation of the GreedySearcher object
            referred to by self.
        """
        # You should *NOT* change this method.
        s = type(self).__name__ + ': '
        s += str(len(self.states)) + ' untested, '
        s += str(self.num_tested) + ' tested, '
        s += 'heuristic ' + self.heuristic.__name__
        return s
    
    
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * self.heuristic(state)
    
    
    def add_state(self, state):
        """ add a sublist that is a [priority, state] pair, where priority is 
        the priority of state that is determined by calling the priority method"""
        self.states += [[self.priority(state),state]]
        
        
    def next_state(self):
        """ choose one of the states with the highest priority"""
        maxs = max(self.states)
        s = maxs[1]
        self.states.remove(maxs)
        return s
        


### Add your AStarSeacher class definition below. ###
class AStarSearcher(GreedySearcher):
    """ A class for objects that perform an perform A* search on an 
        Eight Puzzle.
    """
    
    def priority(self, state):
        """ computes and returns the priority of the specified state,
        based on the heuristic function used by the searcher
        """
        return -1 * (self.heuristic(state) + state.num_moves)
    
