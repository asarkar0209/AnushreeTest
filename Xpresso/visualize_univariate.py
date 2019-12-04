import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

sns.set(context='notebook', style='darkgrid', palette='deep', font='sans-serif', font_scale=1, color_codes=True, rc=None)

x = np.random.normal(size=100)


sns.distplot(x)