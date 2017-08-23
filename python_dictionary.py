# Enter your code here. Read input from STDIN. Print output to STDOUT

def read_into_dict(size):
    a = {}
    for i in range(size):
        tuple = raw_input().split()
        a[tuple[0]] = tuple[1]        
    return a

def print_dict(map):
    for k,v in map.items():
        print k + "=" + v

def check_query(data, names):
    for name in names:
        if name in data:
            print name+"="+data[name]
        else:
            print "Not found"
        

def main():
    #creat empty dictionary in Python
    data = {}    # OR  data = dict()

    #Read number of dictionary entries
    n = int(raw_input())

    #read 'n' dictionary entries
    data = read_into_dict(n);
    
    #print map/dictionary
    #print_dict(data)
    
    #Read list of names
    names = list()  # OR  names = []
    while True:
        try:
            names.append(raw_input())
        except EOFError:
            break
    
    #Check if names exists in dict
    check_query(data, names)
            
if __name__ == "__main__": main()