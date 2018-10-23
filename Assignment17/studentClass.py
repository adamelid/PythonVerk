class Student:
    score = 10
    def add_score(self):
        self.score += 10

    def decrease_score(self):
        self.score -= 10

    def __str__(self):
        return str(self.score)