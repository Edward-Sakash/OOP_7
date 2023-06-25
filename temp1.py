import numpy as np
from scipy.integrate import odeint
import plotly.graph_objects as go

def LorenzMod1(XYZ, t, alpha, beta, xi, delta):
    x, y, z = XYZ
    x_dt = -alpha*x + y*y - z*z + alpha*xi
    y_dt = x*(y - beta*z) + delta
    z_dt = -z + x*(beta*y + z)
    return x_dt, y_dt, z_dt

alpha = 0.1
beta = 4
xi = 14
delta = 0.08

x_0, y_0, z_0 = 0, 1, 0

tmax, n = 100, 50000

t = np.linspace(0, tmax, n)
f = odeint(LorenzMod1, (x_0, y_0, z_0), t, args=(alpha, beta, xi, delta))
X, Y, Z = f.T

c = np.linspace(0, 1, n)

DATA = go.Scatter3d(x=X, y=Y, z=Z,
                    line=dict(color= c,
                              width=3,
                              colorscale="Cividis"),
                    mode='lines')

fig = go.Figure(data=DATA)

fig.update_layout(width=1000, height=1000,
                  margin=dict(r=10, l=10, b=10, t=10),
                  paper_bgcolor='rgb(0,0,0)',
                  scene=dict(camera=dict(up=dict(x=0, y=0, z=1),
                                         eye=dict(x=0, y=1, z=1)),
                             aspectratio = dict(x=1, y=1, z=1),
                             aspectmode = 'manual',
                             xaxis=dict(visible=False),
                             yaxis=dict(visible=False),
                             zaxis=dict(visible=False)
                            )
                 )

fig.show()
