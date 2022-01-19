import nltk
import re
nltk.download('punkt')

class my_corpus():
    def __init__(self, params):
        super().__init__() 
        
        self.params = params
        print('setting parameters')
    
    def encode_as_ints(self, sequence):
        
        int_represent = []
        
        print('encode this sequence: %s' % sequence)
        print('as a list of integers.')
        
        return(int_represent)
    
    def encode_as_text(self,int_represent):

        text = ''
        
        print('encode this list', int_represent)
        print('as a text sequence.')
        
        return(text)

def tokenize(text_file):
    #TOKENIZE
    tokens = nltk.word_tokenize(text_file)
    months_list = ['january','february','march','april','may','june','july','august','september','october','november','december']
    #print(tokens)

    #LOWERCASE
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    #print(tokens[0:10])

    for i in range(len(tokens)):
        if tokens[i].isnumeric() and len(tokens[i])==4:
            tokens[i] = '<year>'
        elif isinstance(tokens[i], float):
            tokens[i] = '<decimal>'

        elif (tokens[i] in months_list) and re.match(r'\d*',tokens[i+1]) and len(tokens[i+1])<3:
            tokens[i+1] = '<days>'

        elif i > 1 and (tokens[i] in months_list) and re.match(r'\d*',tokens[i-1]) and len(tokens[i - 1]) < 3:
            tokens[i - 1] = '<days>'

        elif tokens[i].isdigit():
            tokens[i] = '<integer>'

        elif re.search('[\d*]', tokens[i]) and re.search('[@_!#$%^&*()<>?/\|}{~:-]', tokens[i]):
            tokens[i] = '<other>'

    return tokens

def main():

    text_file = open("source_text.txt").read()
    tokenize(text_file)

# October 2, 2003
# 1 March 1926   -> '\s(\d*\s\w*\s\d*)\s'
'''
    corpus = my_corpus(None)
    
    text = input('Please enter a test sequence to encode and recover: ')
    print(' ')
    ints = corpus.encode_as_ints(text)
    print(' ')
    print('integer encodeing: ',ints)
    
    print(' ')
    text = corpus.encode_as_text(ints)
    print(' ')
    print('this is the encoded text: %s' % text)
'''

if __name__ == "__main__":
    main()
        
    
    
              