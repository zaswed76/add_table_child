import operator
import random


class Operator():
    Add = "add"
    Sub = "sub"
    operations = dict(
        add={"sign": "+", "meth": operator.add},
        sub={"sign": "-", "meth": operator.sub}
    )

    def __init__(self, operator_line: str):
        self.operator_line = operator_line

    def sign(self):
        return self.operations[self.operator_line]["sign"]

    def method(self, *args):
        return self.operations[self.operator_line]["meth"](*args)


#





class Task:
    def __init__(self, level, term, operator_line: str):
        self.operator = Operator(operator_line)
        self.term = term
        self.level = level

    @property
    def text(self):
        return "{}    {}    {}".format(self.level,
                                       self.operator.sign(),
                                       self.term)

    def __repr__(self):
        return "{}: ({} {} {})".format(self.__class__.__name__, self.level,
                                self.operator.sign(), self.term)


class AddTableGame:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.cursor = -1


    def __str__(self):
        return "class: {} - {}".format(self.__class__.__name__,
                                       self.name)

    @property
    def next_step(self):
        if self.cursor < len(self.tasks) - 1:
            self.cursor +=1
            return self.tasks[self.cursor]
        else:
            return None


    def create_tasks(self, level: int, operator_line: str):
        for t in range(1, 10):
            self.tasks.append(Task(level, t, operator_line))

    def tasks_mix(self):
        random.shuffle(self.tasks)




if __name__ == '__main__':
    pass
    game = AddTableGame("add_table")
    game.create_tasks(2, Operator.Add)
    # print(game.tasks)
    # game.tasks_mix()
    for i in range(15):
        task = game.next_step
        if isinstance(task, Task):
            print(task.text)


            # # print(operator.add.__format__())
    # op = Operator(1, 2)
    # print(op)
