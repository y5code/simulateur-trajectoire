import numpy as np



g = 9.81       

m = 0.045      

v0 = 45.0      

alpha = 45.0   

dt = 0.01      



x, y = [0.0], [0.0]

vx = [v0 * np.cos(np.radians(alpha))]

vy = [v0 * np.sin(np.radians(alpha))]



while y[-1] >= 0:

    x.append(x[-1] + vx[-1] * dt)

    y.append(y[-1] + vy[-1] * dt)

    vx.append(vx[-1])

    vy.append(vy[-1] - g * dt)



print(f"Simulation terminee. Portee : {x[-1]:.2f} metres.")

