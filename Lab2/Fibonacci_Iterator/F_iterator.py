class Fibonacci:
    def __init__(self, steps):
        self.steps = steps
        self.current = 0
        self.next_num = 1
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count >= self.steps:
            raise StopIteration()

        result = self.current
        self.current, self.next_num = self.next_num, self.current + self.next_num
        self.count += 1

        return result