Skip to main content
On this page
## Vectors​
Excalibur uses the Vector structure to represent points. The Vector class has many different static methods available for doing vector math as well as instance methods to combine vectors together in different ways.
### Creating vectors​
To quickly create a vector, use the vec global:
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10)
Copy
```
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10)
Copy
```

Alternatively, you may see examples of using the more verbose `new Vector(x, y)` format:
```

ts
import { Vector } from'excalibur'
constpoint=newVector(0, 10)
Copy
```
```

ts
import { Vector } from'excalibur'
constpoint=newVector(0, 10)
Copy
```

To set the value of an existing vector, use Vector.setTo:
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10).setTo(10, 10)
Copy
```
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10).setTo(10, 10)
Copy
```

There are some built-in vector constants you can use:
  * Vector.Zero
  * Vector.One
  * Vector.Half
  * Vector.Left
  * Vector.Right
  * Vector.Up
  * Vector.Down


### Cloning vectors​
Vectors are objects, so mutating them will change the state for all references. Use the Vector.clone method to clone a vector to mutate it:
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10)
constsamePoint= point.setTo(8, 8)
constanotherPoint= point.clone().setTo(50, 50)
console.log(point.toString()) // "(8, 8)"
console.log(samePoint.toString()) // "(8, 8)"
console.log(anotherPoint.toString()) // "(50, 50)"
Copy
```
```

ts
import { vec } from'excalibur'
constpoint=vec(0, 10)
constsamePoint= point.setTo(8, 8)
constanotherPoint= point.clone().setTo(50, 50)
console.log(point.toString()) // "(8, 8)"
console.log(samePoint.toString()) // "(8, 8)"
console.log(anotherPoint.toString()) // "(50, 50)"
Copy
```

Notice how both `point` and `samePoint` share the same vector reference, so using `setTo` mutates the vector. Use `clone` to ensure you are not changing vectors unexpectedly!
  * Vectors
    * Creating vectors
    * Cloning vectors


