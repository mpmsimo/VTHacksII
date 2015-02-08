#!/usr/bin/python
from __future__ import division, print_function
import pickle, random

import nltk

def twitch_chat_features(document, chat_features):
    message_words = set(document)
    message_words = {word.lower() for word in message_words} 
    chat_features = {'contains({})'.format(word) for word in chat_features if word in message_words}
    return chat_features

def pickle_classifier(classifier):
	with open('Twitch_DTClassifer.pickle', 'wb') as file:
		pickle.dump(classifier, file, -1)

def main():
    train_corpus = nltk.corpus.PlaintextCorpusReader('../data/test_data', '.*\.txt')
    entire_corpus = nltk.corpus.PlaintextCorpusReader('../data/raw_data', '.*\.txt')

    train_messages = [(list(train_corpus.words(fileid)), fileid.split('_')[1][:-4]) for fileid in train_corpus.fileids()]

    all_messages =  [entire_corpus.words(fileid) for fileid in entire_corpus.fileids()]

    random.shuffle(train_messages)
    
    with open('TwitchChatFeatures.txt') as feature_file:
		chat_features = set(feature_file)

    message_features = [(twitch_chat_features(message, chat_features), classification) for message, classification in train_messages]

    training_set, testing_set = message_features[:50], message_features[50:]

    message_classifier = nltk.DecisionTreeClassifier.train(training_set)

    print(nltk.classify.accuracy(message_classifier, testing_set), '\n')

    #message_classifier.show_most_informative_features(15)

    pickle_classifier(message_classifier)

if __name__ == "__main__": main()
