import sys
 
def read_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            words.extend(line.split())
    return words

def print_words(filename):
    words = read_words(filename)
    d = dict()
    ans = []
    for i in range(len(words)):
        if d.get(words[i].lower()) == None:
            d[words[i].lower()] = 1
        else:
            d[words[i].lower()] += 1
    ans = list(d.items())
    ans.sort(key=lambda x: x[0])
    
    for i in range(len(ans)):        
        print(ans[i][0], ans[i][1])
    
def print_top(filename):
    words = read_words(filename)
    d = dict()
    ans = []
    for i in range(len(words)):
        if d.get(words[i].lower()) == None:
            d[words[i].lower()] = 1
        else:
            d[words[i].lower()] += 1
    ans = list(d.items())
    ans.sort(key=lambda x: x[1], reverse=True)
    
    for i in range(min(20, len(ans))):        
        print(ans[i][0], ans[i][1])
    

def main():
    if len(sys.argv) != 3:
        print('usage: ./wordcount.py {--count | --topcount} file')
        sys.exit(1)
 
    option = sys.argv[1]
    filename = sys.argv[2]
    if option == '--count':
        print_words(filename)
    elif option == '--topcount':
        print_top(filename)
    else:
        print('unknown option: ' + option)
        sys.exit(1)
 
if __name__ == '__main__':
    main()