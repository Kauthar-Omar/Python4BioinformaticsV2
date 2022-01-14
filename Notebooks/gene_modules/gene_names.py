'''
This is me practising how to use modules.
'''
def get_gen_names(gene_file, gene_names):
    '''
    Takes input as chromosome file and extracts gene_names from it.
    '''
    with open(gene_file, 'r') as myfile:
        with open(gene_names, "w") as outfile:
            count = 0
            flag = False
            for line in myfile:
                if line .startswith('______________'):
                    flag = True
                    count += 1
                    continue
                elif line.startswith('-'):
                    flag = False
                if flag and count ==2:
                    outfile.write(line.split()[0] + '\n')