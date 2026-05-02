# Fix My Code Challenge

## Description

This project is part of the **Holberton School** curriculum. The goal is to dive into an existing codebase and fix bugs — without rewriting everything from scratch. Each task presents broken code in various programming languages, and the challenge is to identify and correct what's going wrong.

---

## Technologies Used

| Language | Task |
|----------|------|
| Python 3 | FizzBuzz, User class |
| JavaScript (Node.js) | Print square |
| Ruby | Sort arguments |
| C (GNU89) | Double linked list |

---

## Tasks

### 0. FizzBuzz — `0-fizzbuzz.py`

A Python implementation of the classic FizzBuzz problem.

**Bug:** The condition order was incorrect — numbers divisible by both 3 and 5 were printing `Fizz` instead of `FizzBuzz`.

**Fix:** Moved the `% 15` check before the `% 3` and `% 5` checks.

```bash
$ ./0-fizzbuzz.py 50
1 2 Fizz 4 Buzz Fizz 7 8 Fizz Buzz 11 Fizz 13 14 FizzBuzz ...
```

---

### 1. Print Square — `1-print_square.js`

A JavaScript program that prints a square of `#` characters based on a given size.

**Bug:** The loop bounds were not using the correct `size` variable, producing an oversized square.

**Fix:** Both the row and column loops now correctly use `size`.

```bash
$ ./1-print_square.js 4
####
####
####
####
```

---

### 2. Sort — `2-sort.rb`

A Ruby script that sorts integer arguments passed via the command line.

**Bug:** The sorting logic was not ordering the integers correctly.

**Fix:** Implemented a custom comparator that correctly sorts integers in ascending order while filtering out non-numeric arguments.

```bash
$ ruby 2-sort.rb 12 41 2 C 9 -9 31 fun -1 32
-9
-1
2
9
12
31
32
41
```

---

### 3. User Password — `3-user.py`

A Python `User` class with password validation.

**Bug:** Missing `__str__` method and `print(u)` call; the object had no string representation. Also, the password attribute was not properly encapsulated.

**Fix:** Added `__str__` returning `"FirstName LastName"`, added `print(u)` in the test block, and used name mangling (`self.__password`) for proper encapsulation.

```bash
$ ./3-user.py
Test User
is_valid_password should return True if it's the right password
is_valid_password should return False if it's not the right password
```

---

### 4. Double Linked List — `4-delete_dnodeint/`

A C implementation of a doubly linked list with a function to delete a node at a given index.

**Bug:** The `delete_dnodeint_at_index` function was not properly relinking the surrounding nodes before freeing the target node — it zeroed the value instead of removing the node from the list.

**Fix:** Correctly update `prev->next` and `next->prev` pointers before calling `free()`.

**Files:**

| File | Description |
|------|-------------|
| `dlistint.h` | Header file with struct definition and prototypes |
| `main.c` | Test file |
| `add_dnodeint_end.c` | Adds a node at the end of the list |
| `print_dlistint.c` | Prints all elements of the list |
| `free_dlistint.c` | Frees the entire list |
| `delete_dnodeint_at_index.c` | Deletes a node at a given index (bug fixed here) |

**Compile & Run:**

```bash
$ gcc -Wall -pedantic -Werror -Wextra -std=gnu89 \
    main.c free_dlistint.c print_dlistint.c \
    add_dnodeint_end.c delete_dnodeint_at_index.c \
    -o delete_dnodeint
$ ./delete_dnodeint
```

---

## Author

**Abdullah Al-Salem**
Holberton School Student
