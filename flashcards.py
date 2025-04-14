
def read_file_to_flashcards(filename):
    with open(filename, 'r') as file:        # Safely opens and auto-closes the file
        lines = file.readlines()

    flashcards = []
    for line in lines:
        line = line.strip()
        if line:
            term, definition = line.split(':', 1)
            flashcards.append((term.strip(), definition.strip()))
    return flashcards


flashcards = read_file_to_flashcards('programming.txt')
print(flashcards)








