from  add_table.games import add_table_game

class Task:
    def __init__(self, task_line):
        self.task_line = task_line

    @property
    def text(self):
        return self.task_line

    @property
    def answer(self):
        return eval(self.task_line)

    def __repr__(self):
        return self.text

class UserGame(add_table_game.TableGame):
    def __init__(self, name_game: str):
        super().__init__(name_game)



    def create_tasks(self, tasks_data: list):
        self.tasks.clear()
        for t in tasks_data:
            self.tasks.append(Task(t))



if __name__ == '__main__':
    tasks = ["10+10+5"]
    ug = UserGame("user")
    ug.create_tasks(tasks)
    ns = ug.next_step
    print(ns)
    print(ns.text)
    print(ns.answer)