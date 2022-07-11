import numpy as np
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential, Model
from tensorflow.python.keras.layers import Dense, Input, Conv2D, Flatten
import time
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from tensorflow.python.keras.callbacks import EarlyStopping, ModelCheckpoint
from sklearn.preprocessing import MaxAbsScaler, RobustScaler
from tensorflow.keras.utils import to_categorical

#1. data 
datasets = load_breast_cancer()
#print(datasets)
x = datasets.data # x = datasets['data'] 이렇게도 사용 가능
y = datasets.target

x_train, x_test, y_train, y_test = train_test_split(x,y,
        train_size=0.7, shuffle=True, random_state=100)

print(x_train.shape, x_test.shape)  # (398, 30) (171, 30)
print(y_train.shape, y_test.shape)  # (398,) (171,)

x_train = x_train.reshape(398,30,1,1)
x_test = x_test.reshape(171,30,1,1 )

# from sklearn.preprocessing import MinMaxScaler, StandardScaler
# from sklearn.preprocessing import MaxAbsScaler, RobustScaler
# scaler = RobustScaler()
# scaler = MaxAbsScaler()

# scaler = MinMaxScaler()
# scaler = StandardScaler()
# scaler.fit(x_train)
# x_train = scaler.transform(x_train)
# x_test = scaler.transform(x_test)
# print(np.min(x_train))   # 0.0
# print(np.max(x_train))   # 0.0 컬럼별로 나누어주어야 한다
# print(np.min(x_test))
# print(np.max(x_test))

print(np.unique(y_train, return_counts=True))
print(np.unique(y_test, return_counts=True))

# 2. 모델구성


# input1 = Input(shape=(30,))
# dense1 = Dense(10)(input1)
# dense2 = Dense(5, activation='relu')(dense1)
# dense3 = Dense(3, activation='relu')(dense2)
# output1 = Dense(1)(dense3)
# model = Model(inputs=input1, outputs=output1)

model = Sequential()
model.add(Conv2D(filters=260, kernel_size=(1,1),
                 padding='same', input_shape=(30,1,1)))
model.add(Conv2D(130, (1,1),
                padding='valid', activation='relu'))
model.add(Conv2D(65, (1,1),
                padding='valid', activation='relu'))
model.add(Flatten())
model.add(Dense(50, activation='relu'))   # activation 활성화 함수 이것으로 인해 결과값이 엄청좋아지고 안좋아진다 필수 ( 다시 공부할것 시그모이드 포함 )
model.add(Dense(30, activation='relu'))      #  레이어를 한정시키며 펑 터지는것을 방지한다 ( 찾아볼것 )
model.add(Dense(20, activation='relu'))   # linear 선형  
model.add(Dense(1, activation='linear'))   # sigmoid = 0과 1이 아니고 0에서 1으로 한정 시킨다 ( 어떤값을 넣어도 0과 1사이로 표출이 된다 ) 반올림으로 0과 1로 
#  이진분류는 무조건 sigmoid 로 끝난다 그다음은 binary_crossentropy 로 쓴다 
#  activation relu 히든에서만 사용이 가능하다 relu 성능 아주 좋다 85% 성능향상 중요 

#3. 컴파일 , 훈련

start_time = time.time()
model.compile(loss='mae', optimizer='adam',   # 회기모델에서 accuracy , mae 둘다 가능 지표를 찾을 수 있음 
              metrics=['mse']) 
earlystopping = EarlyStopping(monitor='val_loss', patience=100, mode='min', verbose=1, # mode='min'뿐아니라 max도 있음  디폴드값 찾아볼것 모르면 오토 
              restore_best_weights=True) 
a = model.fit(x_train, y_train, epochs=1500, batch_size=100,
          validation_split=0.2,
          callbacks = [earlystopping],    # 이것도 리스트 형식이라는것 더 넣을수있음 
          verbose=1)   # a 대신에 hist 라고 쓰임 콜백을 하겠다 얼리 스탑잉을               

end_time = time.time()-start_time
#4. 평가, 예측
loss = model.evaluate(x_test, y_test)
print('loss : ', loss)
print(a.history['val_loss'])

y_predict = model.predict(x_test)  # 이 값이 54번 으로

y_predict = y_predict.flatten()
y_predict = np.where(y_predict > 0.5, 1 , 0)
# print(y_predict) 


from sklearn.metrics import r2_score, accuracy_score         # metrics 행렬 
# r2 = r2_score(y_test, y_predict)
acc = accuracy_score(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print('acc.score : ', acc)
print('r2.score :', r2 )
print('걸린시간 : ', end_time)

model.summary()


# acc.score :  0.9766081871345029
# r2.score : 0.9028132992327366
# 걸린시간 :  58.11681365966797
