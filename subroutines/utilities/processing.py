import numpy as np
import pandas as pd


class data_processing:

    def __init__(self, data):
        self.data = data

    def boxcar_center(self, n):
        a1 = pd.Series(self.data)
        moving_avg = np.array(a1.rolling(window=n, min_periods=1, center=True).mean())
        return moving_avg