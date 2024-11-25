#### Evalutation Function fx = sum of wi * xi for i = 0 to n
#### Activation Function: gx = 1 if fx > 0 else 0
#### error = y - gx
# Input

| X0 | X1 | X2 | Y |
|---|---|---|---|
| 1 | 0 | 2 | 1 |
| 1 | 2 | 0 | 0 |
| 1 | 1 | 1 | 1 |
| 1 | 3 | 0.5 | 0 |
| 1 | 1 | 2.5 | 1 |


### Initial weights: [0. 0. 0.]

## Epoch 1:
### Sample: [1. 0. 2.], f(x): 0.00, g(x): 0, Target: 1, Error: 1, Updated weights: [1. 0. 2.]
### Sample: [1. 2. 0.], f(x): 1.00, g(x): 1, Target: 0, Error: -1, Updated weights: [ 0. -2.  2.]
### Sample: [1. 1. 1.], f(x): 0.00, g(x): 0, Target: 1, Error: 1, Updated weights: [ 1. -1.  3.]
### Sample: [1.  3.  0.5], f(x): -0.50, g(x): 0, Target: 0, Error: 0
### Sample: [1.  1.  2.5], f(x): 7.50, g(x): 1, Target: 1, Error: 0

| Sample     | f(x) | g(x) | Target | Error | Updated Weights |
|------------|-----|---|---|-------|-----------------|
| [1, 0, 2]  | 0   | 0 | 1 | 1     | [1, 0, 2]       |
| [1, 2 , 0] | 1   | 1 | 0 | -1    | [0, -2, 2]      |
| [ 1, 1, 1] | 0   | 0 | 1 | 1     | [1, -1, 3]      |
| [1, 3, 0.5] | -0.5 | 0 | 0 | 0     | [1, -1, 3]      |
| [1, 1, 2.5] | 7.5 | 1 | 1 | 0     | [1, -1, 3]      |

## Epoch 2:
### Sample: [1. 0. 2.], f(x): 7.00, g(x): 1, Target: 1, Error: 0
### Sample: [1. 2. 0.], f(x): -1.00, g(x): 0, Target: 0, Error: 0
### Sample: [1. 1. 1.], f(x): 3.00, g(x): 1, Target: 1, Error: 0
### Sample: [1.  3.  0.5], f(x): -0.50, g(x): 0, Target: 0, Error: 0
### Sample: [1.  1.  2.5], f(x): 7.50, g(x): 1, Target: 1, Error: 0


| Sample     | f(x) | g(x) | Target | Error | Updated Weights |
|------------|------|------|---|-------|------------|
| [1, 0, 2]  | 7    | 1    | 1 | 0     | [1, -1, 3] |
| [1, 2 , 0] | -1   | 0    | 0 | 0     | [1, -1, 3] |
| [ 1, 1, 1] | 3    | 1    | 1 | 0     | [1, -1, 3] |
| [1, 3, 0.5] | -0.5 | 0    | 0 | 0     | [1, -1, 3] |
| [1, 1, 2.5] | 7.5  | 1    | 1 | 0     | [1, -1, 3] |



### => Error converged to 0 so the Weights converged.

## Final weights: [ 1. -1.  3.]
## Total epochs: 2