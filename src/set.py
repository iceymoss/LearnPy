language = set(['c', 'c++', 'python', 'java', 'go', 'js', ])
if 'go' in language:
    print("go是世界上最好的编程语言")

language.add('c#')
print(language, len(language))
language.remove('c#')
print(language, len(language))

