"""

CSR Matrix
We can create CSR matrix by passing an arrray into function scipy.sparse.csr_matrix().



Example explanatiosn:

The example Below returns:


  (0, 5)	1
  (0, 6)	1
  (0, 8)	2

From the result we can see that there are 3 items with value.

The 1. item is in row 0 position 5 and has the value 1.

The 2. item is in row 0 position 6 and has the value 1.

The 3. item is in row 0 position 8 and has the value 2.


"""


import numpy as np
from scipy.sparse import csr_matrix

arr = np.array([0, 0, 0, 0, 0, 1, 1, 0, 2])

print(csr_matrix(arr))