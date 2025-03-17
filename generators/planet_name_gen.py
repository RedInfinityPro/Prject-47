from container.imports_library import *
current_time = time.time()
random.seed(current_time)

def GenerateName():
    # Optional prefix (e.g., "X", "Z", or "Alpha")
    prefixes = ["X", "Z", "Alpha", "Beta", "Gamma", "Delta", "Epsilon", "Omicron", "Nova", "Astro"]
    prefix = random.choice(prefixes)

    # Generate a random core name using letters and numbers
    core_length = random.randint(3, 5)  # Length of the core name
    core_name = ''.join(random.choices(string.ascii_uppercase + string.digits, k=core_length))

    # Optional suffix (e.g., "Prime", "IV", "VII")
    suffixes = ["Prime", "Major", "Minor", "IV", "VII", "B", "C", "D", "Rex", "Xenon"]
    suffix = random.choice(suffixes)

    # Combine prefix, core name, and suffix
    planet_name = f"{prefix}-{core_name}-{suffix}"
    return planet_name