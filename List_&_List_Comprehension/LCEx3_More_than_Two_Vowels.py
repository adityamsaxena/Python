fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if (
    fruit.count("a") + 
    fruit.count("e") + 
    fruit.count("i") + 
    fruit.count("o") + 
    fruit.count("u")) > 2]

print(fruits_with_more_than_two_vowels)