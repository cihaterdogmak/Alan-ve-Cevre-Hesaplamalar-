'''DAİRENİN ALAN VE CEVRE HESABI'''
π = 3.14
r = input("Dairenin Yarıcapı = ")
print('Dairenin Alanı' , float(r)**2 * π)
print('Dairenin Cevresi' , float(r) * 2 * π)

'''KARENİN ALANI VE CEVRESİ'''
x = input ("Karenin Kenarı = ") 
print('Karenin Cevresi' , float(x) * 4)
print('Karenin Alanı' , (float(x))**2)

'''DİKDÖRTGENİN ALANI VE CEVRESİ'''
x = input('Dikdortgenin 1. Kenarı = ' )
y = input('Dikdortgenin 2. Kenarı = ' )
print('Dikdortgenin Cevresi' , 2 * (float(x) + float(y)))
print('Dikdörrgenin Alanı' , float(x) * float(y))

'''UCGENIN ALANI'''
x = input('Ucgenin Tabanı = ')
y = input('Ucgenin Yukseklıgı = ')
print('Ucgenin Alanı' , (float(x)*float(y))/2)