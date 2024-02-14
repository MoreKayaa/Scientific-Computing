# Favian Mokaya Imbera SCT211-0022/2021
# Project 01 
# This program basically uses arrays to eliminate redundancy on repeated lines. It also calls a function for the refrain. The recursive function print_verse() prints each verse in the array.
def old_woman_swallowed_a_fly():
    def refrain():
        return "I don't know why she swallowed that fly,\n" \
               "Perhaps she'll die.\n"
    repeated_sentences = ["She swallowed the spider to catch the fly,",
                          "She swallowed the bird to catch the spider,",
                          "She swallowed the cat to catch the bird,",
                          "She swallowed the dog to catch the cat,",]
    verses = [
        "There was an old woman who swallowed a fly.",
        refrain(),
        "There was an old woman who swallowed a spider,",
        "That wriggled and iggled and jiggled inside her.",
        repeated_sentences[0],
        refrain(),
        "There was an old woman who swallowed a bird,",
        "How absurd to swallow a bird.",
        repeated_sentences[1],
        repeated_sentences[0],
        refrain(),
        "There was an old woman who swallowed a cat,",
        "Imagine that to swallow a cat.",
        repeated_sentences[2],
        repeated_sentences[1],
        repeated_sentences[0],
        refrain(), 
        "There was an old woman who swallowed a dog,",
        "What a hog to swallow a dog.",
        repeated_sentences[3],
        repeated_sentences[2],
        repeated_sentences[1],
        repeated_sentences[0],
        refrain(),
        "There was an old lady who swallowed a snake,",
        "What a mistake to swallow a snake.",
        "She swallowed the snake to catch the dog,",
        repeated_sentences[3],
        repeated_sentences[2],
        repeated_sentences[1],
        repeated_sentences[0],
        refrain(),
        "There was an old woman who swallowed a horse,",
        "She died of course."
    ]

    # Using recursion to print each verse
    def print_verse(verse_index):
        if verse_index < len(verses):
            print(verses[verse_index])
            print_verse(verse_index + 1)

    print_verse(0)


if __name__ == "__main__":
    old_woman_swallowed_a_fly()
