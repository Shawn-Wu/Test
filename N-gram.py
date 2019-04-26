import ngram

correct_data = []
dict_data = []
misspell_data = []
with open('correct.txt', 'rt') as f:
    for line in f:
        correct_data.append(line.strip())
with open('dict.txt', 'rt') as f:
    for line in f:
        dict_data.append(line.strip())
with open('misspell.txt', 'rt') as f:
    for line in f:
        misspell_data.append(line.strip())

f = open('3_gram_output.txt', 'x')
len_misspell = len(misspell_data)
len_dict = len(dict_data)
for i in range(len_misspell):
    print((i / len_misspell) * 100)
    print(misspell_data[i])
    output = ""
    value_list = []
    for j in range(len_dict):
        ngram_value = ngram.NGram.compare(misspell_data[i], dict_data[j], N=3)
        value_list.append(ngram_value)
    max_value = max(value_list)
    for k in range(len(value_list)):
        if value_list[k] == max_value:
            output = dict_data[k] + " "
    output = output + "\n"
    print(output)
    f.writelines(output)
f.close()