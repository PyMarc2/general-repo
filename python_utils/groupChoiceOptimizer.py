import itertools


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

    def add_person(self, person: Person):
        self.personList.append(person)

    def generate_person(self, name, choiceList):
        self.personList.append(Person(name, choiceList))

    def optimize_given_choice(self):
        permutations = list(itertools.permutations(self.choiceList))
        self.optimalChoiceList = []
        lowestSum = len(self.choiceList)**2
        sumList = []

        if self.personList:
            for c in permutations:
                indexes = [self.personList[i].choiceList.index(c[i]) for i in range(len(self.personList))]
                sumList.append(sum(indexes))

                if sumList[-1] < lowestSum:
                    lowestSum = sumList[-1]

            for v, s in enumerate(sumList):
                if s == lowestSum:
                    self.optimalChoiceList.append(permutations[v])

        self.pretty_print_results()

    def pretty_print_results(self):
        matrix = [[n.name for n in self.personList], self.optimalChoiceList[-1]]
        s = [[str(e) for e in row] for row in matrix]
        lens = [max(map(len, col)) for col in zip(*s)]
        fmt = '\t'.join('{{:{}}}'.format(x) for x in lens)
        table = [fmt.format(*row) for row in s]
        print('\n'.join(table) + "\n")

        print("Other equivalents:", self.optimalChoiceList)


Marc = Person("Marc", [1, 2, 3, 4])
Seb = Person("Seb", [2, 3, 4, 1])
Val = Person("Val", [4, 2, 3, 1])
Leo = Person("Leo", [1, 3, 2, 4])

chooser = GroupChoiceOptimizer(choiceList=[1,2,3,4], personList=[Marc, Seb, Val, Leo])
chooser.optimize_given_choice()

