# Python OOP - Abtract Class, Interface, Subclassing

This repo is part of the **Holberton School x Tuwaiq Bootcamp**.  

##  Objectives  

- Abstract classes to enforce structure  
- Interfaces & duck typing to build flexible systems  
- Subclassing built-ins to control behavior  
- Method overriding to customize logic  
- Multiple inheritance to combine roles  
- Mixins to keep code modular and reusable
  
## ✅ Tasks Breakdown
<details> <summary><strong>0. Animal (Abstract Base)</strong></summary>
Define an abstract Animal class with one abstract method: sound().

Subclasses Dog and Cat override it with "Bark" and "Meow".

Instantiating Animal directly raises a TypeError.

</details> <details> <summary><strong>1. Shape Interface & Duck Typing</strong></summary>
Define a Shape ABC with area() and perimeter().

Implement Circle and Rectangle.

Create shape_info(obj) — it just calls area() and perimeter().
No type-checking. If it walks like a Shape, it is a Shape.

</details> <details> <summary><strong>2. VerboseList — Custom List with Logs</strong></summary>
Inherit from Python's list and override:

append() → log what was added

extend() → log how many were added

remove() → log what was removed

pop() → log what was popped

Demonstrates how to extend built-in types while preserving core behavior.

</details> <details> <summary><strong>3. CountedIterator</strong></summary>
Wrap any iterable and track how many items are fetched.

Override __next__ and count internally.

Expose the count via .get_count().

</details> <details> <summary><strong>4. FlyingFish — Multiple Inheritance</strong></summary>
Create:

Fish → has swim() and habitat()

Bird → has fly() and habitat()

Then:

FlyingFish(Fish, Bird) → override all three methods

Print .mro() to show how Python resolves method calls.

</details> <details> <summary><strong>5. Dragon — Mixins in Action</strong></summary>
Build small mixins:

SwimMixin → adds swim()

FlyMixin → adds fly()

Then:

Dragon(SwimMixin, FlyMixin) → combines both behaviors

Add .roar() to make it unique

</details>

---

## Functions Used

| Function / Class       | Purpose                                                             |
|------------------------|----------------------------------------------------------------------|
| `@abstractmethod`      | Declares a method that must be implemented by any subclass          |
| `ABC` / `ABCMeta`      | Used to create abstract base classes                                |
| `area()` / `perimeter()` | Interfaces for geometry objects (`Shape`)                           |
| `append()` / `extend()` | List methods overridden for logging in `VerboseList`                |
| `remove()` / `pop()`   | More list method overrides in `VerboseList`                          |
| `__next__()`           | Custom iteration logic in `CountedIterator`                         |
| `get_count()`          | Returns how many items have been iterated                           |
| `swim()` / `fly()`     | Behavior methods in mixins and base classes                         |
| `habitat()`            | Demonstrates method override in multiple inheritance                |
| `.mro()`               | Shows the method resolution order for a class                       |


