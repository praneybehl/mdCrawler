Skip to main content
On this page
The Matrix type encapsulates a 4x4 matrix that can be used in WebGL or for doing affine transformations on Vectors and other Matrices.
The matrix data is stored in column major order, which is the convention for WebGL matrices.
data[0]| data[4]| data[8]| data[12]  
---|---|---|---  
data[1]| data[5]| data[9]| data[13]  
data[2]| data[6]| data[10]| data[14]  
data[3]| data[7]| data[11]| data[15]  
## Transforming Vectors​
Matrices are an efficient way to transform multiple vectors by the same transformation. Especially if the matrix can be cached.
```

typescript
constpoints= [...];
constmat= Matrix.identity().translate(100, 100).scale(2).rotate(Math.PI/2);
// transform the points
consttransformedPoints= points.map(p=> mat.multiply(p));
constinverse= mat.getAffineInverse();
// undo the transform with the inverse
constoriginalPoints= points.map(p=> inverse.multiply(p));
Copy
```
```

typescript
constpoints= [...];
constmat= Matrix.identity().translate(100, 100).scale(2).rotate(Math.PI/2);
// transform the points
consttransformedPoints= points.map(p=> mat.multiply(p));
constinverse= mat.getAffineInverse();
// undo the transform with the inverse
constoriginalPoints= points.map(p=> inverse.multiply(p));
Copy
```

## Multiplying Matrices​
Order matters when multiplying matrices `A x B != B x A` . When multiplying matrices the order read in the code
  * Transforming Vectors
  * Multiplying Matrices


