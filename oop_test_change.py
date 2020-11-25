import random
from urllib.request import urlopen
import sys

WORD_URL = "https://learncodethehardway.org/words.txt"
WORDS = []

PHRASES = {
    "class %%%(%%%):":
        "Make a class named %%% that is-a %%%.",
    "class %%%(object):\n\tdef __int__(self,***)":
        "class %%% has-a __init__ that takes self and *** params.",
    "class %%%(object):\n\tdef ***(self, @@@)":
        "class %%% has-a function *** that take self and @@@ params.",
    "*** = %%%()":
        "set *** to an instance of class %%%.",
    "***.***(@@@)":
        "From *** get the *** function,call it with params self, @@@.",
    "***.*** = '***'":
        "From *** get the *** attribute and set it to '***'."
}

# do they wnato to drill phrases first
if len(sys.argv) == 2 and sys.argv[1] == "english":
    PHRASE_FIRST = True
else:
    PHRASE_FIRST = False

# load up the words from the website
#for word in urlopen(WORD_URL).readlines():
for word in open("words.txt").readlines():
    WORDS.append(str(word.strip()))


def convert(snippet, phrase):
    print(snippet)
    print("-" * 10)
    print(phrase)
    print("-" * 10)
    x = snippet.count("%%%")
    print(x)
    print("-" * 10)
    class_names = [w.capitalize() for w in 
                    random.sample(WORDS, x)]
                    
    print(class_names)
    xx = snippet.count("***")
    print(xx)
    print("-" * 10)
    other_names = random.sample(WORDS, xx)
    print(other_names)
    results = []
    param_names = []

    for i in range(0, snippet.count("@@@")):
        param_count = random.randint(1,3)
        param_names.append(', '.join(
            random.sample(WORDS, param_count)))
    
    for sentence in snippet, phrase:
        result = sentence[:]

        # fake class names
        for word in class_names:
            result = result.replace("%%%", word, 1)
        
        # fake other names
        for word in other_names:
            result = result.replace("***", word , 1)
        
        # fake parameter lists
        for word in param_names:
            result = result.replace("@@@", word, 1)
        
        results.append(result)
    
    return results

# keep going until they hit CTRL-D
try:
    x =1
    while x:
        x -= 1
        print(PHRASES)
        print("-" * 10)
        print(PHRASES.keys())
        print("-" * 10)
        snippets = list(PHRASES.keys())
        print(snippets)
        random.shuffle(snippets)

        for snippet in snippets:
            phrase = PHRASES[snippet]
            print("-" * 10)
            print(phrase)
            question, answer = convert(snippet, phrase)
            if PHRASE_FIRST:
                question,answer = answer, question

                print(question)

                input("> ")
                print(f"ANSWER: {answer}\n\n")
except EOFError:
    print("\nBye")
