import sys
 
 
def read_words(filename):
    words = []
    with open(filename, "r") as f:
        for line in f:
            words.extend(line.split())
    return words

def count_words(filename):
    words = read_words(filename)
    d = dict()
    ans = []
    for word in words:
        if word.lower() not in d:
            d[word.lower()] = 1
        else:
            d[word.lower()] += 1
    ans = list(d.items())
    
    return ans

def print_words(filename):
    ans = count_words(filename)
    ans.sort(key=lambda x: x[0])
    
    for el in ans:        
        print(el[0], el[1])

    
def print_top(filename):
    ans = count_words(filename)    
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