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

        dict_int1 = dict_int
        tokens_seq = tokenize(sequence)
        int_represent = [dict_int1[y] for y in tokens_seq]

        print('encode this sequence: %s' % sequence)
        print('as a list of integers.')
        return (int_represent)


    
    def encode_as_text(self,int_represent):

        text = [dict_char[y] for y in int_represent]
       
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

#q3-train,test and valid split
def text_split(corpus):
    split_corpus =(corpus.split("<end_of_passage>\n\n<start_of_passage>"))
    # Defines ratios, w.r.t. whole dataset.
    train_ratio = 0.8
    val_ratio = 0.1
    test_ratio = 0.1

    # Produces test split.
    train_rem, test_set = train_test_split(split_corpus, test_size=test_ratio)

    # Adjusts val ratio, w.r.t. remaining dataset.
    ratio_remaining = 1 - test_ratio
    ratio_val_adjusted = val_ratio / ratio_remaining

    # Produces train and val splits.
    training_set, validation_set = train_test_split(train_rem, test_size=ratio_val_adjusted)


    # print("train",training_set)
    # print("test",len(validation_set))
    # print("valid",len(test_set))

    return (training_set, validation_set, test_set)

def statistics(training_set, validation_set, test_set):

    thresh = 3
    count = 0
    training_split = []
    validation_split = []
    test_split = []
    vocabulary = []
    unk_vocabulary_list_validation = []
    unk_vocabulary_list_test = []
    unk_tokens_validation = 0
    unk_tokens_test = 0
    stops_words = list(set(stopwords.words('english')))
    stops_words_list = []

    unk_type_list_validation = []
    unk_type_list_test = []

    #SPLIT the corpus
    for w1 in training_set:
        count += 1
        if count % thresh == 0:
            training_split.append(w1)
    count = 0

    for w2 in validation_set:
        count += 1
        if count % thresh == 0:
            validation_split.append(w2)
    count = 0

    for w3 in test_set:
        count += 1
        if count % thresh == 0:
            test_split.append(w3)
    count = 0

    # VOCABULARY creating from training
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:-]')
    for word in training_split:
        count += 1
        if word not in vocabulary and (string_check.search(word) == None):
            vocabulary.append(word)
    count = 0
    # STOPWORDS in vocabulary
    for voc in vocabulary:
        if voc in stops_words and voc not in stops_words_list:
            stops_words_list.append(voc)

    # UNKNOWN counting
    for w in validation_split:
        count += 1
        if w not in vocabulary:
            unk_tokens_validation += 1
            if w not in unk_vocabulary_list_validation:
                unk_vocabulary_list_validation.append(w)
    count = 0

    for w in test_split:
        count += 1
        if w not in vocabulary:
            unk_tokens_test += 1
            if w not in unk_vocabulary_list_test:
                unk_vocabulary_list_test.append(w)

    # i) number of tokens in each split (with threshold 3)
    num_tokens_training = len(training_split)
    num_tokens_validation = len(validation_split)
    num_tokens_test = len(test_split)
    print(f"i) Number of tokens of training set with threshold 3: {num_tokens_training}")
    print(f"   Number of tokens of validation set with threshold 3: {num_tokens_validation}")
    print(f"   Number of tokens of test set with threshold 3: {num_tokens_test}")

    # ii) the vocabulary size
    vocabulary_size = len(vocabulary)
    print(f"ii) The vocabulary size is: {vocabulary_size}")

    # iii) the number of <unk> tokens
    print(f"iii) The number of <unk> tokens in validation is: {unk_tokens_validation}")
    print(f"     The number of <unk> tokens in test is: {unk_tokens_test}")

    # iv) number of out of vocabulary words
    num_out_vocabulary_validation = len(unk_vocabulary_list_validation)
    num_out_vocabulary_test = len(unk_vocabulary_list_test)
    print(f"iv) The number of out of vocabulary words in validation is: {num_out_vocabulary_validation}")
    print(f"    The number of out of vocabulary words in test is: {num_out_vocabulary_test}")

    # v) the number of types mapped to <unk>
    for unk in unk_vocabulary_list_validation:
        type_unk = type(unk)
        if type_unk not in unk_type_list_validation:
            unk_type_list_validation.append(type_unk)

    for unk in unk_vocabulary_list_validation:
        type_unk = type(unk)
        if type_unk not in unk_type_list_test:
            unk_type_list_test.append(type_unk)
    print(f"v) The number of types mapped to <unk> in validation is : {len(unk_type_list_validation)}")
    print(f"   The number of types mapped to <unk> in test is : {len(unk_type_list_test)}")

    # vi) the number of stop words in the vocabulary
    num_stop_words = len(stops_words_list)
    print(f"vi) The number of stop words in the vocabulary: {num_stop_words}")

    # vii) two custom metrics of your choice

    ratio_unk_voc_validation = num_out_vocabulary_validation/vocabulary_size
    ratio_unk_voc_test = num_out_vocabulary_test / vocabulary_size
    print(f"vii) The ratio between the <unk> and vocabulary size for validation is: {ratio_unk_voc_validation}")
    print(f"     The ratio between the <unk> and vocabulary size for test is: {ratio_unk_voc_test}")





def main():

    # TOKENIZE the corpus
    text_file = open("source_text.txt").read()
    tokens = tokenize(text_file)
    #split dataset sklearn
    text_split(text_file)
    #print(tokens)

    #SPLIT datasets
    splited_data = split_data(tokens)
    training_set = splited_data[0]
    validation_set = splited_data[1]
    test_set = splited_data[2]

    # STATISTICS
    statistics(training_set, validation_set, test_set)

    global dict_int, dict_char
    dict_int = dict([(y, x + 1) for x, y in enumerate(sorted(set(tokens)))])
    dict_char = dict([((x+1),y) for x,y in enumerate(sorted(set(tokens)))])

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


if __name__ == "__main__":
    main()
        
    
    
              