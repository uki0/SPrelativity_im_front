#特殊相対論の可視化

このプログラムは特殊相対論の可視化を試みるものです  
入力画像はある人から見た風景であり，その人が瞬間的に，その視界の中心に向かう速度vを得たとして見える風景を出力します  

なお，視界の光は全て単色光であると仮定し，各点の色値から波長を推定して変換しています  

入力画像を programs/Im_in に配置してください  
出力画像は programs/Im_out に出力されます  

####以下の条件を設定してください
1. 入力画像の水平視野角の半値a  
programs/special_relativity_image.py 15行目
0 < a < 90
```python
#画像風景の視野角
#水平角/2設定
DEG_x = math.radians(a)
```

2. 速度v/光速cの値b  
programs/special_relativity_image.py 23行目
0 < b < 1  
```python
#速度/光速
  BETA = b
```

3. 入力画像の名前.拡張子  
programs/special_relativity_image.py 28行目  
例(yellow.jpg)  
```python
im = Image.open('Im_in/yellow.jpg')
```

4. 出力画像の名前.拡張子  
programs/special_relativity_image.py 78行目  
例(yellow_im3.jpg)  
```python
Image.fromarray(im3).save('Im_out/yellow_im3.jpg')
```


設定ができたら  
 *special_relativity_image.py*  
を実行してください．
