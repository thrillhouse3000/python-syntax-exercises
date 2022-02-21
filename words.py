def print_matching_words(words, starting_letters):
    """
    returns a list of upper-case words that start with the specified letters
    def print_matching_words([words],[starting-letters])
    """
    for word in words:
        word = word.lower()
        for letter in starting_letters:
            letter = letter.lower()
            if word.startswith(letter):
                print(word.upper())

print_matching_words(["Hello", "Hey", "goodbye", "Yo", "Yes"], ['h'])