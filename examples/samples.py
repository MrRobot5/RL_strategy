"""

@since 2023年12月8日 14:23:28
"""
import pandas as pd

if __name__ == '__main__':
    s = pd.Series(['a', 'a', 'b', 'c'])
    s.describe()

    data = pd.read_csv('https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv')
    data.describe()
