# In a city-state of n people, there is a rumor going around that one of the n people is a spy for the neighboring city-state.

# The spy, if it exists:
#     Does not trust anyone else.
#     Is trusted by everyone else (he's good at his job).
#     Works alone; there are no other spies in the city-state.

# You are given a list of pairs, trust. Each trust[i] = [a, b] represents the fact that person a trusts person b.
# If the spy exists and can be found, return their identifier. Otherwise, return -1.

# Example 1:
# Input: n = 2, trust = [[1, 2]]
# Output: 2

class Person:
    def __init__(self, id):
        self.id = id
        self.trusts = 0
        self.trusted = 0
    
    def addTrust(self):
        self.trusts = self.trusts + 1
    
    def getTrusts(self):
        return self.trusts
        
    def addTrusted(self):
        self.trusted = self.trusted + 1
    
    def getTrusted(self):
        return self.trusted

def uncover_spy(n, trust):
    people = []
    
    for i in range(n):
        people.append(Person(i + 1))
    
    for trustItem in trust:
        # If this person is on left
        # Add a "trusts" to their class
        # trustItem[0]
        people[trustItem[0] - 1].addTrust()
        
        # Add "trusted" to the right side
        people[trustItem[1] - 1].addTrusted()
    
    # Find anyone with no trusts and n trusteds
    for person in people:
        if person.getTrusts() == 0 and person.getTrusted() == n - 1:
            return person.id
    
    return -1