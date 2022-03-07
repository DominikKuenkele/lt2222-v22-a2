import gzip
import random

import nltk
import pandas as pd
from nltk.corpus import stopwords
from sklearn.metrics import precision_score, recall_score, f1_score
from sklearn.svm import SVC

POS = "V"


def sample_lines(file_name, lines):
    with gzip.open(file_name, 'rt') as file:
        file_lines = file.read().splitlines()
    if lines > len(file_lines):
        lines = len(file_lines)
    return random.sample(file_lines, lines)


def process_sentences(lines):
    stop_words = set(stopwords.words('english'))
    punctuation_tags = ["'", "(", ")", ",", "--", ".", ":", "''", "``", "SYM", "CD", "LS"]

    tagged_lines = []
    for line in lines:
        tokens = nltk.word_tokenize(line)
        tagged = nltk.pos_tag(tokens)
        lowered = [(word.lower(), tag) for word, tag in tagged]
        filtered = filter(lambda x: x[0] not in stop_words and x[1] not in punctuation_tags and len(x[0]) > 1, lowered)
        tagged_lines.append(list(filtered))

    return tagged_lines


def create_samples(sentences, samples):
    sequences = []
    for sentence in sentences:
        sequences.extend(list(nltk.ngrams(sentence, 5)))
    if samples > len(sequences):
        samples = len(sequences)
    random_samples = random.sample(sequences, samples)

    classifications = []
    for sample in random_samples:
        classifications.append(((sample[0][0][-2:], sample[1][0][-2:], sample[3][0][-2:], sample[4][0][-2:]),
                                int(sample[2][1].startswith(POS))))
    return classifications


def create_df(samples):
    features = [POS]
    dataframe = []

    for sample in samples:
        dataframe.append([0] * len(features))
        if sample[1] == 1:
            dataframe[-1][0] += 1
        for feature in sample[0]:
            if feature not in features:
                features.append(feature)
                for prev_sample in dataframe:
                    prev_sample.append(0)
            dataframe[-1][features.index(feature)] += 1

    return pd.DataFrame(dataframe, columns=features)


def split_samples(dataframe, test_percent):
    split = round(len(dataframe) * test_percent / 100)

    y = dataframe[POS]
    X = dataframe[dataframe.columns.difference([POS])]
    return X[split:], y[split:], X[:split], y[:split]


def train(train_X, train_y, kernel):
    svc = SVC(kernel=kernel)
    svc.fit(train_X, train_y)
    return svc


def eval_model(model, test_X, test_y):
    predictions = model.predict(test_X)
    print('Kernel:', model.kernel),
    print('_________________')
    print('Precision:', precision_score(test_y, predictions))
    print('Recall:', recall_score(test_y, predictions))
    print('F1 Score:', f1_score(test_y, predictions))
