import nltk
import re
from sklearn.model_selection import train_test_split

nltk.download('punkt')
nltk.download('stopwords')
from nltk.corpus import stopwords




    

class my_corpus():

    def __init__(self, params):
        super().__init__()

        self.params = params
        print('setting parameters')
        
    def encode_as_ints(self, sequence):
        # if key in mydict.keys():
        dict_int1 = dict_int
        tokens_seq = tokenize(sequence)
        int_rep=[]
        for i in tokens_seq:

            if i in dict_int1.keys():
                int_represent = dict_int1[i]
                int_rep.append(int_represent)
                print('encode this sequence: %s' % sequence)
                print('as a list of integers.')
            elif i not in dict_int1.keys():

                dict_int1[i] = "<unk>"
                int_represent = dict_int1[i]
                dict_char[int_represent] ="<unk>"
                int_rep.append("<unk>")
                print("done int")

        return (int_rep)


    def encode_as_text(self, int_represent):
        if type(int_represent)!= str:

            text = [dict_char[y] for y in int_represent]
            print('encode this list', int_represent)
            print('as a text sequence.')
        else:
            text = "unk"
        return (text)

def tokenize(text_file):
    # TOKENIZE
    tokens = nltk.word_tokenize(text_file)
    months_list = ['january', 'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october',
                   'november', 'december']
    # print(tokens)

    # LOWERCASE
    for i in range(len(tokens)):
        tokens[i] = tokens[i].lower()
    # print(tokens[0:10])

    for i in range(len(tokens)):
        if tokens[i].isnumeric() and len(tokens[i]) == 4:
            tokens[i] = '<year>'
        elif isinstance(tokens[i], float):
            tokens[i] = '<decimal>'

        elif (tokens[i] in months_list) and re.match(r'\d*', tokens[i + 1]) and len(tokens[i + 1]) < 3:
            tokens[i + 1] = '<days>'

        elif i > 1 and (tokens[i] in months_list) and re.match(r'\d*', tokens[i - 1]) and len(tokens[i - 1]) < 3:
            tokens[i - 1] = '<days>'

        elif tokens[i].isdigit():
            tokens[i] = '<integer>'

        elif re.search('[\d*]', tokens[i]) and re.search('[@_!#$%^&*()<>?/\|}{~:-]', tokens[i]):
            tokens[i] = '<other>'

    return tokens

def main():
    # TOKENIZE the corpus
    text_file = open("source_text.txt").read()
    tokens = tokenize(text_file)
   

    # Q5 encoding
    global dict_int, dict_char
    dict_int = dict([(y, x + 1) for x, y in enumerate(sorted(set(tokens)))])
    dict_char = dict([((x + 1), y) for x, y in enumerate(sorted(set(tokens)))])

    corpus = my_corpus(None)

    text = input('Please enter a test sequence to encode and recover: ')
    print(' ')
    ints = corpus.encode_as_ints(text)
    print(' ')
    print('integer encodeing: ', ints)

    print(' ')
    text = corpus.encode_as_text(ints)
    print(' ')
    print('this is the encoded text: %s' % ' '.join(text))
    print(' ')



if __name__ == "__main__":
    main()
