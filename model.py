import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.layers import Dense, Conv2D, Flattem, Dropout, MaxPooling2D

model = Sequential(
        Conv2D(128, (4, 4), padding='same', activation='relu', input_shape=(6, 7, 1)),
        MaxPooling2D(pool_size=(2, 2)),

        Dense(64, activation='relu'),
        Dense(64, activation='relu'),

        Dense(1)
        )

optimizer = tf.keras.optimizers.Adam()

model.compile(
        loss='mean_squared_error',
        optimizer=optimizer,
        metrics=['accuracy']
        )
