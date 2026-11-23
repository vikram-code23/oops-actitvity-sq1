# 📚 Library Management System – Python OOP

## 1. What Are We Building?

We are building a simple Library Management System using Python.

A library has multiple books. Members can borrow books and return them. The library should also track whether each book is available or already borrowed.

For this activity, we are using two classes:

1. `Book`
2. `Library`

## 2. Understanding the Book Class

The `Book` class represents an individual book.

```python
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True
```

### Explanation

- `class Book` – Creates a Book class.
- `__init__()` – Constructor that runs automatically when an object is created.
- `self.title` – Stores the book title.
- `self.author` – Stores the author's name.
- `self.available = True` – Initially, every book is available.

### Creating a Book Object

```python
book1 = Book("Python 101", "Rao")
```

Now we have created a book object.

Its details are:

- Title: Python 101
- Author: Rao
- Available: True

### Understanding the __str__() Method

```python
def __str__(self):
    status = "Available" if self.available else "Borrowed"
    return f"{self.title} by {self.author} [{status}]"
```

This method controls how the book details are displayed when we use `print()`.

Example output:

```text
Python 101 by Rao [Available]
```

## 3. Understanding the Library Class

The `Library` class manages all the books.

```python
class Library:

    def __init__(self):
        self.books = []
```

### Explanation

- `class Library` – Creates a Library class.
- `__init__()` – Initializes the library.
- `self.books = []` – Creates an empty list to store Book objects.

Think of this list as a library shelf where we keep all our books.

## 4. Understanding Library Methods

### A. add_book()

```python
def add_book(self, book):
    self.books.append(book)
    print(f"'{book.title}' added successfully.")
```

**How it works:**

- Receives a Book object.
- Uses `append()` to add the book to the list.
- Displays a success message.

### B. borrow()

```python
def borrow(self, title):

    for book in self.books:

        if book.title == title:

            if book.available:
                book.available = False
                print(f"'{title}' borrowed successfully.")

            else:
                print(f"Sorry, '{title}' is already borrowed.")

            return

    print(f"No book titled '{title}'.")
```

**How it works:**

1. Searches for the book using its title.
2. Checks whether the book exists.
3. Checks whether the book is available.
4. If available, changes its status to `False`.
5. If already borrowed, displays an error message.
6. If the book doesn't exist, displays a not-found message.

**Remember:**

- `True` = Available
- `False` = Borrowed

### C. return_book()

```python
def return_book(self, title):

    for book in self.books:

        if book.title == title:

            if not book.available:
                book.available = True
                print(f"'{title}' returned successfully.")

            else:
                print(f"'{title}' was not borrowed.")

            return

    print(f"No book titled '{title}'.")
```

**How it works:**

1. Searches for the book.
2. Checks whether it is currently borrowed.
3. If borrowed, changes its status to `True`.
4. If it was not borrowed, displays a message.
5. If the book doesn't exist, displays a not-found message.

### D. show_books()

```python
def show_books(self):

    for book in self.books:
        print(book)
```

**How it works:**

- Uses a `for` loop to access every book.
- Prints each book's details.
- The `__str__()` method displays the title, author and availability status.

## 5. Main Program – How Everything Connects

First, create a Library object.

```python
library = Library()
```

Next, create Book objects.

```python
book1 = Book("Python 101", "Rao")
book2 = Book("Java Basics", "John")
book3 = Book("Linux Essentials", "David")
```

Add the books to the library.

```python
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)
```

Display all books.

```python
library.show_books()
```

Borrow a book.

```python
library.borrow("Python 101")
```

Return a book.

```python
library.return_book("Python 101")
```

Display the updated book list.

```python
library.show_books()
```

## 6. Overall Execution Flow

```text
        Start
          |
          v
    Create Library
          |
          v
     Create Books
          |
          v
     Add Books
          |
          v
    Show All Books
          |
          v
     Borrow Book
          |
          v
     Return Book
          |
          v
   Show Updated Status
          |
          v
         End
```

## 7. Sample Output

```text
Python 101 added successfully.
Java Basics added successfully.
Linux Essentials added successfully.

--- Library Books ---
Python 101 by Rao [Available]
Java Basics by John [Available]
Linux Essentials by David [Available]

--- Borrow Book ---
'Python 101' borrowed successfully.

--- Borrow Again ---
Sorry, 'Python 101' is already borrowed.

--- Return Book ---
'Python 101' returned successfully.

--- Final Book List ---
Python 101 by Rao [Available]
Java Basics by John [Available]
Linux Essentials by David [Available]
```

## 8. Key Concepts Learned

| Concept | What I Learned |
|---|---|
| Class | Creating a blueprint |
| Object | Creating instances of a class |
| Constructor | Initializing object details |
| self | Accessing object attributes and methods |
| List | Storing multiple Book objects |
| append() | Adding books to the list |
| for loop | Searching through books |
| if-else | Checking book availability |
| Boolean | Tracking True and False status |
| __str__() | Displaying book information |

**My Learning:** Through this activity, I understood how two Python classes work together, how objects are stored in a list, and how methods are used to perform operations such as adding, borrowing and returning books.

---

---------------------------------------------------------------------------------------


#MACHINE LEARNING
# ML-Based Addition Calculator Using Machine Learning

## 1. Project Overview

This project demonstrates how Machine Learning can be used to predict the sum of two numbers without directly using the `+` operator in the program.

Instead of performing addition manually, we train a **Linear Regression model** using sample input numbers and their corresponding sums. Once trained, the model predicts the sum of new numbers provided by the user.

## 2. Technologies Used

- **Python 3.11** – Programming language
- **NumPy** – To create and handle numerical datasets
- **Scikit-learn** – To build and train the Machine Learning model
- **Linear Regression** – ML algorithm used for prediction

## 3. How Does It Work?

The project works in the following steps:

### Step 1: Import Libraries

Import NumPy and Linear Regression from Scikit-learn.

- NumPy helps organize numerical data into arrays.
- Linear Regression is the Machine Learning algorithm used to learn the relationship between inputs and outputs.

### Step 2: Create Training Data

We provide sample pairs of numbers as input.

Example:

| First Number | Second Number | Expected Sum |
|---|---|---|
| 1 | 2 | 3 |
| 2 | 3 | 5 |
| 3 | 4 | 7 |
| 10 | 20 | 30 |
| 50 | 60 | 110 |
| 100 | 200 | 300 |

- `X` represents the input features (two numbers).
- `y` represents the expected output (their sum).

### Step 3: Create the ML Model

We create a Linear Regression model using:

`model = LinearRegression()`

This creates the model that will learn the relationship between the input numbers and their corresponding sums.

### Step 4: Train the Model

We train the model using:

`model.fit(X, y)`

During training, the model learns a mathematical relationship between the two input numbers and the output.

The model learns an equation similar to:

`Predicted Sum = (Weight 1 × Number 1) + (Weight 2 × Number 2) + Intercept`

Ideally, the learned weights are close to 1 and the intercept is close to 0.

### Step 5: Get User Input

The program asks the user to enter two numbers.

Example:
- First number: 400000
- Second number: 1

### Step 6: Prepare the Input

The user-provided numbers are converted into a NumPy array.

`new_input = np.array([[num1, num2]])`

The double square brackets represent a two-dimensional input structure expected by Scikit-learn.

### Step 7: Predict the Result

We use:

`prediction = model.predict(new_input)`

The trained model uses the relationship it learned during training to predict the output for the new input.

### Step 8: Display the Result

Finally, the predicted result is displayed.

Example:

```text
Enter first number: 400000
Enter second number: 1

Predicted Sum: 400001.0
```

## 4. Project Workflow

```text
        START
          |
          v
    Import Libraries
          |
          v
   Create Training Data
       (X and y)
          |
          v
   Create Linear Regression
          |
          v
      Train the Model
       (model.fit)
          |
          v
   Get Two Numbers from User
          |
          v
    Prepare Input Array
          |
          v
     Model Prediction
     (model.predict)
          |
          v
    Display Predicted Sum
          |
          v
         END
```

## 5. How Machine Learning Works in This Project

```text
       TRAINING PHASE
              |
              v
     Sample Input Data (X)
              |
              v
     Expected Output Data (y)
              |
              v
       Linear Regression
              |
              v
         Trained Model
              |
              |
       PREDICTION PHASE
              |
              v
      User Enters Two Numbers
              |
              v
       Trained ML Model
              |
              v
       Predicted Result
```

## 6. Key Learning Outcomes

- Understood the basic concept of Machine Learning.
- Learned the difference between training and prediction.
- Understood how input features and target values are provided to an ML model.
- Practiced using NumPy arrays.
- Built and trained a Linear Regression model using Scikit-learn.
- Understood how a trained model predicts outputs for new inputs.

## 7. Important Note

This is a beginner-level educational project created to understand the Machine Learning workflow.

Linear Regression learns a mathematical pattern from the training data. It is not actually performing arithmetic like a normal calculator, and its predictions may not always be exact for every possible input.

