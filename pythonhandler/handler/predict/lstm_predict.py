from keras.layers import Dense, Activation, Dropout, LSTM
from .predict import predict


class lstm_predict(predict):
    def model_structure(self):
        self.model.add(LSTM(input_dim=1, units=50, return_sequences=True))
        self.model.add(LSTM(input_dim=50, units=100, return_sequences=True))
        self.model.add(LSTM(input_dim=100, units=200, return_sequences=True))
        self.model.add(LSTM(300, return_sequences=False))
        self.model.add(Dropout(0.2))
        self.model.add(Dense(100))
        self.model.add(Dense(units=1))
        self.model.add(Activation('relu'))


# if __name__ == '__main__':
#     p = lstm_predict("000001", 20)
#     dataset, trainPredict, testPredict = p.model_run()
