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

    @property
    def answer(self):
        return self.operator.method(self.level, self.term)

    def __repr__(self):
        return "{}: ({} {} {})".format(self.__class__.__name__, self.level,
                                self.operator.sign(), self.term)


class AddTableGame:
    def __init__(self, name):
        self.name = name
        self.tasks = []
        self.cursor = -1
        self._current_task = None


    @property
    def current_task(self):
        return self._current_task

    @current_task.setter
    def current_task(self, task):
        self._current_task = task

    def check_answer(self, answer):

        if int(answer) == self.current_task.answer:
            return True

    def __str__(self):
        return "class: {} - {}".format(self.__class__.__name__,
                                       self.name)

    @property
    def next_step(self):
        if self.cursor < len(self.tasks) - 1:
            self.cursor +=1
            self.current_task = self.tasks[self.cursor]
            return self.current_task
        else:
            return None

    def run_new_game(self):
        self.cursor = -1


    def create_tasks(self, level: int, operator_line: str, mix=False):
        self.tasks.clear()
        # for t in range(1, 10):
        for t in range(1, 2):
            self.tasks.append(Task(level, t, operator_line))
        if mix:
            self.tasks_mix()


    def tasks_mix(self):
        random.shuffle(self.tasks)

    def current_answer(self):
        return




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
