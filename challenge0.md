Challenge 0: Static and Dynamic Structures
Phase 0 - Sort the Scenarios

Scenario 0: Airplane Seats
An airplane has exactly 180 seats. Each seat may be empty or assigned to one passenger.

0. Structure choice: Static structure
1. Reason: The airplane always has exactly 180 seats. The number of seat positions does not grow or shrink.
2. Most important operation: Direct access. The system should quickly access a seat by its seat number.
3. Disadvantage: The structure always reserves space for all 180 seats, even when many seats are empty.

Scenario 1: Help Desk Tickets
A help desk receives an unpredictable number of support tickets throughout the day.

0. Structure choice: Dynamic structure
1. Reason: The number of support tickets is unpredictable and can increase or decrease throughout the day.
2. Most important operation: Insertion. New tickets must be added whenever customers submit them.
3. Disadvantage: A dynamic structure may use additional memory and may be more complex to manage.

Scenario 2: Vending Machine Slots
A vending machine has 12 fixed slots for snack types.

0. Structure choice: Static structure
1. Reason: The machine has exactly 12 physical slots, so the number of positions is fixed.
2. Most important operation: Direct access. Each snack type can be found using its slot number.
3. Disadvantage: The machine cannot store more than 12 snack types without changing its physical design.

Scenario 3: Connected Multiplayer Game Players
A multiplayer game stores the players who are currently connected.

0. Structure choice: Dynamic structure
1. Reason: Players can connect to or disconnect from the game at any time, so the number of players constantly changes.
2. Most important operation: Insertion and deletion. Players must be added when they connect and removed when they disconnect.
3. Disadvantage: Adding and removing players may require more memory management than using a fixed-size structure.

Scenario 4: Classroom Desks
A classroom has 30 numbered desks.

0. Structure choice: Static structure
1. Reason: The classroom has exactly 30 desks, and each desk has a fixed number.
2. Most important operation: Direct access. A desk can be located or assigned using its desk number.
3. Disadvantage: The structure cannot represent more than 30 desks unless its capacity is changed.

Scenario 5: Live Chat Messages
A live chat system stores incoming messages until moderators review them.

0. Structure choice: Dynamic structure
1. Reason: The number of incoming messages is unpredictable, and messages are removed after moderators review them.
2. Most important operation: Insertion and deletion. New messages must be added, and reviewed messages must be removed.
3. Disadvantage: The structure may continue growing and use a large amount of memory if moderators do not review messages quickly enough.

Static and Dynamic Structure Trade-offs
A static structure has a fixed capacity. It is useful when the number of positions is known in advance. Static structures often provide fast, direct access and predictable memory usage. However, they may waste memory when some positions are unused, and they cannot easily grow when more storage is needed.
A dynamic structure can grow or shrink as data is added or removed. It is useful when the amount of data is unpredictable. Dynamic structures use storage more flexibly, but they may require additional memory and more complicated insertion, deletion, or resizing operations.
Structure	Benefits	Costs
Static	Fast direct access, predictable capacity, simple organization.  Fixed size, possible unused space, cannot easily grow.
Dynamic can grow and shrink; flexible storage; useful for unpredictable data. More memory management, possible resizing cost, and more complexity
Structure-Based Solution
For the airplane seating system, I chose a static structure before writing the solution because the airplane always has exactly 180 seats.
The following Python example uses a list with 180 fixed seat positions:
TOTAL_SEATS = 180

# None means that the seat is currently empty.
seats = [None] * TOTAL_SEATS


def assign_seat(seat_number, passenger_name):
    if seat_number < 1 or seat_number > TOTAL_SEATS:
        return "Invalid seat number."

    index = seat_number - 1

    if seats[index] is not None:
        return f"Seat {seat_number} is already assigned."

    seats[index] = passenger_name
    return f"Seat {seat_number} assigned to {passenger_name}."


def remove_passenger(seat_number):
    if seat_number < 1 or seat_number > TOTAL_SEATS:
        return "Invalid seat number."

    index = seat_number - 1

    if seats[index] is None:
        return f"Seat {seat_number} is already empty."

    passenger_name = seats[index]
    seats[index] = None
    return f"{passenger_name} was removed from seat {seat_number}."


print(assign_seat(25, "Alex"))
print(assign_seat(25, "Jordan"))
print(remove_passenger(25))
The most important operation in this solution is direct access. The program can access a seat directly using its seat number. A static list is appropriate because the number of airplane seats never changes.
