# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util 
from game import Directions
from typing import List

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()




def tinyMazeSearch(problem: SearchProblem) -> List[Directions]:
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]

def depthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    "*** YOUR CODE HERE ***"


    fringe = util.Stack()#Εφοσον ο αλγοριθμος αναζητησης ειναι DFS το fringe ειναι Stack 
    fringe.__init__()
    fringe.push((problem.getStartState(), [])) #Στο fringe εισαγουμε καθε φορα ενα tuple με 2 στοιχεια , το state και μια λιστα , η οποια θα αποτελειται απο τις ενεργειες που εχουμε κανει για να βρεθουμε στην τρεχουσα κατασταση.                                            
    explored_set = set()                        #Στην συγκεκριμενη περιπτωση δεν εχουμε κανει καποια ενεργεια αρα η λιστα ειναι κενη. Το explored_set θα ειναι ενα set στο οποιο θα βαζουμε τις καταστασεις τις οποιες εχουμε επισκευτει, και θα ελεγχουμε εαν μια κατασταση βρισκεται μεσα σε αυτο σε χρονο O(1)

    if problem.isGoalState(problem.getStartState()) :#Ελεγχουμε εαν η αρχικη κατασταση ειναι κατασταση στοχου, εαν ειναι τοτε επιστρεφουμε μια αδεια λιστα
        return []

    while(fringe.isEmpty()==False):#Οσο το fringe δεν ειναι αδειο

        state , moves = fringe.pop()#Κανουμε pop το tuple απο το stack και περνουμε την κατασταση και τις ενεργειες που εχουμε κανει για να φτασουμε εκει 

        if(problem.isGoalState(state) == True):#Εαν ειναι κατασταση στοχου τοτε επιστρεφουμε την λιστα με τις ενεργειες
            return moves

        if state not in explored_set:#Εαν η κατασταση δεν ειναι στο explored_set
            explored_set.add(state) #Την εισαγουμε 
            for successor , action , cost in problem.getSuccessors(state) : #Με την getSuccesors περνουμε ολες τις τριπλετες τις μορφης successor,action , cost
                if successor not in explored_set:#Ελεγχουμε εαν το successor ειναι στο explored_set , εαν ειναι τοτε δεν το ξαναεισαγουμε αλλιως 
                    new_actions = moves + [action] #Οι ενεργειες για να φτασουμε στον successor ειναι αυτες που καναμε για να φτασουμε στο current state + την ενεργεια για να παμε απο το current_state στο successor
                    fringe.push((successor , new_actions))  #Εισαγουμε το tuple στο fringe

    return []#Εαν δεν εχει βρεθει μονοπατι τοτε επιστρεφουμε αδεια λιστα 
    util.raiseNotDefined()

def breadthFirstSearch(problem: SearchProblem) -> List[Directions]:
    """Search the shallowest nodes in the search tree first."""
    "*** YOUR CODE HERE ***"
    fringe = util.Queue()#Εφοσον ο αλγοριθμος αναζητησης ειναι BFS το fringe ειναι Ουρα 
    fringe.__init__()
    fringe.push((problem.getStartState() , []))#Οπως στο DFS εισαγουμε στην ουρα ενα tuple με δυο στοιχεια , το state και μια λιστα ενεργειων 
    explored_set = set()

    if problem.isGoalState(problem.getStartState()) :#Εαν η αρχικη κατασταση ειναι κατασταση στοχου τοτε επιστρεφουμε μια αδεια λιστα
        return []

    while(fringe.isEmpty() == False):#Οσο η ουρα δεν ειναι αδεια
        state , moves = fringe.pop()#Βγαζουμε το πρωτο tuple της ουρας και περνουμε το state και τις ενεργειες που καναμε για να φτασουμε εκει

        if problem.isGoalState(state):#Εαν η κατασταση που βρισκομαστε ειναι κατασταση στοχου τοτε επιστρεφουμε την λιστα ενεργειων 
            return moves

        if state not in explored_set:#Εαν δεν εχουμε κανει explore την κατασταση τοτε
            explored_set.add(state)#την εισαγουμε στο set
            for successor , action , cost in problem.getSuccessors(state):#Περνουμε τους successors την ενεργεια για να παμε στον καθε ενα και το κοστος 
                if successor not in explored_set:#Εαν δεν ειναι ειδη στο set τοτε υπολογιζουμε την καινουργια λιστα ενεργειων για τον καθε successor , η οποια θα αποτελειται απο τις κινησεις που καναμε για να φτασουμε στο state μαζι με το action για να παμε στον successor
                    new_actions = moves + [action]
                    fringe.push((successor , new_actions))#Εισαγουμε το tuple στο fringe
    
    return []#Εαν δεν κανουμε reach το goal επιστρεφουμε αδεια λιστα ενεργειων 
    util.raiseNotDefined()

def uniformCostSearch(problem: SearchProblem) -> List[Directions]:
    """Search the node of least total cost first."""
    "*** YOUR CODE HERE ***"
    
    fringe = util.PriorityQueue()#Χρησιμοποιουμε PQ γιατι θελουμε να διαταζουμε τους κομβους αναλογα με τα κοστοι τους . 
    fringe.__init__()

    fringe.push( (problem.getStartState() , [] , 0) , 0  )#Στο PQ θα εισαγουμε ενα tuple το οποιο θα αποτελειται απο την τρεχουσα κατασταση , την λιστα ενεργειων και το κοστος του μονοπατιου (για το start state ειναι 0) 
    explored_set = set()#Προκειμενου να γινεται η ταξινομιση των κομβων μεσα στο PQ θα εισαγουμε εκτος απο το tuple , για δευτερη φορα το κοστος του μονοπατιου. 
    
    if problem.isGoalState(problem.getStartState()) : #Ελεγχος για το εαν το start_state ειναι goal_state
        return []

    while (fringe.isEmpty() == False):#Οσο το fringe δεν ειναι αδειο
        state , moves , path_cost = fringe.pop()#Βγαζουμε την κατασταση που για να παμε σε αυτη εχουμε το λιγοτερο κοστος  , και μαζι με αυτη περνουμε και την λιστα ενεργειων καθως και το κοστος 
        
        if problem.isGoalState(state) : #Εαν ειναι κατασταση στοχου επιστρεφουμε την λιστα ενεργειων 
            return moves
        
        if state not in explored_set:#Εαν δεν ειναι στο set 
            explored_set.add(state)#την εισαγουμε
            for successor , actions , cost in problem.getSuccessors(state):#Περνουμε τον καθε succesor , το action που αντιστοιχει και το κοστος μονοπατιου για να παμε σε αυτο 
                new_actions = moves + [actions]#Δημιουργουμε την λιστα ενεργειων του successor
                fringe.update((successor , new_actions , path_cost + cost) , path_cost + cost)#Προκειμενου να εισαγουμε τον successor στο fringe με κοστος μονοπατιου το κοστος για να παμε στο state + τοτε κοστος για να παμε απο το state στο successor , χρησιμοποιουμε την συναρτηση update , η οποια εαν δει οτι ο successor υπαρχει ειδη μεσα στο pq αλλα με μεγαλυτερο κοστος απο αυτο που μολις υπολογισαμε , τοτε τον ενημερωνει με το καινουργιο κοστος και το καινουργιο μονοπατι προς αυτον.
                #ΑΛλιως εαν δεν υπαρχει ο successor μεσα στο fringe τοτε η update θα τον εισαγει κανονικα , ή εαν υπαρχει αλλα εχει μικροτερο ή ισο κοστος απο αυτο που υπολογισαμε τοτε δεν θα τον εισαγει καθολου.
                    
    return []#Εαν δεν βρεθει το goal_state τοτε επιστρεφουμε αδεια λιστα ενεργειων
    util.raiseNotDefined()

def nullHeuristic(state, problem=None) -> float:
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem: SearchProblem, heuristic=nullHeuristic) -> List[Directions]:
    """Search the node that has the lowest combined cost and heuristic first."""
    "*** YOUR CODE HERE ***"

    fringe = util.PriorityQueue()#Παλι το fringe ειναι PQ
    fringe.__init__() 
    f_cost = heuristic(problem.getStartState() , problem)
    g_cost = 0   
    fringe.push((problem.getStartState() , [] , f_cost) , f_cost )#Στο fringe εισαγουμε ενα tuple με στοιχεια το state , το action list , το κοστος f του state και ως στοιχειο συγκρισης των στοιχειων κατα την εισαγωγη τους στο PQ χρησιμοποιουμε και παλι το f_cost
    explored_set = set()#Για το start state το κοστος f ειναι απλος το h καθως το g = 0
    G_costs = {}#Επισης χρησιμοποιω και ενα dictionary στο οποιο κανω την αντιστοιχιση καταστασης με το αντιστοιχο g_cost

    G_costs[problem.getStartState()] = g_cost

    if(problem.isGoalState(problem.getStartState())):
        return []
    
    while (fringe.isEmpty() == False) :#Οσο το fringe δεν ειναι αδειο 

        state , moves , f_cost  = fringe.pop() #Βγαζουμε την κατασταση με το μικροτερο f απο το fringe και μαζι με αυτην παιρνουμε το action list και το κοστος f του state
        if problem.isGoalState(state) :#Εαν ειναι κατασταση στοχου τοτε επιστρεφουμε την λιστα ενεργειων 
            return moves 
        
        if state not in explored_set:#Αν δεν ειναι στο set τοτε το εισαγουμε 
            explored_set.add(state)
            for successor , action , cost in problem.getSuccessors(state): #Παιρνουμε το successor state , το action για να παμε σε αυτο και το κοστος μονοπατιου
                h_cost = heuristic(successor , problem)#Υπολογιζουμε το κοστος h του successor μεσω της συναρτησης heuristic
                g_cost = G_costs[state] + cost #Το g_cost του succesor θα ειναι το κοστος g για να παμε μεχρι το state(το οποιο το παιρνουμε απο το dictionary) + το κοστος μονοπατιου για να παμε απο το state στο succesor
                f_cost = h_cost + g_cost #To f_cost ειναι το αθροισμα του g και του h 
                new_actions = moves + [action]#Φτιαχνουμε την καινουργια λιστα ενεργειων 
                if successor not in G_costs: #Εαν δεν εχουμε ειδη εισαγει το κοστος g του successor στο dictionary, σημαινει οτι τον επισκευτομαστε πρωτη φορα  οποτε το εισαγουμε 
                    G_costs[successor] =  g_cost
                else:#Αλλιως εαν το κοστος g που ειχαμε υπολογισει για να παμε σε αυτο απο καποιο αλλο μονοπατι , μαζι με το h ειναι μεγαλυτερο απο το f που μολις υπολογισαμε τοτε
                    if G_costs[successor] + heuristic(successor , problem) > f_cost :
                        G_costs[successor] = g_cost#Ενημερωνουμε την τιμη του g_cost στο dictionary
                        if successor in explored_set:#Εαν ειναι στο explored_set τοτε τον βγαζουμε για να μπορουμε να τον ξαναεξετασουμε αφου βρικαμε καλυτερο μονοπατι προς αυτον.
                            explored_set.remove(successor)
                fringe.update((successor ,new_actions , f_cost) , f_cost)#Τελος μεσω της update εισαγουμε τον successor στο frontier εφοσον δεν υπαρχει ειδη μεσα , αλλιως εαν υπαρχει και το κοστος f  ειναι μεγαλυτερο απο αυτο που μολις υπολογισαμε , σημαινει οτι βρικαμε καλυτερο μονοπατι προς αυτον ,αρα τον ενημερωνουμε . Εαν υπαρχει ειδη μεσα αλλα εχει μικροτερο ή ισο f απο αυτο που βρικαμε τοτε δεν το ξαναεισαγουμε
                
    return []#Επιστρεφουμε αδεια λιστα εαν δεν φτασουμε στο goal
    util.raiseNotDefined()

# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
