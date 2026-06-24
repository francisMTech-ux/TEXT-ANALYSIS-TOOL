# Text Analysis Tool
# Author: FRANCIS NJAU
# Date: June 24, 2026

# Function to validate non-empty input
def get_non_empty_input(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input:
            return user_input
        else:
            print("Input cannot be empty. Please try again.")

# Main Program
def main():
    print("=== Text Analysis Tool ===")

    # 1. User Input
    text = get_non_empty_input("Enter a paragraph or lengthy text: ")

    # Normalize text for case-insensitive operations
    normalized_text = text.lower()

    # 2. Character Count
    char_count = len(text)
    print(f"\nTotal number of characters: {char_count}")

    # 3. Word Count
    words = text.split()
    word_count = len(words)
    print(f"Total number of words: {word_count}")

    # 4. Most Common Character
    from collections import Counter
    char_counter = Counter(normalized_text.replace(" ", ""))  # ignore spaces
    most_common_char, freq = char_counter.most_common(1)[0]
    print(f"Most common character: '{most_common_char}' (appears {freq} times)")

    # 5. Character Frequency
    char_input = get_non_empty_input("Enter a character to check frequency: ").lower()
    if len(char_input) != 1:
        print("Please enter only one character.")
    else:
        char_freq = normalized_text.count(char_input)
        print(f"Frequency of '{char_input}': {char_freq}")

    # 6. Word Frequency
    word_input = get_non_empty_input("Enter a word to check frequency: ").lower()
    word_freq = sum(1 for w in words if w.lower() == word_input)
    print(f"Frequency of word '{word_input}': {word_freq}")

    # 7. Unique Words
    unique_words = set(w.lower() for w in words)
    print(f"Number of unique words: {len(unique_words)}")

    print("\n=== Analysis Complete ===")

# Run the program
if __name__ == "__main__":
    main()