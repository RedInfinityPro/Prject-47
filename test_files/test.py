import random

def biased_random(min_val, max_val, mode, bias_strength=2):
    choices = [random.randint(min_val, max_val) for _ in range(bias_strength)]
    choices.append(mode)
    return random.choice(choices)
print(biased_random(0,5,3))