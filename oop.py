import numpy as np
import matplotlib.pyplot as plt


# probability of circularization or concatemrization = f(len, concentration)

class DNA:
    id_counter = 0
    # id
    # head = [0, 0]
    self.tail = self.head.copy()
    length = 0
    path = [[0, 0]]

    def __init__(self, length=0, head=None):
        # print(type(self))
        type(self).id_counter += 1
        self.id = self.id_counter
        self.length = length
        if head is None:
            self.head = [0, 0]
        if length != 0:
            for i in range(length):
                print(i)
                if np.random.choice([1, -1]) == 1:
                    self.tail[0] += np.random.choice([1, -1])
                else:
                    self.tail[1] += np.random.choice([1, -1])
                print(self.tail)
                self.path.append([self.tail[0], self.tail[1]])

    def get_all(self):
        print(f"DNA {self.id}")
        print(f"head is at {self.head}")
        print(f"tail is at {self.tail}")
        print(f"length is {self.length}")
        print("--------------------------")
        return self.id, self.head, self.tail, self.length, self.path


if __name__ == "__main__":
    dna1 = DNA()
    dna2 = DNA(5)
    dna3 = DNA(12)
    print(dna1.tail, dna2.tail, dna3.tail)
    dna1.get_all()
    dna2.get_all()
    dna3.get_all()
