import pandas as pd
import numpy as np
import matplotlib.pyplot as mpt


df = pd.DataFrame(np.random.rand(10, 3), columns=['a', 'b', 'c'])
df.plot.bar()
mpt.show()


