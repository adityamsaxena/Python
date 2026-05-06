fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_only_two_vowels = [fruit for fruit in fruits if (
    fruit.count("a") + 
    fruit.count("e") + 
    fruit.count("i") + 
    fruit.count("o") + 
    fruit.count("u")) == 2]

print(fruits_with_only_two_vowels)

#Alternate Solution:-->
# fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
# vowels = "aeiou"
# fruits_with_only_two_vowels = new_fruit = [item for item in fruits if sum(ch in vowels for ch in item) == 2]
# print(fruits_with_only_two_vowels)
