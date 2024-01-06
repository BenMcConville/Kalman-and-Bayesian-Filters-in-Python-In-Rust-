import matplotlib.pyplot as plt
from numpy.random import randn

dataPoints = 100

def gen_data(x0, dx, count, noise_factor=1.0):
   return [x0 + (dx * i) + (randn() * noise_factor) for i in range(count)] 

def GHFilter(data, timeStep=1.0, dx=1.0, x0=0.0, g=1.0, h=1.0):
    predictions, estimates = [], [x0]
    estimate = x0
    for x in data:
        prediction = estimate + (timeStep * dx)
        estimate   = prediction + ((x - prediction) * g)
        dx         = dx         + (((x - prediction) / timeStep) * h)

        estimates.append(estimate)
    
    return estimates

data = gen_data(155.0, 1.0, dataPoints) 
results = GHFilter(data, 1.0, 1.0, 155.0, 0.25, 0.33)

plt.plot(results)
plt.plot(range(dataPoints), data, 'o')
plt.legend(['Estimates', 'Data'])
plt.show()
