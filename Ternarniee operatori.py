word = 'slovo'
result = []

for i in range(len(word)):
    letter = word[i].lower() if i%2!=0 else word[i].upper()
    result.append(letter)

result = ''.join(result)
print(result)

# print('Hello world!')