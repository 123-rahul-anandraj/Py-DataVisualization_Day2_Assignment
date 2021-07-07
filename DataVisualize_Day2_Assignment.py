#Day2 Assigment No:2

import numpy as np
import pandas as pd
import matplotlib as mplt
import matplotlib.pyplot as plt
import seaborn as sns

pd1=pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
#print(pd1)
pd1.plot.bar()
plt.title('Bar Graph Assignment-2')
plt.legend()
plt.grid()
plt.show()

