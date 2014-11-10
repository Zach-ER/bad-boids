from boids import update_boids
from nose.tools import assert_almost_equal
import os
import yaml
import boids as b

def test_bad_boids_regression():
    regression_data=yaml.load(open(os.path.join(os.path.dirname(__file__),'fixture.yml')))
    boid_data=regression_data["before"]
    update_boids(boid_data)
    for after,before in zip(regression_data["after"],boid_data):
        for after_value,before_value in zip(after,before): 
            assert_almost_equal(after_value,before_value,delta=0.01)
	
def test_dont_crash():
    xvs,yvs,xs,ys  = [[0,1],[2,3],[0,0],[1,2]]
    xs,ys= b.dont_crash(xs,ys,xvs,yvs)
    assert xs == [0,1] and ys == [1,4]

def test_update_positions():
    xvs,yvs,xs,ys  = [[0,1],[2,3],[0,0],[1,2]]
    xs,ys= b.update_positions(xs,ys,xvs,yvs)
    assert xs == [0,1] and ys == [3,5]

def test_sync_speed():
    xvs,yvs,xs,ys  = [[0,1],[2,3],[0,0],[1,2]]
    xs,ys= b.sync_speed(xs,ys,xvs,yvs)
    assert xvs == [0.0625, 0.94140625] and yvs == [2.0625, 2.94140625]

def test_move_to_middle():
    xvs,xs  = [[0,1],[0,0]]
    step_size = 0.1
    xvs= b.move_to_middle(xvs,xs,step_size)
    assert xvs == [0.0,1.0]

def test_init_boids():
    bds = b.initialise_boids()
    assert len(bds[0]) == len(bds[1]) == len(bds[2]) == len(bds[3])