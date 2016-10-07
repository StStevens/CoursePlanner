'''
Created on Oct 4, 2016

@author: Nick
'''

class Course(object):
    '''
    Represents a course.
    '''
    def __init__(self, shortName, fullName, units, prereq, description=None):
        self.shortName = shortName
        self.fullName = fullName
        self.units = units
        self.prereq = prereq
        self.description = description

def parsePreReq(prereqs: str)-> tuple: #Make this recursive
    baseReqs = prereqs.replace("(", "( ")
    baseReqs = baseReqs.replace(")", " )")
    tokens = baseReqs.split(" ")[1:]
    requirements, _ = reqParse(tokens)
    return requirements

def reqParse(tokens, start=0):
    requirement = Requirement([])
    shortName = []
    place = start
    while place < len(tokens):
        token = tokens[place]
        if token[0] == '(':
            grouping, newPlace = reqParse(tokens, place+1)
            requirement.addRequirement(grouping)
            place = newPlace
        elif token[-1] == ')':
            if shortName != []:
                requirement.addRequirement(" ".join(shortName))
            return(requirement, place)
        elif token == 'or' or token =='and':
            requirement.setOperator(token)
            if shortName != []:
                requirement.addRequirement(" ".join(shortName))
            shortName = []
        else:
            shortName.append(token)
        place += 1
    return (requirement, place)

    
class Requirement():
    def __init__(self, courses = [], operator=None):
        self.courses = courses
        self.operator = operator
    
    def addRequirement(self, requirement):
        self.courses.append(requirement)
    
    def setOperator(self, operator):
        self.operator = operator
        

if __name__ == "__main__":
    testText = 'Requirements: (IN4MATX 45 or I&C SCI 46 or CSE 46 or ((I&C SCI 33 or CSE 43) and I&C SCI 45J)) and (STATS 7 or STATS 67).'
    result, _ = parsePreReq(testText)
    print (result.courses)
    test = 1