"""
A deliberately bad implementation of [Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
"""

from matplotlib import pyplot as plt
from matplotlib import animation
import random

# Deliberately terrible code for teaching purposes

def initialise_boids():
    boids_x=[random.uniform(-450,50.0) for x in range(50)]
    boids_y=[random.uniform(300.0,600.0) for x in range(50)]
    boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
    boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]
    return (boids_x,boids_y,boid_x_velocities,boid_y_velocities)

def init_figure():
    figure=plt.figure()
    axes=plt.axes(xlim=(-500,1500), ylim=(-500,1500))
    scatter=axes.scatter(boids[0],boids[1])
    return figure, scatter

# Fly towards the middle
def move_to_middle(velocs,coords,step_size):
    for i in range(len(coords)):
        for j in range(len(coords)):
            velocs[i] += (coords[j]-coords[i])*step_size/len(coords)
    return velocs

# fly away from nearby boids
def dont_crash(xs,ys,xvs,yvs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 100:
                xvs[i]+=+(xs[i]-xs[j])
                yvs[i]+=+(ys[i]-ys[j])
    return xvs, yvs

# Try to match speed with nearby boids
def sync_speed(xs,ys,xvs,yvs):
    for i in range(len(xs)):
        for j in range(len(xs)):
            if (xs[j]-xs[i])**2 + (ys[j]-ys[i])**2 < 10000:
                xvs[i] += (xvs[j]-xvs[i])*0.125/len(xs)
                yvs[i] += (yvs[j]-yvs[i])*0.125/len(xs)
    return xvs, yvs

# move the boids
def update_positions(xs,ys,xvs,yvs):
    for i in range(len(xs)):
        xs[i]=xs[i]+xvs[i]
        ys[i]=ys[i]+yvs[i]
    return xs,ys

def update_boids(boids):
    xs,ys,xvs,yvs=boids
    step_size = 0.01
	# Fly towards the middle
    xvs = move_to_middle(xvs,xs,step_size)
    yvs = move_to_middle(yvs,ys,step_size)
	# Fly away from nearby boids
    xvs,yvs = dont_crash(xs,ys,xvs,yvs)
    # Try to match speed with nearby boids
    xvs,yvs = sync_speed(xs,ys,xvs,yvs)
	# Move according to velocities
    xs,ys = update_positions(xs,ys,xvs,yvs)


boids = initialise_boids()
figure,scatter = init_figure()

def animate(frame):
   update_boids(boids)
   scatter.set_offsets(zip(boids[0],boids[1]))


anim = animation.FuncAnimation(figure, animate,
                               frames=50, interval=50)

if __name__ == "__main__":
    plt.show()
