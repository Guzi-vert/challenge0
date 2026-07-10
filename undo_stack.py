# undo_stack.py

class UndoStack:
    def __init__(self):
        # TODO: Create an empty list to store actions
         self.actions = []

    def do_action(self, action):
        """
        Add a new action to the undo history.
        Example action: "typed hello"
        """
        # TODO: Add the action to the stack
        self.actions.append(action)

    def undo_action(self):
        """
        Remove and return the most recent action.
        If there are no actions, return "Nothing to undo."
        """
        # TODO: Check whether the stack is empty

        # TODO: Remove and return the most recent action
        if len(self.actions) == 0:
            return "Nothing to undo."
          
          # Remove and return the most recent action.
        return self.actions.pop()

    def show_history(self):
        """
        Print all actions currently stored in the undo history.
        """
        # TODO: Print the current action history
        print("Current history:", self.actions)


# Demo code
history = UndoStack()

history.do_action("typed hello")
history.do_action("made text bold")
history.do_action("changed font size")

history.show_history()

print(history.undo_action())
print(history.undo_action())

history.show_history()
