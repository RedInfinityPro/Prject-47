from container.imports_library import *
current_time = time.time()
random.seed(current_time)

def BusinessName():
    prefixes = [
        "Nova", "Peak", "Elite", "Prime", "Core", "Vital", "Next", "Swift",
        "Bright", "Clear", "Smart", "Echo", "Alpha", "Meta", "Golden", "Silver",
        "Apex", "Summit", "Fusion", "Synergy", "Insight", "Vision", "Horizon",
        "Everest", "Omega", "Zenith", "Quantum", "Prism", "Spectrum", "Venture"
    ]
        
    # Business-related suffixes
    suffixes = [
        "Tech", "Solutions", "Systems", "Dynamics", "Innovations", "Partners",
        "Enterprises", "Group", "Networks", "Logic", "Works", "Concepts",
        "Global", "Industries", "Ventures", "Labs", "Studio", "Collective",
        "Connect", "Forge", "Capital", "Experts", "Minds", "Consulting",
        "Services", "Wave", "Point", "Hub", "Nexus", "Matrix"
    ]
        
    # Business modifiers (optional)
    modifiers = [
        "Pro", "Plus", "Max", "Ultra", "Advanced", "Premium", "Superior",
        "Strategic", "Innovative", "Creative", "Digital", "Modern", "Global",
        "Integrated", "Unified", "Central", "Direct", "Dynamic", "Sustainable",
        "Reliable", "", "", "", ""  # Empty strings to make modifiers optional
    ]
        
    # Business domains/industries
    domains = [
        "Finance", "Health", "Data", "Cloud", "Mobile", "Web", "Cyber",
        "Media", "Energy", "Design", "Legal", "Supply", "Market", "Food",
        "Software", "Hardware", "Retail", "Medical", "Edu", "Bio", "Green",
        "Eco", "AI", "Smart", "Virtual", "Digital", "", "", "", ""  # Empty strings to make domains optional
    ]
        
    # Generate name with various patterns
    pattern = random.choice([
        lambda: f"{random.choice(prefixes)} {random.choice(suffixes)}",
        lambda: f"{random.choice(prefixes)}{random.choice(suffixes)}",
        lambda: f"{random.choice(domains)}{random.choice(suffixes)}",
        lambda: f"{random.choice(prefixes)} {random.choice(domains)}",
        lambda: f"{random.choice(prefixes)}{random.choice(modifiers)} {random.choice(suffixes)}",
        lambda: f"{random.choice(domains)} {random.choice(suffixes)}",
        lambda: f"{random.choice(prefixes)} {random.choice(domains)} {random.choice(suffixes)}"
    ])
        
    return pattern()