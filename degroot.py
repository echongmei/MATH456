import operator
import copy
from collections import defaultdict


model = defaultdict(dict)
model[0][1] = 1/2
model[0][9] = 1/2

model[1][0] = 1/3
model[1][2] = 1/3
model[1][8] = 1/3

model[2][1] = 1/3
model[2][3] = 1/3
model[2][7] = 1/3

model[3][2] = 1/3
model[3][4] = 1/3
model[3][6] = 1/3

model[4][3] = 1/2
model[4][5] = 1/2

model[5][4] = 1/2
model[5][6] = 1/2

model[6][3] = 1/3
model[6][5] = 1/3
model[6][7] = 1/3

model[7][2] = 1/3
model[7][6] = 1/3
model[7][8] = 1/3

model[8][1] = 1/3
model[8][7] = 1/3
model[8][9] = 1/3

model[9][0] = 1/2
model[9][8] = 1/2

print(model)

def converge(x, y):
    return x == y
def degroot(model, belief_vector):
    old_vector = [0,0,0,0,0,0,0,0,0,0]
    new_vector = belief_vector
    it = 0
    conv = True
    while conv:
        old_vector = copy.deepcopy(new_vector)
        it +=1
        for i in range(len(old_vector)):
            avg= 0
            di = model[i]
            for key, outdegree in di.items():
                avg += outdegree*old_vector[key]
            new_vector[i] = round(avg, 4)
        print("b(", it, ") : ", new_vector)
        if (converge(old_vector, new_vector)):
            conv =  False
    return

degroot(model, [1,1,0,0,0,0,0,0,1,1])
