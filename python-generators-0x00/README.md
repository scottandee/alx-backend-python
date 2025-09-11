# Python Generators 0x00
Generators are a special type of iterable in Python that allow you to yield items one at a time using the `yield` keyword. They are memory-efficient and enable lazy evaluation, making them ideal for handling large datasets or infinite sequences.

## Project Objectives
- Learn to create and utilize generators for iterative data processing, enabling memory-efficient operations.
- Implement batch processing and lazy loading to work with extensive datasets without overloading memory.
- Develop solutions to simulate live data updates and apply them to streaming contexts.
- Use generators to calculate aggregate functions like averages on large datasets, minimizing memory consumption.
- Use SQL queries to fetch data dynamically, integrating Python with databases for robust data management.

## How to Run the Code
1. Copy the contents of `.env.example` into a new file called `.env`
2. Create a postgres database user name and password
3. Fill the `.env` with correct details
3. Run `python3 seed.py` to create the database.
4. Run the script using `python3 <filename>.py`.

## Generator Syntax
### Simple Generator
A generator function uses the `yield` keyword to produce values one at a time.

```python
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)
```

### Generator Expression
A generator expression is a concise way to create a generator.

```python
gen_exp = (x * x for x in range(5))

for value in gen_exp:
    print(value)
```

## Benefits of Generators
- **Memory Efficiency**: Generate items on the fly without storing the entire sequence in memory.
- **Lazy Evaluation**: Produce values only when needed, improving performance for large datasets.
- **Simplified Code**: Replace complex iterator classes with simple generator functions.
- **Infinite Sequences**: Easily create infinite sequences without running out of memory.
- **Improved Performance**: Reduce overhead for large-scale data processing tasks.
- **Flexibility**: Use `yield` to control the flow of data dynamically.

