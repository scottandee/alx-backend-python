# Python Decorators - 0x01
Decorators are functions that modify the behavior of another function or method. They are applied using the @decorator name syntax and can be used to add, modify, or extend the behavior of the original function without altering its code. Common use cases for decorators include logging, enforcing access control, memoization, and more.

## Project Objectives
- Deepen knowledge of Python decorators and how they can be used to create reusable, efficient, and clean code.
- Enhance database management skills by automating repetitive tasks like connection handling, logging, and caching.
- Implement robust transaction management techniques to ensure data integrity and handle errors gracefully.
- Optimize database queries by leveraging caching mechanisms to reduce redundant calls.
- Build resilience into database operations by implementing retry mechanisms for transient errors.
- Apply best practices in database interaction for scalable and maintainable Python applications.

## How to Run the Code

1. Run `python3 seed.py` to create the database.
2. Execute the python scripts using `python3 <filename>.py`.

## Decorator Syntax
### Simple Decorator
A simple decorator is a function that takes another function as input and extends or modifies its behavior. It is applied using the `@decorator_name` syntax.

```python
def simple_decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@simple_decorator
def say_hello():
    print("Hello!")

say_hello()
```

### Decorator with Arguments
Decorators can also accept arguments by nesting an additional function layer. This allows for more flexible and dynamic behavior.

```python
def decorator_with_args(arg):
    def outer_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Decorator argument: {arg}")
            return func(*args, **kwargs)
        return wrapper
    return outer_decorator

@decorator_with_args("example")
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
```

## Benefits of Decorators
- **Code Reusability**: Encapsulate reusable functionality in a single place.
- **Separation of Concerns**: Keep the core logic of functions clean and focused.
- **Enhanced Readability**: Simplify complex logic by abstracting repetitive tasks.
- **Dynamic Behavior**: Modify or extend functionality without altering the original function.
- **Improved Maintainability**: Centralize common patterns, making code easier to update and debug.
