import operator
import random



class Operator():
    Add = "add"
    Sub = "sub"
    Mul = "mul"
    operations = dict(
        add={"sign": "+", "meth": operator.add},
        sub={"sign": "-", "meth": operator.sub},
        mul={"sign": "*", "meth": operator.mul}
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


class TableGame:
    name_to_operator = dict(minus_table = "sub", add_table = "add",
                            mul_table="mul", user="user")
    def __init__(self, name_game: str):
        self.name_game = name_game
        self.tasks = []
        self.cursor = -1
        self._current_task = None
        self.operator = self.name_to_operator[self.name_game]



    @property
    def current_task(self):
        return self._current_task

    @current_task.setter
    def current_task(self, task):
        self._current_task = task

    def check_answer(self, answer):
        if int(answer) == self.current_task.answer:
            return True
        else: return False

    def __str__(self):
        return "class: {} - {}".format(self.__class__.__name__,
                                       self.name_game)

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


    def create_tasks(self, level: int, operator_line: str, mix=False,
                     test_mode=False, double=False):

        self.tasks.clear()

        seq = range(1, 2) if test_mode else range(1, 11)

        for t in seq:
            if operator_line in [Operator.Add, Operator.Mul]:
                self.tasks.append(Task(level, t, operator_line))
            elif level >= t:
                self.tasks.append(Task(level, t, operator_line))
        if mix:
            self.tasks_mix()
        if double:
            self.tasks_double()
            self.tasks_mix()


    def tasks_double(self):
        self.tasks*=2

    def tasks_mix(self):
        random.shuffle(self.tasks)

    def current_answer(self):
        return




if __name__ == '__main__':
    pass
    game = TableGame("add_table")
    game.create_tasks(2, Operator.Add)
    print(game.tasks[0].text)
    print(game.tasks[0].answer)

