def rev_str(pr_str):
    return ''.join(reversed(pr_str))

res_str = ''
with open("input.txt", 'r', encoding='UTF-8') as init_file:
    for line in init_file:
        s = []
        result = line.rstrip('\n\r')
        res = result.split(' ')
        for key in res:
            s.append(rev_str(key))
        str1 = ' '.join(s)
        res_str = res_str + str1 + '\n'

with open("input.txt", 'w', encoding='UTF-8') as result_file:
    result_file.write(res_str)