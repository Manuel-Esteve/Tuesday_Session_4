alphabet = " abcdefghijklmnopqrstuvwxyz"
vowels = "aeiou"
message = ""
with open("secret.txt") as f:
    for line in f:
        n_vowels = 0
        for v in vowels:
            n_vowels += line.count(v)
        print(alphabet[n_vowels], end="")
        # for each vowel inside vowels
        #count the number of appearances (.count) and add inside n.vowels
        #index alphabet[n.vowels] that is one letter
