import numpy as np

class Point:
    def __init__(self, x_: float, y_: float, z_: float):
        self.x = x_
        self.y = y_
        self.z = z_
        
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        
        return Point(new_x, new_y, new_z)
        
    def __sub__(self, other):
        new_x = self.x - other.x
        new_y = self.y - other.y
        new_z = self.z - other.z
        
        return Point(new_x, new_y, new_z)
    
    def __truediv__(self, other):
        new_x = self.x / other
        new_y = self.y / other
        new_z = self.z / other
        
        return Point(new_x, new_y, new_z)

def point_abs(A: Point):
    return np.sqrt(A.x**2 + A.y**2 + A.z**2)

def cross_product(A: Point, B: Point):
    return Point(A.y * B.z - A.z * B.y, A.z * B.x - A.x * B.z, A.x * B.y - B.y * A.x)

def dot_product(A: Point, B: Point):
    return A.x * B.x + A.y * B.y + A.z * B.z
    
class Plane:
    def __init__(self, p1_: Point, p2_: Point, p3_: Point):
        self.p1 = p1_
        self.p2 = p2_
        self.p3 = p3_
        
        self.norm = cross_product(p2_ - p1_, p3_ - p1_) / point_abs(cross_product(p2_ - p1_, p3_ - p1_))
        
    # TO-DO: define a method to determine which side of a plane a point is on
    # Possible idea: find vector between one of three points in plane and point of interest, then find projection onto normal vector
    
    def point_outside(self, p: Point):
        proj = dot_product(p - self.p1, self.norm)
        
        if proj > 0:
            return True
        else:
            return False
        
    def extract_point(self, p: Point, step_size):
        new_point = p
        point_loc = self.point_outside(p)
        
        while not point_loc:
            new_point = Point(new_point.x + step_size * self.norm.x,
                             new_point.y + step_size * self.norm.y,
                             new_point.z + step_size * self.norm.z)
            
            point_loc = self.point_outside(p)
            
        return new_point
    
def main():
    point1 = Point(0.0, 0.0, 0.0)
    point2 = Point(1.0, 0.0, 0.0)
    point3 = Point (0.0, 1.0, 0.0)
    ex_plane = Plane(point1, point2, point3)
    ex_point = Point(0.5, 0.5, -0.5)
    
    extracted_point = ex_plane.extract_point(ex_point, 0.01)
    
    print(extracted_point.x, extracted_point.y, extracted_point.z)
    
if __name__ == "__main__":
    main()
