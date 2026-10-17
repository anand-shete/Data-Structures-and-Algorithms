
"""
Python Exception Hierarchy  

• BaseException: The absolute root of all exception
	• SystemExit: Raised when the program is told to close eg. sys.exit()
	• KeyboardInterrupt: Raised when a user hits Ctrl+C to cancel a running program.
	• Exception: The parent class for almost all standard application error
		• ArithmeticError: The parent for math disasters.
			• ZeroDivisionError: Trying to divide by zero 5 / 0
			• OverflowError: A numeric calculation exceeds maximum limits.
		• LookupError: The parent for trying to access data that isn't there.
			• IndexError: Looking for a list index that doesn't exist.
			• KeyError: Looking for a dictionary key that doesn't exist.
		• ValueError: An argument has the right type, but an inappropriate value eg. int("apple")
		• TypeError: An operation is applied to an inappropriate data type eg. len(5)
		• NameError: A variable or function name is not defined in the local or global scope.
		• OSError: The parent for system-level failures files, networks
			• FileNotFoundError: Trying to open a file that does not exist.
			• PermissionError: Trying to open a system file without admin rights.
"""


# custom exception
class CustomErr(Exception):
    """
    Python error stacks are read from **bottom to top**
    """
    
    print('custom error handling class')


# raise (throw) exception
age = int(input("Enter age: "))
if age < 0:
    raise ValueError('age cannot be -ve')
elif age < 18:
    print('good to go')
else:
    raise CustomErr("hehehe")