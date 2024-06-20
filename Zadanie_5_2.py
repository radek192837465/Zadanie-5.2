#Udostępnienie konwersacji z ChatemGPT, w której jest obraz nie jest możliwe.
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Ustawienia animacji
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_aspect('equal')

# Ustawienia tła
fig.patch.set_facecolor('lightblue')
ax.set_facecolor('lightblue')

# Ukryj osie X i Y
ax.xaxis.set_visible(False)
ax.yaxis.set_visible(False)

# Usuń marginesy
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)

# Lista kropli deszczu
drops = []

class Drop:
    def __init__(self, x, y, size=0.1, growth=0.1):
        self.x = x
        self.y = y
        self.size = size
        self.growth = growth
        self.circle = plt.Circle((self.x, self.y), self.size, color='blue', alpha=0.5)

    def update(self):
        self.size += self.growth
        self.circle.set_radius(self.size)
        if self.size > 1.5:
            drops.remove(self)

    def add_to_axes(self, ax):
        ax.add_patch(self.circle)

def init():
    return []

def update(frame):
    if np.random.rand() < 0.3:
        drop = Drop(np.random.uniform(0, 10), np.random.uniform(0, 10))
        drop.add_to_axes(ax)
        drops.append(drop)
    
    for drop in drops:
        drop.update()

    return [drop.circle for drop in drops]

# Stworzenie animacji
ani = FuncAnimation(fig, update, frames=100, init_func=init, blit=True, repeat=True)

# Pokaż animację
plt.show()
