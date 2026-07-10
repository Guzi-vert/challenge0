# Challenge 2: Locker Number Hashing

## Phase 1 - Predict It

### 1. What kind of input does the hash function receive?

The hash function receives a student name as a string and the number of locker rows as an integer.

### 2. What kind of output should the hash function produce?

The function should produce an integer that represents a valid locker row number.

### 3. Why should the same name always produce the same locker row?

The function uses the same calculation every time. Therefore, the same characters produce the same total and the same locker row.

### 4. What might cause two different names to be assigned to the same row?

Two different names may produce totals that have the same remainder when divided by the number of rows. This causes a collision.

### 5. Is a collision always an error? Why or why not?

No. A collision is not always an error because hash functions often assign different keys to the same bucket. The program only needs a way to handle multiple students in the same row.

---

## Phase 2 - Hash Function Pseudocode

1. Start with a total of 0.
2. Loop through every character in the student name.
3. Convert each character into a number using `ord()`.
4. Add each number to the total.
5. Divide the total by the number of rows and keep the remainder.
6. Return the remainder as the locker row number.

---

## Phase 3 - Assign Students Pseudocode

1. Receive a list of student names.
2. Loop through each name.
3. Call `locker_hash` with the name and the number of rows.
4. Print the student name and assigned row.

---

## Phase 4 - Test for Collisions

I tested these ten students with five locker rows:

- Ava
- Liam
- Noah
- Mia
- Zoe
- Emma
- Olivia
- Ethan
- Lucas
- Sophia

### 1. Which names were assigned to the same row?

Ava and Noah were assigned to row 0.

Liam, Zoe, Olivia, and Sophia were assigned to row 2.

Mia, Emma, and Lucas were assigned to row 4.

Ethan was assigned to row 1.

### 2. What row had the most students assigned to it?

Row 2 had the most students. It had four students.

### 3. Did the same name always get the same row when you ran the program again?

Yes. The same name always produced the same row because the hash calculation did not change.

### 4. What changed when you increased the number of locker rows?

The possible row numbers increased, and the students were spread across more rows. This can reduce the number of collisions.

### 5. What changed when you decreased the number of locker rows?

There were fewer possible rows, so more students were assigned to the same rows. This increased the number of collisions.

---

## Phase 5 - Reflect On the Data Structure

### 1. What does the student name represent in this challenge: a key, a value, or an index?

The student name represents a key. The hash function uses the key to calculate where the student should be assigned.

### 2. What does the locker row number represent?

The locker row number represents an index or bucket number.

### 3. Why do we use modulo in the hash function?

Modulo keeps the result within the valid range of locker rows. For example, with five rows, the result must be from 0 through 4.

### 4. Why are collisions more likely when there are fewer locker rows?

When there are fewer rows, more student names must share the same small set of possible results. This makes collisions more likely.

### 5. How is this similar to choosing a bucket in a hash table?

A hash table uses a hash function to convert a key into a bucket index. In this challenge, the student name is the key and the locker row is the bucket.

### 6. What would need to happen if each row could only hold one student?

The program would need a collision-handling method. For example, it could search for the next available row or reject the assignment if every row was full.