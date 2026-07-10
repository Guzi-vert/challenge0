# campus_map.py

campus_map = {
    "Library": ["Student Center", "Science Building"],
    "Student Center": ["Library", "Gym", "Cafeteria"],
    "Science Building": ["Library", "Engineering Lab"],
    "Gym": ["Student Center"],
    "Cafeteria": ["Student Center"],
    "Engineering Lab": ["Science Building"],
    "Bookstore": ["Student Center", "Cafeteria"],
    "Admin Office": ["Library"],
}


def show_neighbors(campus_map, location):
    """
    Print all locations directly connected to the given location.
    """
    # TODO: Check whether location is in campus_map

    # TODO: If not found, print a helpful message

    # TODO: If found, print the location name

    # TODO: Loop through the location's neighbors and print each one
    if location not in campus_map:
        print(f"{location} is not in the campus map.")
        return
    
    print(f"Neighbors of {location}:")

    for neighbor in campus_map[location]:
        print(f"- {neighbor}")


# Demo calls
show_neighbors(campus_map, "Library")
print()

show_neighbors(campus_map, "Gym")
print()

show_neighbors(campus_map, "Parking Lot")
print()

show_neighbors(campus_map, "Bookstore")
print()

show_neighbors(campus_map, "Engineering Lab")
print()