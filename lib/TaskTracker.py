class TaskTracker:
    def __init__(self):
        # Parameters:
        #   none
        # Side effects:
        #   none
        self.tasks = []

    def add_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   f"{task} added"
        # Side-effects:
        #   adds task to self.tasks list
        self.tasks.append(task)
        print(f'{task} added')
    
    def show_tasks(self):
        # Returns:
        #   list of tasks
        # Side-effects:
        #   prints out tasks to be done
        if len(self.tasks) == 0:
            print('no tasks left!')
        else:
            for task in self.tasks:
                print(task)
        return self.tasks
    
    def complete_task(self, task):
        # Parameters:
        #   task: string representing a single task
        # Returns:
        #   Nothing
        # Side-effects
        #   prints to user f"{task} complete!"
        try:
            self.tasks.remove(task)
            print(f"{task} complete!")
        except:
            print(f'{task} is not on the list..')
            return None