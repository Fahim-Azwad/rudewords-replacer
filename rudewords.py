import string

rude_words=['crap', 'darn', 'heck', 'jerk', 'idiot', 'butt', 'devil',
            'shit']   

replacements={}

def add_element(key, value):
    if key not in replacements:
        replacements.update({key:value})
    print(replacements)
    

def replacer(word):
    new=list(word)
    for n in range(len(new)):
        new[n]='*'
    s="".join(new)
    print(s)
    add_element(word,str(s))


def check_line(line):
    rude_count=0
    words=line.split(" ")
    for word in words:
        word=word.strip(string.punctuation).lower()
        if word in rude_words:
            rude_count+=1
            print(f'Found rude word:{word}')
            print('Replacing it now! with *')
            replacer(word)
                
    return rude_count

def replace_words(filename):
    with open(filename) as myfile:
        rude_count = 0
        for line in myfile:
            rude_count+= check_line(line)
    change() 
    if rude_count == 0:
        print("Congrats! no rude word xD")

def change():
    with open('rudewords.txt') as infile, open('clean.txt', 'w') as outfile:
        for line in infile:
            for src, target in replacements.items():
                line = line.replace(src, target)
            outfile.write(line)


if __name__ == '__main__':
    replace_words('rudewords.txt')