from container.imports_library import *

def Format_Number(num):
    """Formats large numbers with suffixes"""
    if num >= 1e6:
        suffixes = ['Mill', 'Bill','Tril','Quad', 'Quin', 'Sext', 'Sept', 'Octi', 'Noni', 'Deci', 'Unde', 'Duod', 'Tred', 'Quat', 'Quin', 'Sexd', 'Sept', 'Octo', 'Nove', 'Vigi', 'Cent']
        index = int(math.log10(num) // 3 - 2)
        return f"{num / 10**(6 + index * 3):.2f} {suffixes[index]}" if index < len(suffixes) else f"{num:.2e}"
    return f"{num:,.2f}"

def Large_Number_Random_Generator(Min_number, Max_number, round_number=0):
    unique_seed = random.seed(int.from_bytes(os.urandom(8), byteorder="big"))
    if Min_number < Max_number:
        random_number = round(random.uniform(Min_number, Max_number), round_number)
    else:
        return 0
    return random_number

def Weighted_Random(min_val, max_val, weight=3):
        # Using base as random value raised to a power creates a weighted distribution
        base = random.random() ** weight
        weighted_value = min_val + (max_val - min_val) * base
        return max(min_val, min(weighted_value, max_val))