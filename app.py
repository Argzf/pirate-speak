import re

def translate_to_pirate(text):
    # Dictionary of pirate-themed word replacements
    pirate_words = {
        "hello": "ahoy",
        "hi": "yo-ho-ho",
        "my": "me",
        "friend": "matey",
        "sir": "matey",
        "madam": "proud beauty",
        "excuse": "arrr",
        "where": "whar",
        "is": "be",
        "the": "thar",
        "you": "ye",
        "your": "yer",
        "old": "barnacle-covered",
        "restaurant": "galley",
        "house": "ship",
        "today": "this fine day",
        "bank": "buried treasure",
        "money": "booty",
        "happy": "grog-filled",
        "drunk": "three sheets to the wind",
        "nearby": "broadside",
        "smart": "cunning",
        "dog": "parrot",
        "cat": "parrot",
        "fish": "shark bait",
        "food": "grub",
        "eat": "devour",
        "drink": "swill",
        "sleep": "take a caulk",
        "yes": "aye",
        "no": "nay",
        "please": "if ye be so kind",
        "thanks": "yo-ho-ho",
        "money": "doubloons",
        "treasure": "booty",
        "map": "chart",
        "ship": "vessel",
        "captain": "skipper",
        "crew": "scallywags",
        "enemy": "scurvy dog",
        "fight": "duel",
        "run": "sail away",
        "quickly": "smartly",
        "beautiful": "comely",
        "dangerous": "treacherous",
        "happy": "jolly",
        "sad": "scurvy",
        "hurt": "wounded",
        "safe": "shipshape",
        "help": "lend a hand",
        "kill": "send to Davy Jones' locker",
        "stop": "avast",
        "attack": "pillage",
        "city": "port",
        "town": "village",
        "road": "sea path",
        "money": "pieces of eight",
        "stupid": "addled",
        "fool": "landlubber",
        "idiot": "nincompoop",
        "joke": "jest",
        "laugh": "yo-ho-ho",
        "toilet": "head",
        "bathroom": "head",
        "money": "plunder",
        "angry": "irate",
        "run": "scurry",
        "walk": "saunter",
        "big": "mighty",
        "small": "wee",
        "strange": "bizarre",
        "smell": "stench",
        "good": "savvy",
        "bad": "rotten",
        "go": "sail",
        "come": "come aboard",
        "to": "t'",
        "with": "wit'",
        "up": "upwards",
        "down": "downwards",
        "in": "in",
        "out": "out",
        "on": "on",
        "off": "off",
        "and": "an'",
        "but": "but",
        "or": "or",
        "that": "that",
        "this": "this",
        "these": "these",
        "those": "those",
        "some": "some",
        "many": "many",
        "few": "few",
        "most": "most",
        "all": "all",
        "every": "every",
        "any": "any"
    }
    
    # Split the text into words and iterate over them
    words = re.findall(r'\b\w+\b', text)
    translated_words = []
    for word in words:
        # Convert the word to lowercase for case-insensitive matching
        lowercase_word = word.lower()
        # Check if the word needs to be translated
        if lowercase_word in pirate_words:
            # Replace the word with its pirate-themed equivalent
            translated_word = pirate_words[lowercase_word]
            # Preserve the original capitalization
            if word.istitle():
                translated_word = translated_word.title()
            elif word.isupper():
                translated_word = translated_word.upper()
            # Add the translated word to the list
            translated_words.append(translated_word)
        else:
            # Keep the original word if no translation is available
            translated_words.append(word)
    
    # Join the translated words back into a string
    translated_text = ' '.join(translated_words)
    return translated_text

# Example usage
sentence = "Hello, my friend! How are you today?"
translated_sentence = translate_to_pirate(sentence)
print(translated_sentence)
