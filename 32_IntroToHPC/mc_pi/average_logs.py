import os
import numpy as np

pivals = []
for fname in os.listdir('logs'):
    with open(os.path.join('logs', fname), 'r') as f:
        pivals.append(float(f.read()))

pi = np.array(pivals).mean()
print(f'{pi:.16f}')
