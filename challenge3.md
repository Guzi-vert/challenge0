# Challenge 3: Campus Map Neighbor Finder

## Phase 1 - Understand the Map

### 0. What are the nodes in this campus map?

The nodes are the campus locations:

- Library
- Student Center
- Science Building
- Gym
- Cafeteria
- Engineering Lab
- Bookstore

### 1. What are the edges in this campus map?

The edges are the walking paths between connected campus locations.

Examples include:

- Library and Student Center
- Library and Science Building
- Student Center and Gym
- Student Center and Cafeteria
- Science Building and Engineering Lab
- Student Center and Bookstore
- Cafeteria and Bookstore

### 2. What does each dictionary key represent?

Each dictionary key represents one campus location, or node.

### 3. What does each dictionary value represent?

Each dictionary value is a list of locations that can be reached directly from that location.

### 4. Why is a graph a better fit than a plain list for this problem?

A graph is a better fit because it stores both the campus locations and the connections between them. A plain list would only show the names of the locations, but it would not show which locations are connected.

---

## Phase 2 - Read the Adjacency List

### 0. Which locations can be reached directly from Library?

Student Center and Science Building can be reached directly from Library.

### 1. Which locations can be reached directly from Student Center?

Library, Gym, Cafeteria, and Bookstore can be reached directly from Student Center.

### 2. Which locations can be reached directly from Gym?

Only Student Center can be reached directly from Gym.

### 3. Is Library directly connected to Gym?

No. Library is not directly connected to Gym.

### 4. Is Library indirectly connected to Gym through another location?

Yes. Library is indirectly connected to Gym through Student Center.

The path is:

`Library -> Student Center -> Gym`

---

## Phase 3 - Build the Neighbor Finder

The `show_neighbors` function works like this:

1. It receives the campus map and a location.
2. It checks whether the location exists in the map.
3. If the location does not exist, it prints a helpful message.
4. If the location exists, it prints the location name.
5. It loops through the list of direct neighbors.
6. It prints each neighbor.

---

## Phase 4 - Add to the Map

I added one new campus location:

- Bookstore

The Bookstore is connected to:

- Student Center
- Cafeteria

I also updated Student Center and Cafeteria so that the connection works in both directions.

---

## Phase 5 - Test Your Program

## Test 0

```python
show_neighbors(campus_map, "Library")

Result:

The program displayed Student Center and Science Building. This tested a location with several neighbors.

## Test 1
show_neighbors(campus_map, "Gym")

Result:

The program displayed Student Center. This tested a location with one neighbor.

## Test 2
show_neighbors(campus_map, "Parking Lot")

Result:

The program printed:

Parking Lot is not in the campus map.

The program did not crash.

## Test 3
show_neighbors(campus_map, "Bookstore")

Result:

The program displayed Student Center and Cafeteria. This tested the new location that I added.

## Test 4
show_neighbors(campus_map, "Engineering Lab")

Result:

The program displayed Science Building. Engineering Lab is indirectly connected to Library through Science Building.


## Phase 6 - Reflect On the Data Structure

0. Why is this campus map an example of a graph?

This campus map is a graph because it contains nodes and edges. The campus locations are nodes, and the walking paths between locations are edges.

1. What would be harder if this map were stored as one plain list of location names?

It would be harder to determine which locations are directly connected. A plain list would only store names and would not show the walking paths between them.

2. Why does a dictionary of lists work well for this problem?

A dictionary makes it easy to find a location by name. The list stored with each location contains all of its direct neighbors.

3. What does it mean for two locations to be directly connected?

Two locations are directly connected when there is one walking path between them and no other location is needed.

4. What does it mean for two locations to be indirectly connected?

Two locations are indirectly connected when a person must pass through one or more other locations to travel between them.

5. How is this similar to a real map or navigation app?

A navigation app represents places as nodes and roads or paths as edges. It uses these connections to help find routes between locations.

6. What would need to change if walking paths had distances or travel times?

Each connection would also need to store a distance or travel time.

For example:

("Library", 4)

The number could represent four minutes of walking time.