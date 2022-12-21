
with open('1234.txt', 'r') as infile:
    lines = infile.readlines()

processed_lines = [line.replace('"', '') for line in lines]

with open('123.txt', 'w') as outfile:
    outfile.writelines(processed_lines)


# with open('test.txt','r') as r:
#     lines=r.readlines()
# with open('1.txt','w') as w:
#     for l in lines:
#         if ': 3' not in l :
#            w.write(l)