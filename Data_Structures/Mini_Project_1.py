# Create a dictionary that contains a list of people and one interesting fact about each of them.Display each person and his or her interesting fact to the screen.
# Next, change a fact about one of the people.Also add an additional person and corresponding fact.Display the new list of people and facts.
# Run the program multiple times and notice if the order changes.

people_facts = {
    "Ada Lovelace": "Considered the first computer programmer.",
    "Alan Turing": "Helped break the Enigma code during WWII.",
    "Grace Hopper": "Popularized the term 'debugging' for fixing computer bugs."
}

# Display initial facts
for person, fact in people_facts.items():
    print(f"{person}: {fact}")

# Modify a fact
people_facts["Grace Hopper"] = "Invented the first compiler for a programming language."

# Add a new person
people_facts["Tim Berners-Lee"] = "Invented the World Wide Web."

# Display updated facts
for person, fact in people_facts.items():
    print(f"{person}: {fact}")
