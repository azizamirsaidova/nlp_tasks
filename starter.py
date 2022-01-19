import nltk
import re
nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords

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

def split_data(tokens):

    split1 = round(len(tokens)*0.8)
    split2 = round(split1 + len(tokens)*0.1)

    training_set = tokens[:split1]
    validation_set = tokens[split1:split2]
    test_set = tokens[split2:]

    # print(len(training_set))
    # print(len(validation_set))
    # print(len(test_set))

    return (training_set, validation_set, test_set)

def statistics(training_set, validation_set, test_set):

    thresh = 3
    count = 0
    vocabulary = []
    unk_vocabulary_list = []
    num_tokens = 0
    unk_tokens = 0
    stops_words = list(set(stopwords.words('english')))
    stops_words_list = []
    aux_set = validation_set + test_set

    # VOCABULARY creating from training
    for word in training_set:
        count += 1
        if count % thresh == 0:
            if word not in vocabulary:
                vocabulary.append(word)
    print(len(vocabulary))

    # STOPWORDS in vocabulary
    for voc in vocabulary:
        if voc in stops_words and voc not in stops_words_list:
            stops_words_list.append(voc)

    print(len(stops_words_list))

    # UNKNOWN counting
    for w in aux_set:
        if w not in vocabulary:
            unk_tokens += 1
            if w not in unk_vocabulary_list:
                unk_vocabulary_list.append(w)
    print(len(unk_vocabulary_list))







def main():

    # TOKENIZE the corpus
    text_file = open("source_text.txt").read()
    tokens = tokenize(text_file)
    #print(tokens)

    #SPLIT datasets
    splited_data = split_data(tokens)
    training_set = splited_data[0]
    validation_set = splited_data[1]
    test_set = splited_data[2]

    # STATISTICS
    statistics(training_set, validation_set, test_set)


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
        
    
    
              