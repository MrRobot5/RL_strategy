
import numpy as np
from gym import spaces

action_space = spaces.Box(low=np.array([0, 0]), high=np.array([3, 1]), dtype=np.float16)
for i in range(20):
    sample = action_space.sample()
    print(sample)
