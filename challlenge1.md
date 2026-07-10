# Challenge 1: Undo Button Stack

## Phase 0 - Design It

### 0. What does the undo button need to remember?

The undo button needs to remember the user's previous actions and the order in which those actions happened.

### 1. When a new action happens, where should it go?

A new action should be added to the top of the stack because it is the most recent action.

### 2. When the user clicks undo, which action should be removed first?

The most recent action should be removed first.

### 3. Why is a stack a better fit than a queue for this problem?

A stack uses Last In, First Out behavior. This matches an undo button because the most recent action must be undone first. A queue would remove the oldest action first.

### 4. What should happen if the user clicks undo but there is nothing left to undo?

The program should return a helpful message such as "Nothing to undo." It should not crash.

---

## Phase 1 - Pseudocode

### `__init__`

1. Create an empty list.
2. Store the list as the action history.

### `do_action`

1. Receive a new action.
2. Add the action to the end of the list.

### `undo_action`

1. Check whether the action history is empty.
2. If it is empty, return "Nothing to undo."
3. Otherwise, remove and return the last action.

### `show_history`

1. Display all actions currently stored in the history.

---

## Phase 4 - Reflect On It

### Why does an undo button use stack behavior?

An undo button uses stack behavior because the most recent action should always be undone first.

### What does LIFO mean in this program?

LIFO means Last In, First Out. The last action added to the history is the first action removed.

### What would go wrong if this program used FIFO behavior instead?

FIFO would remove the oldest action first. That would not match how an undo button is expected to work because users usually want to reverse their most recent action.

### Which method represents push?

The `do_action` method represents a push because it adds a new action to the stack.

### Which method represents pop?

The `undo_action` method represents pop because it removes and returns the most recent action.

### What part of this challenge felt easiest?

The easiest part was adding actions to the list with the `append` method.

### What part of this challenge felt least obvious?

The least obvious part was checking whether the stack was empty before using `pop`, because calling `pop` on an empty list would cause an error.
