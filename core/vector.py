from math import sqrt


class Vector2:
    def __init__(self, x: float = 0.0, y: float = 0.0):
        self.x = x
        self.y = y

    def set(self, x: float, y: float) -> 'Vector2':
        self.x = x
        self.y = y
        return self
    
    def tuple(self) -> tuple[float, float]:
        return (self.x, self.y)
    
    def dist(self, other: 'Vector2') -> float:
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx * dx + dy * dy)
    
    def sub(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x - other.x, self.y - other.y)
    
    def normalize_ip(self) -> 'Vector2':
        magnitude = sqrt(self.x * self.x + self.y * self.y)
        self.x /= magnitude
        self.y /= magnitude
        return self
    
    def mult(self, scalar: float) -> 'Vector2':
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __str__(self) -> str:
        return f"Vector2({self.x}, {self.y})"
    
    def __repr__(self) -> str:
        return self.__str__()
    
    def add(self, other: 'Vector2') -> 'Vector2':
        return Vector2(self.x + other.x, self.y + other.y)