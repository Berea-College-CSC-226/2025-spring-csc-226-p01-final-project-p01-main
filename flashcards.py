def load_flashcards(filename):
    flashcards = []

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # Skip empty lines
            if line.strip() == '':
                continue

            # Handle markdown-style lists with asterisks
            if '*' in line:
                line = line.strip().strip('*').strip()

            # Try different separators
            if ': ' in line:
                parts = line.split(': ', 1)
            else:
                parts = line.strip().split(':', 1)

            # Check if the line has both term and definition
            if len(parts) == 2:
                term = parts[0].strip()
                definition = parts[1].strip()

                # Create a dictionary for the flashcard and add it to the list
                flashcard = {
                    'term': term,
                    'definition': definition
                }
                flashcards.append(flashcard)

    return flashcards
