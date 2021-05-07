from json import load
from re import search

def is_cedula(str):
    return search('[0-9]{5,}', str)

def is_year(str):
    return search('^[0-9]{4}$', str)

def convert(data, outfile):
    blocks = data['Blocks']
    line = []

    with open(outfile, 'w') as f:
        for block in blocks:
            type = block['BlockType']
            if type == 'LINE':
                text = block['Text']
                if is_cedula(text):
                    line.append(text)

                if is_year(text):
                    line.append(text)
                    f.write(';'.join([col for col in line]))
                    f.write('\n')
                    line = []

def main():
    blockfile = './block.json'
    csvfile = './ddt.csv'

    data = {}
    with open(blockfile, 'r') as f:
        data = load(f)
    convert(data, csvfile)
    
if __name__ == "__main__":
    main()
