import numpy as np

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

def main():
    ex_p1 = np.array([0, 0, 0])
    ex_p2 = np.array([1.0, 0, 0])
    ex_p3 = np.array([0, 1.0, 0])
    ex_p = np.array([0.25, 0.25, -1])
    ex_plane = plane(ex_p1, ex_p2, ex_p3)
    
    print(ex_plane.extract(ex_p, 0.01))

if __name__ == "__main__":
    main()
