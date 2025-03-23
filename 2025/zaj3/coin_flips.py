import random

class CoinFlips:
    def __init__(self, number_of_flips):
        self.number_of_flips = number_of_flips
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter < self.number_of_flips:
            self.counter += 1
            return random.choice(["O", "R"])
        else:
            raise StopIteration

three_flips = CoinFlips(3)
print(next(three_flips))
print(next(three_flips))
print(next(three_flips))

three_flips = CoinFlips(3)

for flip in three_flips:
    print(flip)

three_flips = CoinFlips(3)
while True:
    try:
        next(three_flips)
    except StopIteration:
        print("Completed all coin flips!")
        break