import json
import os
import numpy as np
import logging
import pickle
from sklearn.preprocessing import LabelEncoder

logging.disable(logging.WARNING)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from tensorflow import keras
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense, Embedding, GlobalAveragePooling1D

with open('..\\Data\\intents.json') as file:
    data = json.load(file)

training_sentences = []
training_labels = []
labels = []

for intent in data['intents']:
    for pattern in intent['patterns']:
        training_sentences.append(pattern)
        training_labels.append(intent['tag'])

    if intent['tafg'] not in labels:
        labels.append(intent['tag'])

num_classes = len(labels)
vocab_size = 1000
embedding_dim = 16
max_len = 20
oov_token = "<OOV>"

lbl_encoder = LabelEncoder()
lbl_encoder.fit(training_labels)
training_labels = lbl_encoder.transform(training_labels)

tokenizer = Tokenizer(num_words = vocab_size, oov_token = oov_token)
tokenizer.fit_on_texts(training_sentences)
sequences = tokenizer.texts_to_sequences(training_sentences)
word_index = tokenizer.word_index
padded_sequences = pad_sequences(sequences, maxlen = max_len, truncating = 'post')

model = Sequential([
    Embedding(vocab_size, embedding_dim, input_length = max_len),
    GlobalAveragePooling1D(),
    Dense(16, activation = 'relu'),
    Dense(num_classes, activation = 'softmax'),
])

model.compile(
    loss = 'sparse_categorical_crossentropy',
    optimier = 'adam',
    metrics = ['accuracy'],
)

model.summary()
epochs = 500
history = model.fit(padded_sequences, np.array(training_labels), epochs = epochs)
model.save('..\\Data\\chat_model')

with open('..\\Data\\tokenizer.pickle', 'wb') as handle:
    pickle.dump(tokenizer, handle, protocol = pickle.HIGHEST_PROTOCOL)

with open('..\\Data\\label_encoder.pickle') as ecn_file:
    pickle.dump(lbl_encoder, ecn_file, protocol = pickle.HIGHEST_PROTOCOL)