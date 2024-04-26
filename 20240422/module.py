class Maximum:
    def maximum(x: float, y: float) -> float:
        answer: float = x if x > y else y
        return answer
    

class Minimum:
    def minimum(x: float, y: float) -> float:
        answer: float = x if x < y else y
        return answer