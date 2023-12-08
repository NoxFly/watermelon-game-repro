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