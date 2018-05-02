# Round 1B 2018 - C. Transmutation
# https://codejam.withgoogle.com/2018/challenges/0000000000007764/dashboard/000000000003675c 

from copy import deepcopy

class Recipe:
    def __init__(self, m, r1, r2):
        self.m = m
        self.vector = [0] * m
        self.vector[r1] = 1
        self.vector[r2] = 1

    def __repr__(self):
        return str(self.vector)

    def __getitem__(self, idx):
        return self.vector[idx]

    def __setitem__(self, idx, val):
        self.vector[idx] = val

    def __add__(self, other):
        r = Recipe(self.m, 0, 0)
        r.vector = [a + b 
            for a, b in zip(self.vector, other.vector)
        ]
        return r

    def __mul__(self, integer):
        r = Recipe(self.m, 0, 0)
        r.vector = [integer * x for x in self.vector]
        return r

    def __rmul__(self, integer):
        return self.__mul__(integer)

    def __deepcopy__(self, memodict={}):
        copy_object = Recipe(self.m, 0, 0)
        copy_object.vector = self.vector
        return copy_object

def get_recipes(m):
    return [
        Recipe(m, *map(lambda x: int(x)-1, input().split()))
        for _ in range(m)
    ]

def find_debt(grams):
    return next(
        (i for i, gram in enumerate(grams)
           if  gram < 0),
        -1
    )

def update_grams(grams, recipe, debt_gram, debt_idx) -> None:
    # print('updating grams', grams)
    # print('recipe', recipe)
    if recipe[debt_idx]:
        raise RuntimeError

    for i, metal in enumerate(recipe):
        if metal > 0:
            grams[i] += metal * debt_gram
    grams[debt_idx] = 0

def update_recipes(recipes, debt_idx):
    debt_recipe = recipes[debt_idx]
    # print('updating recipe', debt_recipe)

    for i, recipe in enumerate(recipes):
        debt_metal = recipe[debt_idx]
        if debt_metal:
            recipe += debt_metal * debt_recipe
            recipe[debt_idx] = 0
            recipes[i] = recipe

def check(recipes, grams, target):
    recipes = deepcopy(recipes)
    grams = grams[:]

    grams[0] -= target
    if grams[0] > 0: return True

    debt_idx = find_debt(grams)
    while debt_idx != -1:
        # print('grams:', grams)
        # print('debt_idx:', debt_idx)

        try:
            update_grams(grams, recipes[debt_idx], grams[debt_idx], debt_idx)
            # print('updated grams:', grams)
        except RuntimeError:
            return False
        
        update_recipes(recipes, debt_idx)
        # print('updated recipes:', recipes)

        debt_idx = find_debt(grams)

    return True

def solve(m, recipes, grams) -> int:
    # pprint(recipes)
    # print(check(recipes, grams, 5))
    lo, hi = 0, sum(grams)

    while lo <= hi:
        mid = (lo + hi) // 2
        # print('binary checking:', lo, mid, hi)
        if check(recipes, grams, mid):
            lo = mid + 1
        else:
            hi = mid - 1

    return lo-1

### Remember to delete tests and scaffolding before submission
file = open('sample.in')
input = file.readline

num_cases = int(input())
for case in range(1, num_cases+1):
    m = int(input())
    recipes = get_recipes(m)
    grams = [*map(int, input().split())]
    result = solve(m, recipes, grams)

    output = 'Case #%s: %s' %(case, result)
    print(output)

file.close()