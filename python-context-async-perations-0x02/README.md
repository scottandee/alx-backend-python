# Python Context Managers & Async Operations - 0x02
Context managers in Python provide a clean and reliable way to manage resources such as files, database connections, and network sockets. They ensure that resources are properly acquired and released using the `with` statement, which automatically invokes the `__enter__` and `__exit__` methods.

Asynchronous programming allows for non-blocking code execution, enabling tasks to run concurrently. Python’s asyncio library provides tools to write asynchronous code using async and await keywords, making it suitable for IO-bound tasks like web servers and network communication.

## Project Objectives
- Implement class-based context managers using __enter__ and __exit__ methods
- Understand resource management and automatic cleanup with context managers
- Master asynchronous database operations using aiosqlite
- Implement concurrent query execution with asyncio.gather
- Handle database connections and queries in a Pythonic way  

## How to Run the Code
1. Ensure you have Python 3 installed.    
2. Run `python3 seed.py` to create the sqlite database.  
3. Run the script using `python3 <filename>.py`.  

## Context Manager
### Using a File Context Manager
```python
with open("example.txt", "w") as f:
    f.write("Hello, World!")
```
### Class-based Context Manager
```python
class OpenFile:
    def __enter__(self):
        return self.file_obj

    def __exit__(self, type, value, traceback):
        self.file_obj.close()
```
## Benefits of a Context Manager
- **Automatic Resource Management**: Resources are released automatically without manual cleanup.
- **Exception Safety**: Resources are cleaned up even when errors occur.
- **Code Readability**: Cleaner and more concise syntax for handling resources.
- **Reusability**: Write once, use across multiple projects.
- **Consistency**: Guarantees predictable setup and teardown behavior.

## Asynchronous Functions
### Basic Coroutine
A coroutine is a functions defined with `async def` that can be paused and resumed.
```python
import asyncio

async def greet(name):
    print(f"Hello {name}")
    await asyncio.sleep(1)
    print(f"Goodbye {name}")

asyncio.run(greet("World"))
```

### Running Multiple Coroutines
Running multiple coroutines concurrently without multithreading

```python
async def main():
    await asyncio.gather(
        greet("Alice"),
        greet("Bob"),
    )

asyncio.run(main())
```

## Benefits of Asynchronous Programming
- **Non-Blocking Execution**: Perform tasks without waiting for I/O operations.  
- **Concurrency**: Run multiple tasks simultaneously with minimal overhead.  
- **Scalability**: Handle thousands of connections efficiently.  
- **Improved Performance**: Faster response times in I/O-heavy applications.  
