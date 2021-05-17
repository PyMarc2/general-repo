import itertools
from copy import deepcopy

class Person:
    def __init__(self, name=None, choiceList=None):
        self.name = name
        self.choiceList = choiceList
        self.givenChoice = None

    def set_name(self, name: str):
        self.name = name

    def add_choice(self, choice: int):
        self.choiceList.append(choice)

    def set_choiceList(self, choices: list):
        self.choiceList = choices

    def set_givenChoice(self, given: int):
        self.givenChoice = given


class GroupChoiceOptimizer:
    def __init__(self, target="min", choiceList=[], personList=[]):
        self.choiceList = choiceList
        self.target = target
        self.personList = personList
        self.optimalChoiceList = []
        self.lowestSum = len(self.choiceList)**2
        self.solutionIndex = 0

    def add_person(self, person: Person):
        self.personList.append(person)

    def generate_person(self, name, choiceList):
        self.personList.append(Person(name, choiceList))

    def optimize_given_choice(self):
        permutations = list(itertools.permutations(self.choiceList))
        self.optimalChoiceList = []
        sumList = []

        if self.personList:
            for c in permutations:
                indexes = [self.personList[i].choiceList.index(c[i]) for i in range(len(self.personList))]
                sumList.append(sum(indexes))

                if sumList[-1] < self.lowestSum:
                    self.lowestSum = sumList[-1]

            for v, s in enumerate(sumList):
                if s == self.lowestSum:
                    self.optimalChoiceList.append(list(permutations[v]))

        matrix = deepcopy([[n.name for n in self.personList], self.optimalChoiceList[self.solutionIndex],
                  [self.personList[i].choiceList.index(self.optimalChoiceList[self.solutionIndex][i]) + 1 for i in
                   range(len(self.personList))]])
        matrix[0].insert(0, "")
        matrix[1].insert(0, "choice")
        matrix[2].insert(0, "rank")
        self.pretty_print_matrix(matrix)

        print("Other equivalents ranks:")
        matrix = deepcopy([[self.personList[i].choiceList.index(self.optimalChoiceList[v][i]) + 1 for i in range(len(self.personList))] for v in range(len(self.optimalChoiceList))])
        matrix.insert(0, [n.name for n in self.personList])

        self.pretty_print_matrix(matrix)

    def pretty_print_matrix(self, matrix):
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table) + "\n")


Marc = Person("Marc", [1, 2, 3, 4, 5, 6, 7])
Seb = Person("Seb", [2, 3, 4, 1, 6, 7, 5])
Val = Person("Val", [5, 6, 7, 4, 2, 3, 1])
Antoine = Person("Antoine", [5, 6, 1, 3, 2, 4, 7])
Julien = Person("Julien", [4, 6, 2, 7, 1, 3, 5])
Owen = Person("Owen", [6, 7, 4, 2, 5, 3, 1])
LP = Person("LP", [1, 2, 5, 3, 7, 4, 6])

chooser = GroupChoiceOptimizer(choiceList=[1, 2, 3, 4, 5, 6, 7], personList=[Marc, Seb, Val, Antoine, Julien, Owen, LP])
chooser.optimize_given_choice()

