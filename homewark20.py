
def all_variants(text):
    for list_1 in range(len(text) + 1):
        for list_2 in range(len(text) - list_1 + 1):
            yield text[list_2 : list_2 + list_1]

a = all_variants("abc")
for i in a:
    print(i)



