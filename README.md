# | Just Another Shooter Game |

**Game Overview**

This Python game demonstrates object-oriented programming (OOP) principles through interactive gameplay involving fruits and bullets. The codebase is structured around a clear class hierarchy and composition techniques to promote modularity and code reuse.

- **Class Hierarchy & Inheritance:**  
  The core entities, such as `Fruit` and `Bullet`, are implemented as base classes. Specialized fruits (e.g., exotic fruits) inherit from the `Fruit` class, allowing them to extend or override behavior while reusing common attributes and methods.

- **Composition:**  
  The game leverages composition by associating objects, such as attaching an `AdditionalBullet` instance to a main bullet. This approach enables flexible relationships between objects without deepening the inheritance tree.

- **Dynamic Attributes:**  
  Some classes, like the additional fruit, showcase dynamic behavior by changing attributes (e.g., color) randomly each frame, illustrating how OOP can be used to manage state and behavior changes over time.

- **Extensibility:**  
  The design makes it easy to add new fruit or bullet types by extending base classes or composing new behaviors, supporting scalability and maintainability.

This project is ideal for demonstrating OOP concepts such as inheritance, composition, encapsulation, and dynamic attribute management in Python.