import random

# Define lists for pharmaceutical sounding prefixes and suffixes
prefixes = ["Alpra", "Metro", "Pento", "Hydro", "Cefu", "Doxa", "Lora", "Amlo"]
suffixes = ["zolam", "pril", "barb", "sartan", "mycin", "dipine", "floxacin", "lone"]

# List of common drug side effects
side_effects = ["Nausea", "Headache", "Dizziness", "Dry mouth", "Sleepiness", "Constipation", "Weight gain", "Blurry vision"]

def generate_medication():
    """Generate random medication data."""
    # Construct a random medication name
    med_name = random.choice(prefixes) + random.choice(suffixes)
    
    # Random efficacy percentage
    efficacy = random.uniform(50, 99)  # Generates a float between 50 and 99
    
    # Random side effects - select between 1 and 4 side effects for a medication
    adverse_event = random.sample(side_effects, k=random.randint(1, 4))
    
    return {
        "Medication Name": med_name,
        "Efficacy (%)": round(efficacy, 2),
        "Adverse Event": adverse_event
    }

# Test the generator
for _ in range(10):
    print(generate_medication())

# Sample output:
# {'Medication Name': 'Pentofloxacin', 'Efficacy (%)': 95.11, 'Adverse Event': ['Nausea', 'Dizziness']}
# {'Medication Name': 'Lorapril', 'Efficacy (%)': 98.61, 'Adverse Event': ['Weight gain', 'Dry mouth', 'Blurry vision']}
# {'Medication Name': 'Cefumycin', 'Efficacy (%)': 97.75, 'Adverse Event': ['Weight gain', 'Dizziness', 'Sleepiness']}
