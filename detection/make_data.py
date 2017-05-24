'''
画像を水増しする。
角度変えたり、反転させたり。
参考書籍: Pythonによるスクレイピング&機械学習 開発テクニック BeautifulSoup,scikit-learn,TensorFlowを使ってみよう
src: gyudon-makedata2.py
'''

import glob
import random
import math
from PIL import Image
import numpy as np

load_dir = './images/selected/'
save_dir = './images/created/'
categories = [
    'carrot',
    'onion',
    'radish',
    'tomato',
    'cabbage',
]
cat_len = len(categories)
image_size = 50

X = []
Y = []
def add_sample(cat, fname, is_train):
    global count
    img = Image.open(fname)
    img = img.convert("RGB")
    img = img.resize((image_size, image_size))
    dir_name = fname.split('/')[4]+'/'
    file_name = fname.split('/')[-1]
    data = np.asarray(img)
    X.append(data)
    Y.append(cat)
    if not is_train: return
    for ang in range(-20, 20, 5):
        img2 = img.rotate(ang)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)
        img2.save(save_dir+'/'+dir_name+file_name+'-'+str(ang)+'.png')
        # 反転する
        print(save_dir+'test/'+dir_name+file_name+'-'+str(ang)+'.png')
        img2 = img2.transpose(Image.FLIP_LEFT_RIGHT)
        data = np.asarray(img2)
        X.append(data)
        Y.append(cat)

def make_sample(files, is_train):
    global X, Y
    X = []; Y = []
    for cat, fname in files:
        add_sample(cat, fname, is_train)
    return np.array(X), np.array(Y)

# ディレクトリごとに分けられたファイルを収集する
allfiles = []
for idx, cat in enumerate(categories):
    image_dir = load_dir + "/" + cat
    files = glob.glob(image_dir + "/*.jpg")
    for f in files:
        allfiles.append((idx, f))

# シャッフルして学習データとテストデータに分ける
random.shuffle(allfiles)
th = math.floor(len(allfiles) * 0.6)
train = allfiles[0:th]
test = allfiles[th:]
X_train, y_train = make_sample(train, True)
X_test, y_test = make_sample(test, True)
xy = (X_train, X_test, y_train, y_test)
np.save("./images/ingredients.npy", xy)
print("ok,", len(y_train))