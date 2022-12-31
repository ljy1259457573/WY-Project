#
# with open('test.txt', 'r') as infile:
#     lines = infile.readlines()
#
# processed_lines = [line.replace(',', '') for line in lines]
#
# with open('123.txt', 'w') as outfile:
#     outfile.writelines(processed_lines)


with open('3.txt','r') as r:
    lines=r.readlines()
with open('3.txt','w') as w:
    for l in lines:
        if ': 1' not in l :
           w.write(l)