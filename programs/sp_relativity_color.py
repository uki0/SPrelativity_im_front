#-*-coding: utf-8 -*-
from PIL import Image
import numpy as np
import math
import colorsys
from matplotlib import pyplot as plt
from decimal import Decimal, ROUND_HALF_UP


def color1():
    #lamda-HSL[区間番号][下-上, H-lamda]を作る

    #Hls = np.array([360, 330, 300, 240, 180, 120, 60, 0])
    Hls = np.array([0, 60, 120, 180, 240, 300, 330, 360])
    lam = np.array([360, 380, 470, 490, 520, 580, 780, 830])

    return lam, Hls

def color2(BETA, GAMMA, W, H, lam, Hls, RGB_1, xb_1, yb_1, zb_1, i, j, k, l, m, n, o, p):

    deg_x, deg_y = math.atan2(yb_1, xb_1), math.atan2(zb_1, (xb_1**2 + yb_1**2)**(1/2))
    deg = BETA * math.cos(deg_y) * math.cos(deg_x)

    if 1 == GAMMA*(1 - deg):
        i += 1
        RGB_4 = RGB_1
    else:
        #redshift390nmをローレンツ変換
        lamda_m = 360 * ( GAMMA *( 1- deg ))
        lamda_M = 830 * ( GAMMA *( 1- deg ))
        #print(lamda_m)
        if (lamda_M < 360) or (830 < lamda_m):
            j += 1
            RGB_4 = (0, 0, 0)

        else:
            #RGBをHLSに変換
            HLS_1 = colorsys.rgb_to_hls(RGB_1[0]/255., RGB_1[1]/255., RGB_1[2]/255.)

            if (HLS_1[1] == 0) or (HLS_1[1] == 1) or (HLS_1[2] == 0):
                k += 1
                RGB_4 = RGB_1
            else:
                h = HLS_1[0] *360
                #取得したHSL(H値)の含まれる領域を取得
                if h in Hls:
                    num1 = np.where(h == Hls[:])
                    num = num1[0][0]
                    if num == 6 or num == 7:
                        lam_1 = lam[13-num]
                    else:
                        lam_1 = lam[6-num]
                else:
                    num1_M1 = np.where(h < Hls[:])
                    num1_M = num1_M1[0]
                    num1_m1 = np.where(Hls[:] < h)
                    num1_m = num1_m1[0]
                    #print(h)
                    #print(num1_M, num1_m)
                    #領域における波長の上下限を取得
                    if len(num1_M) == 1:
                        l += 1
                        lam_1 = lam[6] + abs( (Hls[7]-h) * (lam[7]-lam[6]) / (Hls[7]-Hls[6]) )
                    else:
                        m += 1
                        aM = np.min(num1_M)
                        am = np.max(num1_m)
                        lam_1 = lam[5-am] + abs( (Hls[aM] - h) * (lam[6-am] - lam[5-am]) / (Hls[aM] - Hls[am] ) )

                #ローレンツ変換
                lam_2 = lam_1 * ( GAMMA *( 1- deg ))
                #print(lam_1, lam_2)
                if (lam_2 < 360) or (830 < lam_2):
                    n += 1
                    RGB_4 = (0, 0, 0)
                else:
                    #取得した波長の含まれる領域を取得
                    if lam_2 in lam:
                        num2 = np.where(lam_2 == lam[:])
                        num = num2[0][0]
                        if num == 6 or num == 7:
                            H_2 = Hls[13-num]
                        else:
                            H_2 = Hls[6-num]
                    else:
                        num2_M1 = np.where(lam_2 < lam[:])
                        num2_M = num2_M1[0]
                        num2_m1 = np.where(lam[:] < lam_2)
                        num2_m = num2_m1[0]
                        #領域におけるH値の上下限を取得
                        if len(num2_M) == 1:
                            o += 1
                            H_2 = Hls[6] + abs( (lam[7]-lam_2) * (Hls[7]-Hls[6]) / (lam[7]-lam[6]) )
                        else:
                            p += 1
                            bM = np.min(num2_M)
                            bm = np.max(num2_m)
                            #print(bM, bm)
                            H_2 = Hls[5-bm] + abs( (lam[bM] - lam_2) * (Hls[6-bm] - Hls[5-bm]) / (lam[bM] - lam[bm] ) )

                    #HLSをRGBに変換
                    RGB_2 = colorsys.hls_to_rgb(H_2/360., HLS_1[1], HLS_1[2])
                    RGB_3 = np.array(RGB_2)
                    RGB_3 = RGB_3*255.
                    #print(Hls[6-num] +0)
                    #print(colorsys.hls_to_rgb(H_2/360, HLS_1[1], HLS_1[2]))
                    #print(RGB_2)
                    #四捨五入
                    RGB_3[0] = Decimal(str(RGB_3[0])).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                    RGB_3[1] = Decimal(str(RGB_3[1])).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
                    RGB_3[2] = Decimal(str(RGB_3[2])).quantize(Decimal('0'), rounding=ROUND_HALF_UP)

                    RGB_4 = (int(RGB_3[0]), int(RGB_3[1]), int(RGB_3[2]))
    return RGB_4, i, j, k, l, m ,n ,o, p
