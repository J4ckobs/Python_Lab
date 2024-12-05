import ahocorasick

def build_automaton(patterns):

    A = ahocorasick.Automaton()
    for idx, key in enumerate(patterns):
        A.add_word(key, (idx, key))

    A.make_automaton()
    return A

def search_patterns(text, automaton):
    results = []
    for end_idx, (insert_order, original_value) in automaton.iter(text):
        start_idx = end_idx - len(original_value) + 1
        results.append((start_idx, end_idx, original_value))
    return results

# Przykładowe wzorce
patterns = ["he", "she", "his", "hers"]

# Tworzenie automatu
automaton = build_automaton(patterns)

# Tekst do przeszukania
text = "ahishers"

# Wyszukiwanie wzorców w tekście
matches = search_patterns(text, automaton)

for start_idx, end_idx, pattern in matches:
    print(f"Znaleziono wzorzec '{pattern}' od indeksu {start_idx} do {end_idx}")
