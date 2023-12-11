from typing import List


class QuadtreePoint:
    def __init__(self, x: float, y: float, radius: float, ref):
        self.x = x
        self.y = y
        self.radius = radius
        self.ref = ref

class Quadtree:
    def __init__(self, x: float, y: float, width: float, height: float, capacity: float):
        self.boundary = (x, y, width, height)
        self.capacity = capacity
        self.circles = []
        self.divided = False

    def insert(self, circle: QuadtreePoint) -> bool:
        if not self.in_boundary(circle):
            return False

        if len(self.circles) < self.capacity:
            self.circles.append(circle)
            return True

        if not self.divided:
            self.subdivide()

        return (self.northeast.insert(circle) or
                self.northwest.insert(circle) or
                self.southeast.insert(circle) or
                self.southwest.insert(circle))

    def in_boundary(self, circle: QuadtreePoint) -> bool:
        x, y, w, h = self.boundary
        return (x - w <= circle.x <= x + w and
                y - h <= circle.y <= y + h)

    def subdivide(self) -> None:
        x, y, w, h = self.boundary
        self.northeast = Quadtree(x + w / 2, y - h / 2, w / 2, h / 2, self.capacity)
        self.northwest = Quadtree(x - w / 2, y - h / 2, w / 2, h / 2, self.capacity)
        self.southeast = Quadtree(x + w / 2, y + h / 2, w / 2, h / 2, self.capacity)
        self.southwest = Quadtree(x - w / 2, y + h / 2, w / 2, h / 2, self.capacity)
        self.divided = True

    def queryRadius(self, x: float, y: float, radius: float) -> List[QuadtreePoint]:
        points_in_radius = []

        # Check if the range intersects this quad
        if (abs(x - self.boundary[0]) > (self.boundary[2] + radius) or
            abs(y - self.boundary[1]) > (self.boundary[3] + radius)):
            return points_in_radius

        # Check objects in this quad
        for circle in self.circles:
            if ((circle.x - x)**2 + (circle.y - y)**2) <= radius**2:
                points_in_radius.append(circle)

        # If this quad can't be subdivided, return the points it contains
        if not self.divided:
            return points_in_radius

        # Otherwise, add the points from the children
        points_in_radius.extend(self.northeast.queryRadius(x, y, radius))
        points_in_radius.extend(self.northwest.queryRadius(x, y, radius))
        points_in_radius.extend(self.southeast.queryRadius(x, y, radius))
        points_in_radius.extend(self.southwest.queryRadius(x, y, radius))

        return points_in_radius