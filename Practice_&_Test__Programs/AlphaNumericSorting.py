def alpha_numeric_sorting(str):
    alphabets = []
    numbers = []
    for ch in str:
        if ch.isalpha():
            alphabets.append(ch)
        else:
            numbers.append(ch)
    final_ordered_list = sorted(alphabets) + sorted(numbers)
    output = ''.join(final_ordered_list)
    print(output)
alpha_numeric_sorting('A123B')