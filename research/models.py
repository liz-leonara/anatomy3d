import numpy as np

# use numpy ndarrays of length 3 to represents points in Cartesian 3D space

class plane:
    def __init__(self, p1_: np.ndarray, p2_: np.ndarray, p3_ = np.ndarray):
        self.p1 = p1_
        self.p2 = p2_
        self.p3 = p3_
        
        self.norm = np.cross(p2_ - p1_, p3_ - p1_)
        self.norm /= np.linalg.norm(self.norm)
        
    def outside(self, p: np.ndarray):
        proj = np.dot(p, self.norm)
        
        if proj > 0:
            return True
        else:
            return False
        
    def extract(self, p: np.ndarray, step: float):
        new_p = p
        
        while not self.outside(new_p):
            new_p = new_p + step * self.norm
            
        return new_p
    
class model:
    def __init__(self, planes_: np.ndarray):
        self.planes = planes_
        
    # To-do: implement a method to take array of points and determine object's planes
