from PIL import Image
import numpy as np
import math
import colorsys
from matplotlib import pyplot as plt
from decimal import Decimal, ROUND_HALF_UP
from tqdm import tqdm
import time

import sp_relativity_move as mo
import sp_relativity_color as co

#画像風景の視野角
#水平角/2設定
DEG_x = math.radians(80)
#仰俯角/2指定
#DEG_y = math.radians(30)

if DEG_x == 0:
    print("DEG_x and DEG_y can not be 0. ")
else:
    #速度/光速
    BETA = 0.7
    #定数ガンマ
    GAMMA = (1 - BETA**2)**(-1/2)

    # 元となる画像の読み込み(配列に変換)
    im = Image.open('Im_in/yellow.jpg')
    #オリジナル画像の幅と高さを取得
    W, H = im.size
    im = np.array(im)
    #print(im.shape)
    #print(W,H)
    
    #各種定数
    R_x = W / (2 * math.sin(DEG_x))
    R_y = (R_x**2 + (H/2)**2 - (W/2)**2)**(1/2)
    DEG_y = math.asin(H/(2 * R_y))
    #print(math.degrees(DEG_y))
    x = R_x * math.cos(DEG_x)
    R = (( (W/2)**2 + (H/2)**2) +x**2)**(1/2)
    #print(R_x * math.cos(DEG_x), R_y * math.cos(DEG_y))
    #print(R**2, R_y**2 + (W/2)**2, R_x**2 + (H/2)**2)

    #新画像生成(配列に変換)
    #色変換用
    im2 = np.array(Image.new("RGB", (W, H), (0, 0, 0)))
    #移動用
    im3 = np.array(Image.new("RGB", (W, H), (0, 0, 0)))
    #移動用
    #im4 = np.array(Image.new("RGB", (W, H), (0, 0, 0)))

    lam, Hls = co.color1()
    q, r, s, t, m, n, o, p = 0, 0, 0, 0, 0, 0, 0, 0
    for i in tqdm(range(H)):
        for j in range(W):
            #球面上に来る(y, x)を取得
            #im3(i, j)に来るim2(y, x)を取得
            #print(j)
            yb_1, xb_1, zb_1, za_1, ya_1 = mo.move1(BETA, GAMMA, R, W, H, x, i, j)

            if (int(za_1) >= H) or (int(za_1) < 0)or (int(ya_1) >= W)or (int(ya_1) < 0):
                im2[i, j] = (0, 0, 0)
            else:
                #RGBやりとりで色変換
                im2[i, j], q, r, s, t, m, n, o, p = co.color2(BETA, GAMMA, W, H, lam, Hls, im[int(za_1), int(ya_1)], xb_1, yb_1, zb_1, q, r, s, t, m, n, o, p)
    #print(q, r, s, t, m, n, o, p)

    for k in tqdm(range(0, H)):
        for l in range(0, W):
            za_2, ya_2 = mo.move2(GAMMA, W, H, k, l)

            if (int(za_2) >= H) or (int(za_2) < 0)or (int(ya_2) >= W)or (int(ya_2) < 0):
                im3[k, l] = (0, 0, 0)
            else:
                #RGBやりとりで色変換
                im3[k, l] = im2[int(za_2), int(ya_2)]
    #色変化のみ確認用
    #Image.fromarray(im2).save('Im_out/yellow_im2.jpg')
    Image.fromarray(im3).save('Im_out/yellow_im3.jpg')
