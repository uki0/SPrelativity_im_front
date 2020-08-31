from PIL import Image
import numpy as np
import math
from matplotlib import pyplot as plt
from decimal import Decimal, ROUND_HALF_UP

def move1(BETA, GAMMA, R, W, H, x_a2, z_a2, y_a2):


    #曲面に投射
    def A2toB2(x):
        return ( R * x / ( (x_a2)**2 + (y_a2 - W/2 )**2 + (z_a2 - H/2 )**2 )**(1/2) )
    x_b2 = A2toB2(x_a2)
    y_b2 = A2toB2(y_a2 - W/2 )
    z_b2 = A2toB2(z_a2 - H/2 )

    #print(x_a2, y_a2 - W/2 , z_a2 - H/2 )

    #ローレンツ変換
    x_b1 = x_b2/ GAMMA
    y_b1 = y_b2
    z_b1 = z_b2
    #平面へ投射
    x_a1 = x_a2/GAMMA
    y_a1 = y_a2
    z_a1 = z_a2

    #print(y_a1,z_a1)

    #print('2', y_a2, z_a2)
    #print( x_a1, x_a2)
    #print('2', my_round(z_a1+H/2-0.5), my_round(y_a1+W/2-0.5))
    return y_b1, x_b1, z_b1, z_a1, y_a1


def move2(GAMMA, W, H, z_a10, y_a10):

    za_2 = GAMMA* (z_a10 -H/2 ) +H/2
    ya_2 = GAMMA* (y_a10 -W/2 ) +W/2

    #四捨五入
    ya_2 = Decimal(str(ya_2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
    za_2 = Decimal(str(za_2)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

    return za_2, ya_2
