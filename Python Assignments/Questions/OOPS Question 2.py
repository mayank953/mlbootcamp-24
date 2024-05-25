
# Question 0: Class for Bank Account
"""
Design a Python class named `BankAccount` to represent bank accounts.

Theory:
A bank account typically includes attributes such as account number, balance, and account holder name.
The class should handle operations such as deposit, withdrawal, and transfer of funds between accounts.

Operations:
1. Deposit: Add funds to the account
2. Withdrawal: Subtract funds from the account
3. Transfer: Transfer funds from one account to another

Test Cases:
Test Case 1:
acc1 = BankAccount("John Doe", 1000)
acc2 = BankAccount("Jane Smith", 2000)
assert acc1.balance == 1000
assert acc2.balance == 2000
acc1.deposit(500)
acc2.withdraw(100)
acc1.transfer(acc2, 200)
assert acc1.balance == 1300
assert acc2.balance == 2300

Test Case 2:
acc3 = BankAccount("Alice Johnson", 500)
acc4 = BankAccount("Bob Brown", 1500)
assert acc3.balance == 500
assert acc4.balance == 1500
acc3.deposit(100)
acc4.withdraw(200)
acc3.transfer(acc4, 300)
assert acc3.balance == 400
assert acc4.balance == 1800
"""

class BankAccount:
    pass



# Question 1: Class for Complex Numbers
"""
Create a Python class named `ComplexNumber` to represent complex numbers.

Theory:
A complex number is a number that comprises a real part and an imaginary part.
It is typically written in the form a + bi, where 'a' is the real part,
and 'b' is the imaginary part, and 'i' is the imaginary unit (√-1).

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Division (/)
5. Comparison (==, !=)

Test Cases:
Test Case 1:
complex1 = ComplexNumber(3, 4)
complex2 = ComplexNumber(1, -2)
assert str(complex1) == "3+4i"
assert str(complex2) == "1-2i"
assert str(complex1 + complex2) == "4+2i"
assert str(complex1 - complex2) == "2+6i"
assert str(complex1 * complex2) == "11-2i"
assert str(complex1 / complex2) == "-1.0+2.5i"
assert complex1 != complex2

Test Case 2:
complex3 = ComplexNumber(-2, 5)
complex4 = ComplexNumber(2, 3)
assert str(complex3) == "-2+5i"
assert str(complex4) == "2+3i"
assert str(complex3 + complex4) == "0+8i"
assert str(complex3 - complex4) == "-4+2i"
assert str(complex3 * complex4) == "-16-1i"
assert str(complex3 / complex4) == "1.0+i"
assert complex3 != complex4
"""

class ComplexNumber:
    pass



# Question 3: Class for Matrix
"""
Implement a Python class named `Matrix` to represent matrices.

Theory:
A matrix is a two-dimensional array of numbers. The class should handle operations
such as addition, subtraction, multiplication, transposition, and determinant calculation.

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Transposition: Transpose the matrix
5. Determinant: Calculate the determinant of the matrix

Test Cases:
Test Case 1:
matrix1 = Matrix([[1, 2], [3, 4]])
matrix2 = Matrix([[5, 6], [7, 8]])
assert str(matrix1) == "[[1, 2], [3, 4]]"
assert str(matrix2) == "[[5, 6], [7, 8]]"
assert str(matrix1 + matrix2) == "[[6, 8], [10, 12]]"
assert str(matrix1 - matrix2) == "[[-4, -4], [-4, -4]]"
assert str(matrix1 * matrix2) == "[[19, 22], [43, 50]]"
assert str(matrix1.transpose()) == "[[1, 3], [2, 4]]"
assert matrix1.determinant() == -2

Test Case 2:
matrix3 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix4 = Matrix([[7, 8], [9, 10], [11, 12]])
assert str(matrix3) == "[[1, 2, 3], [4, 5, 6]]"
assert str(matrix4) == "[[7, 8], [9, 10], [11, 12]]"
assert str(matrix3 + matrix4) == "Addition not possible"
assert str(matrix3 - matrix4) == "Subtraction not possible"
assert str(matrix3 * matrix4) == "[[58, 64], [139, 154]]"
assert str(matrix4.transpose()) == "[[7, 9, 11], [8, 10, 12]]"
assert matrix4.determinant() == "Determinant not possible"
"""

class Matrix:
    pass

```python
# Question 4: Class for Polynomial
"""
Create a Python class named `Polynomial` to represent polynomials.

Theory:
A polynomial is an expression consisting of variables (or indeterminates) and coefficients,
that involves only the operations of addition, subtraction, multiplication, and non-negative integer exponents.

Operations:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (*)
4. Evaluation: Evaluate the polynomial at a given value
5. Differentiation: Compute the derivative of the polynomial

Test Cases:
Test Case 1:
poly1 = Polynomial([1, 2, 3])
poly2 = Polynomial([3, 4, 5])
assert str(poly1) == "1x^2 + 2x + 3"
assert str(poly2) == "3x^2 + 4x + 5"
assert str(poly1 + poly2) == "4x^2 + 6x + 8"
assert str(poly1 - poly2) == "-2x^2 - 2x - 2"
assert str(poly1 * poly2) == "3x^4 + 10x^3 + 22x^2 + 23x + 15"
assert poly1.evaluate(2) == 17
assert poly2.evaluate(2) == 29

Test Case 2:
poly3 = Polynomial([1, -1])
poly4 = Polynomial([2, -3, 4])
assert str(poly3) == "1x - 1"
assert str(poly4) == "2x^2 - 3x + 4"
"""

class Polynomial:
    pass



# Question 1: Implementing a Vehicle Hierarchy

from abc import ABC, abstractmethod

class Vehicle(ABC):
    """
    Design a Python class named `Vehicle` to represent a generic vehicle.

    Theory:
    A vehicle is a machine that transports people or cargo from one place to another.

    Operations:
    1. Start: Start the vehicle's engine. (Abstract Method)
    2. Stop: Stop the vehicle's engine.
    3. Drive: Drive the vehicle.

    Test Cases:
    Test Case 1:
    vehicle = Car("Toyota", "Red")
    assert vehicle.start() == "Starting the Toyota engine"
    assert vehicle.stop() == "Stopping the Toyota engine"
    assert vehicle.drive() == "Driving the Toyota"

    Test Case 2:
    # Additional test cases can be added here
    pass


class Car(Vehicle):
    """
    Design a Python class named `Car` to represent a car.

    Theory:
    A car is a road vehicle typically with four wheels, powered by an internal combustion engine.

    Operations:
    1. Lock Doors: Lock the car's doors.
    2. Unlock Doors: Unlock the car's doors.

    Test Cases:
    Test Case 1:
    car = Car("Toyota", "Red")
    assert car.start() == "Starting the Toyota engine"
    assert car.lock_doors() == "Locking the Toyota doors"
    assert car.drive() == "Driving the Toyota"

    Test Case 2:
    # Additional test cases can be added here
    pass


class Bicycle(Vehicle):
    """
    Design a Python class named `Bicycle` to represent a bicycle.

    Theory:
    A bicycle is a human-powered or motor-powered vehicle with two wheels.

    Operations:
    1. Pedal: Move the bicycle forward by pedaling.
    2. Ring Bell: Ring the bicycle's bell.

    Test Cases:
    Test Case 1:
    bicycle = Bicycle("Mountain Bike", "Green")
    assert bicycle.start() == "Starting the Mountain Bike engine"
    assert bicycle.pedal() == "Moving forward by pedaling"
    assert bicycle.ring_bell() == "Ringing the bell"

    Test Case 2:
    # Additional test cases can be added here
    pass
    """

# Question 2: Implementing a Shape Hierarchy

class Shape(ABC):
    """
    Design a Python class named `Shape` to represent a geometric shape.

    Theory:
    A shape is a geometric object that has a boundary and can be measured in terms of area and perimeter.

    Operations:
    1. Area: Calculate the area of the shape. (Abstract Method)
    2. Perimeter: Calculate the perimeter of the shape. (Abstract Method)

    Test Cases:
    Test Case 1:
    shape = Rectangle(4, 5)
    assert shape.area() == 20
    assert shape.perimeter() == 18

    Test Case 2:
    # Additional test cases can be added here
    pass


class Rectangle(Shape):
    """
    Design a Python class named `Rectangle` to represent a rectangle.

    Theory:
    A rectangle is a quadrilateral with four right angles.

    Operations:
    1. Area: Calculate the area of the rectangle.
    2. Perimeter: Calculate the perimeter of the rectangle.

    Test Cases:
    Test Case 1:
    rectangle = Rectangle(4, 5)
    assert rectangle.area() == 20
    assert rectangle.perimeter() == 18

    Test Case 2:
    # Additional test cases can be added here
    pass


class Circle(Shape):
    """
    Design a Python class named `Circle` to represent a circle.

    Theory:
    A circle is a simple shape consisting of all points in a plane that are at a given distance from a given center point.

    Operations:
    1. Area: Calculate the area of the circle.
    2. Perimeter: Calculate the perimeter of the circle.

    Test Cases:
    Test Case 1:
    circle = Circle(5)
    assert circle.area() == 78.54
    assert circle.perimeter() == 31.42

    Test Case 2:
    # Additional test cases can be added here
    pass

"""

    
    
    
    
    
    
    

# Question: Implementing the Quadrilateral Family

class Quadrilateral:
    """
    Design a Python class named `Quadrilateral` to represent a generic quadrilateral shape.
    The class should include methods to calculate perimeter and area, although the formula for area may not be applicable for all quadrilaterals.
    Quadrilateral is a superclass for other specific types of quadrilaterals.

    Attributes:
    - sides: A list containing the lengths of all four sides of the quadrilateral (list)
    - angles: A list containing the measures of all four angles of the quadrilateral in degrees (list)

    Methods:
    - perimeter(): Calculates and returns the perimeter of the quadrilateral (float)
    - area(): Calculates and returns the area of the quadrilateral (float). Note: The formula for area may not be applicable for all quadrilaterals.

    Test Cases:
    Test Case 1:
    quad1 = Quadrilateral([3, 4, 5, 6], [90, 90, 90, 90])
    assert quad1.perimeter() == 18
    # The sum of all sides = 3 + 4 + 5 + 6 = 18

    Test Case 2:
    quad2 = Quadrilateral([4, 4, 4, 4], [90, 90, 90, 90])
    assert quad2.area() == 16
    # For a square with side length 4, the area is 4 * 4 = 16

    Test Case 3:
    # Additional test cases can be added here


class Rectangle(Quadrilateral):
    """
    Design a Python class named `Rectangle` that inherits from the `Quadrilateral` class.
    The `Rectangle` class represents a rectangle shape.

    Attributes:
    - length: Length of the rectangle (float)
    - width: Width of the rectangle (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the rectangle (float)

    Test Cases:
    Test Case 1:
    rect1 = Rectangle(4, 6)
    assert rect1.area() == 24
    # For a rectangle with length 4 and width 6, the area is 4 * 6 = 24

    Test Case 2:
    # Additional test cases can be added here


class Square(Rectangle):
    """
    Design a Python class named `Square` that inherits from the `Rectangle` class.
    The `Square` class represents a square shape.

    Attributes:
    - side_length: Length of the side of the square (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the square (float)

    Test Cases:
    Test Case 1:
    square1 = Square(5)
    assert square1.area() == 25
    # For a square with side length 5, the area is 5 * 5 = 25

    Test Case 2:
    # Additional test cases can be added here


class Rhombus(Quadrilateral):
    """
    Design a Python class named `Rhombus` that inherits from the `Quadrilateral` class.
    The `Rhombus` class represents a rhombus shape.

    Attributes:
    - side_length: Length of the side of the rhombus (float)
    - diagonals: Length of the diagonals of the rhombus (list)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the rhombus (float)

    Test Cases:
    Test Case 1:
    rhombus1 = Rhombus(6, [8, 8])
    assert rhombus1.area() == 24
    # For a rhombus with side length 6 and diagonals 8 and 8, the area is (8 * 8) / 2 = 24

    Test Case 2:
    # Additional test cases can be added here


class Parallelogram(Quadrilateral):
    """
    Design a Python class named `Parallelogram` that inherits from the `Quadrilateral` class.
    The `Parallelogram` class represents a parallelogram shape.

    Attributes:
    - base: Length of the base of the parallelogram (float)
    - height: Height of the parallelogram (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the parallelogram (float)

    Test Cases:
    Test Case 1:
    parallelogram1 = Parallelogram(5, 8)
    assert parallelogram1.area() == 40
    # For a parallelogram with base 5 and height 8, the area is 5 * 8 = 40

    Test Case 2:
    # Additional test cases can be added here


class Trapezoid(Quadrilateral):
    """
    Design a Python class named `Trapezoid` that inherits from the `Quadrilateral` class.
    The `Trapezoid` class represents a trapezoid shape.

    Attributes:
    - base1: Length of one base of the trapezoid (float)
    - base2: Length of the other base of the trapezoid (float)
    - height: Height of the trapezoid (float)

    Methods:
    - area(): Overrides the area() method from the superclass to calculate and return the area of the trapezoid (float)

    Test Cases:
    Test Case 1:
    trapezoid1 = Trapezoid(3, 5, 4)
    assert trapezoid1.area() == 16
    # For a trapezoid with base1 3, base2 5, and height 4, the area is ((3 + 5) * 4) / 2 = 16

    Test Case 2:
    # Additional test cases can be added here

