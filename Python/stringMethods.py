# verilmis ededin 3-e tam bolunub bolunmediyini tapin

# a=9
# if a%3==0:
#     print('3-e bolunur')
# else:
#     print('bolunmur')
# ------------------------------------

# 1-den 50-ye qeder 3-bolunende qaliqda1qalan ededler

# for i in range (1,51):
#     if i%3 == 1:
#         print(i)
#     else:
#         print('false')
# -----------------------------------

# 10-dan 400-e qeder cut ededlerin icinden 3-e  bolunende qaliqda 1 qalan ededlerin cemi
# s=0
# for i in range(10,401):
#     if i%2 ==0:
#         if  i%3 ==1:
#             s=s+i
# print(s)
# ----------------------------

# verilen melumatlar uzerinde string metodlarini tetbiq edin:
# ad="sehla"
# soyad="memmedova"

# 1. her iki adi ilk herfini boyuk etmek
# 2. h herfinin necenci indexde yerlesmesi

# print(ad.capitalize())
# print(soyad.capitalize())
# print(ad.index('h'))
# --------------------------

# cumle = "salam dos necesinizi= asafafjanjkfsad"
# c=cumle.split()
# en_qisa_soz= c[0]

# for i in c:
#     if len(i) < len(en_qisa_soz):
#         en_qisa_soz = i

# print("en qisa soz",en_qisa_soz)

# # uzun soz
# sozler = cumle.split()
# en_uzun_soz = ""

# for i in sozler:
#     if len(i) > len(en_uzun_soz):
#         en_uzun_soz = i

# print("En uzun soz:", en_uzun_soz)


# 5-den kicik reqemlerin hasili

# integer = int(input("ededi daxil edin: "))

# hasil = 1
# output = [int(x) for x in str(integer)]
# for i in output:
#     if i < 5:
#         hasil = hasil * i
# print(hasil)

# p = 1
# while integer > 0:
#     r = integer % 10
#     if r < 5:
#         p = p*r
#     integer = integer // 10
# print(p)


# setrin simvollari icerisinde butun reqemlerin kvadratlari cemi

# setir=str(input('metni daxil edin: '))
# reqemler= '0123456789'
# s=1
# for i in setir:
#     if reqemler.count(i) > 0:
#         s=s*int(i)**3
# print(s)


# a=int(input('reqemi daxil edin: ' ))
# print(a**(1/2))


# ededi tersden yazan funksiya

# eded = int(input("ededi daxil edin: "))

# def sehlaninFunksiyasi(a): {
#     print(int(str(a)[::-1]))
# }

# sehlaninFunksiyasi(eded)

# 1-den daxil edilen edede qeder (input) cut ededlerin cemini ve hasilini hesablayan funksiya
# a = 1
# b = int(input('Ededi daxil edin: '))
# s = 0
# d = 1


# def sey():
#     global s, d
#     for i in range(a, b):
#         if i % 2 == 0:
#             s = s + i
#             d = d * i


# sey()
# print(d)
# print(s)


# daxil edilen ededin kokalti qiymetini hesablayan funksiya

# a=int(input('ededi daxil edin: '))

# def a(a):
#     print(a*2)

# a(a)

# daxil edilen ededin kvarati ile kubunun cemini hesablayan funksiya

# a=int(input('ededi daxil edin '))
# def jk():
#     global a
#     s=0
#     kvadrat=a**2
#     kub=a**3
#     print(kvadrat + kub)
# jk()

# ----------------------------------------


# daxil edilen araliq qeder cut ededleri teyin eded funksiya

# a=int(input('ededi daxil edin:'))
# def df(): 
#     for i in range (1,a):
#         if i%2 == 0:
#             print(i)
# df()


# daxil edilen ededin sonuncu ededinden 1 vahid evvelde yerlesen ededi teyin eden funksiya

# daxilEdilenEded = input("ededi daxil edin: ")

# def daxilEdilenEdeddenEvvelkiEded():
#     listeda = list(daxilEdilenEded)
#     print(listeda[len(listeda) - 2])

# daxilEdilenEdeddenEvvelkiEded()


# daxil ededin ededin polindrom olub olmamasini yoxlayan funksiya

# daxilEdilen = input("ededi daxil edin: ")

# def polindromCheck():
#     reverseEded = (str(daxilEdilen)[::-1])
#     if (reverseEded == daxilEdilen):
#         print("polindromdur")
#     else:
#         print("polindrom deyil")
# polindromCheck()

# daxil edilen menfi ededi musbet edede ceviren funksiya ve eded musbetdirse musbet ededin daxil edildiyini bildirmek

# a= int(input('ededi daxil edin: '))

# def gh():
#     global a
#     if (a < 0):
#         a=a* (-1)
#         print(a)
# gh()


# daxil edilen ededin daxil edilen edede qaliqsiz bolunub bolunmediyini teyin eded funksiya

# a=int(input('ededi daxil edin:'))
# b=int(input('ededi daxil edin:'))

# def ugh():
#     if (a%b == 0):
#         print('a ededi b ededine bolunur')
#     else:
#         print('a ededi b ededine bolunmur')
# ugh()  

# daxil edilen 1den 7-ye qeder ededin heftenin hansi gunu oldugunu teyin e

# a= int(input(' ededi yazin: '))
# def alma():
#     if (a == 1):
#         print('bazar ertesi')
#     elif (a == 2):
#         print('cersembe axsami')
#     else:
#         print('gunleri duzgun daxil edin')
# alma()    

# -----------------------------

# and, or

# 1-den 100-e  qeder olan ededlerden 2-ye ve 40-ya qaliqsiz bolunen ededi teyin eden funksiya

# and
# def qaliqsiz_bolunen():
#     for i in range(1,101):
#         if(i % 2 == 0 and i % 40 == 0 ):
#             print(i)

# qaliqsiz_bolunen()

# or

# def qaliqsiz_bolunen():
#     for i in range(1,101):
#         if(i % 2 == 0 or i % 40 == 0):
#             print(i)

# qaliqsiz_bolunen()

# 1-den 5000-e qeder olan ededlerden hem cut ededleri hemde 4500-den boyuk olan ededleri ekrana cixaran funksiya
# def alma():
#     for i in range (1,5001):
#         if (i % 2 ==0 and i>=4500):
#             print(i)
# alma()            

# 1-den 500-e qeder 200-e ve ya 400-e qaliqsiz bolunen ededleri teyin eden funksiya
# s=0
# def xoruz():
#     for i in range (1,501):
#         if (i % 200 == 0 or i % 400 == 0):
#             print(s) 
# xoruz()            

# ----------------------------------

# daxil edilen ededin 100-den boyuy olub olmadigini ve cut eded olub olmadigini yoxlayan funksiya

# a=int(input('ededi daxil edin'))
# def masin():
#     if a>100 and a%2==0:
#         print(a)
#     else:
#         print('a ededi 100 den boyuk deyil')   

# if a > 0:
#     masin()
# else:
#     print('eded  menfidir cut eded daxil edin!!!!!!')
    

# daxil edilen araliqda olan cut ededlerin cemi ve tek ededlerin hasilini hesablayan funksiya
# a=int(input('ededi daxil edin: '))
# b =int(input('ededi daxil edin:'))
# s=0
# p=1
# def eded():
#     global a,b,s,p
#     for i in range (a,b):
#         if i%2 ==0:
#             s=s+i
            
#         else:
#             p=p*i
            
# eded()           
# print(s)
# print(p)


# daxil edilen sözün sonuncu hərfini və uzunluğunu qaytaran funksiya

# a=input('metni daxil edin:')
# b= list(a)
# print(b[len(b) - 1])
# print(len(b))

# ------------------------------------
# pyhton sonuncu gun

# 1-den daxil edilen edede qeder olan cut ededlerin cemi

# a=int(input('ededi daxil edin:'))
# s=0
# for i in range (1,a):
#     if i%2 == 0:
#         s=s+i
# print(s)


# daxil edilen ədədin 15 və 20 arasında olub olmadığını yoxlayan funksiya
# a=int(input('edeid daxil edin: '))
# def eded():
#     global a
#     if (a>15 and a<20):
#         print("true")
#     else:
#         print('false')
# eded()            


# daxil edilən ədədin kravratını hesablayan funksiya

# a=int(input('ededi daxil edin: '))
# def defter():
#     b=a**2
#     print(b)
# defter()    

# 90-a qeder cüt ededlerin hasili ve tek ededlerin cəmini hesablayan funksiya
# s=0
# p=1
# def eded():
#     global s,p
#     for i in range (1,91):
#         if (i%2 == 0 ):
#             p=p*i
#         else:
#             s=s+i
# eded()
# print(p)
# print(s)                

# 1-den 20-yə qədər 2 rəqəmli və cüt ədədləri ekrana çıxaran funksiya

# def eded():
#     for i in range (1,21):
#         if len(str(i)) > 1 and i % 2 == 0:
#             print(i)
# eded()

# ------------------------------------------------------------------

# daxil edilen ededin 100-den kicik olub olmadigini yoxlayan funksiya

# a=int(input('ededi daxil edin: '))
# def eded():
#     global a
#     if a < 100:
#         print(a)
#     else:
#         print('eded 100 den kicik deyil')
# eded()


# daxil edilen sozun uzunlugunu gosteren funksiya
# a = input('sozu daxil edin:')

# def eded():
#     global a
#     print( len(a))
# eded()



# daxil edilen sozun sonuncu herfini ve ilk herfini gosterin

# a=input('sozu daxil edin: ')
# b=list(a) 
# print(b[len(b) -1])
# print(b[0])





# daxil edilen ededin kvarati ile kubunun cemini hesablayan funksiya
# a=int(input('ededi daxil edin: '))
# s=0
# def ev():
#     global a,s,b,c
#     b=a**2
#     c=a**3
#     print(b+c)
# ev()


# 1-den 50-ye qeder olan ededleri 3-bolunende qaliqda qalan ededler 
# for i in range (1,51):
#     if i%3== 2:
#        print('2')
#     if i%3== 1:
#         print('1')
#     if i%3==0:
#         print('0')




# daxil edilen ədədin 15 və 20 arasında olub olmadığını yoxlayan funksiya
# a=int(input('ededi daxil edin: '))
# def eded ():
#     global a
#     if (a>15 and a<20):
#         print('a ededi 15 ile 20 arasinda yerlesir')
#     else:
#         print('a ededi 15 ve 20 arasinda yerlesmir')
# eded()


# daxil edilen ededin 50 - 70 arasinda olub olmadigini ve cut eded oldugunu yoxlayan funksiya

# a=int(input('ededi daxil edin: '))
# def eded():
#     if ( 70>a>50 and a%2==0 ):
#         print(a)
#     else:
#         print('eded 50 ile 70 arasinda yerlesmir')

#     if a>0:
#         print(a)
#     else:
#         print('eded menfidir musbet eded daxil edin')
# eded()




# sozun herflere ayrilaraq massive yigilmasi
# a=input('sozu daxil edin: ')
# b=list(a)

# print(b)

# daxil edilen sozun uzunlugu 10-dan boyukdurse 10-dan boyuk oldugunu bildirmek
 
# a=input('sozu daxil edin: ')
# if len(a)>10:
#    print('a ededi 10 dan boyukdur')
# else:
#    print('a ededi 10 dan boyuk deyil')

# daxil edilen ededin cut ve ya 10-dan boyuk oldugunu teyin eden funksiya

# a=int(input('ededi daxil edin:'))
# def say():
#     if a%2==0 or a>10:
#         print(a)
#     else: 
#         print('eded cut ve ye 10 dan boyuk deyil')
# say()


# ----------------------------------------------

# s = 0
# i = 1
# while i <= 10:
#     s = s+i
#     i= i+1
#     if i>5:
#         break
# print(s)

# def f(a, b):
#     while a !=0 and b !=0:
#         if a>b:
#             a=a%b
#         else:
#             b=b%a
#     return a + b

# a=int(input())
# b=int(input())

# print(f(a, b))

# tekrarin silinmesi

# a = [1,2,3,4,3,2]
# t=[]

# for x in a:
#     if t.count(x) == 0:
#         t.append(x)

# a=t 
# print(a)

# def eded(x):
#     s = 0
#     while x>0:
#         q = x%10
#         s = s+q
#         x = x//10
#     return s

# a = 289
# while a>9:
#     a=eded(a)

# print(a)


# m = 2
# n = 6
# k = 9
# if m + n < k:
#     print(k // (n-m))
# else:
#     print(k % (n-m))

# print(3 % 10)


# a = [351, 648, 776, 918]

# for i in a:
#     print((i // 100 + i % 10)*2)

# --------------------------

# a = [1,2,4,5,4,9,9,4,1,2,2,3,5,6,75,15,15,15,45,15,45,78,89]  massivində ikidən çox təkrarlanan elementləri silmək

# a = [1,2,4,5,4,9,9,4,1,2,2,3,5,6,75,15,15,15,45,15,45,78,89]
# b=[]

# for i in a:
#     if b.count(i) == 0:
#         b.append(i)

# print(b)

# təkrarlanan elementlərdən yeni massiv yaradın və yaradılan massivdə cüt və tək ədədləri göstərin

# t=[]

# n=int(input('eded daxil edin; '))

# def sumtwo(n):
#     while n % 2 == 0 and n > 1:
#         n = n/2
#     return n == 1

# print(sumtwo(n))


#  eks ardicilliq

# n = 156465
# m=str(n)
# print(m[::-1])


# evveline 3 yazmaq

# n= 45442

# b = [int(x) for x in str(n)]
# b=b+[4]

# print(b)


# ilk ve son reqem
# a=int(input('ededi daxil edin: '))
# ilk_raqam = (a // (10 ** (len(str(a)) - 1))) * 5
# son_raqam = (a % 10) * 2
# print(ilk_raqam, son_raqam)
# -----------------------

# kvadratin terefi ve perimetri
# a=int(input("terefi daxil edin: "))

# perimetr = a * 4
# sahesi = a * a
# print("sahesi: ", sahesi, "perimetri: ", perimetr)

# -----------------
# 2-nin quvveti olub olmadigi
# eded= int(input('ededi daxil edin: '))

# def is_power_of_two(n):
#     if n <= 0:
#         return False
#     while n % 2 == 0:
#         n = n / 2
#     return n == 1

# if is_power_of_two(eded):
#     print(eded, "2'nin kuvvetidir.")
# else:
#     print(eded, "2'nin kuvveti değildir.")

# -------------------------------
# eks ardicilliq
# eded= input('ededi daxil edin: ')
# print(eded[::-1])

# ------------------
# evveline 3 elave etmek
# eded= input('ededi daxil edin: ')
# yenilenen_sayi = str(3) + str(eded)
# print(yenilenen_sayi)


# 1) Daxil edilmiş ədəddən bir əvvəlki və bir sonrakı ədədi ekrana çıxaran funksiya
# eded = int(input('ededi daxil edin: '))
# a = eded

# def ededs():
#     global eded, a
#     eded = eded + 1
#     a = a - 1
# ededs()

# print(eded, a)

# 2) Daxil edilmiş sözün ilk və son hərfinin yerini dəyişən funksiya
# soz = input('Sözü daxil edin: ')

# ilk_harf = soz[0]
# son_harf = soz[-1]
# digerleri = soz[1:-1]
# yeni_soz = son_harf + digerleri + ilk_harf
# print(yeni_soz)


# 3) Daxil edilmiş cümlədə ilk və son sözü göstərən funksiya

# cumle=input('cumleni daxil edin: ')
# m=cumle.split()
# print(m[0])
# print(m[-1])

# 4) Daxil edilmiş massivdə elementlərini yerini əks ardıcıllıqla düzən funksiya

# a= input('sozu daxil edin:')
# print(a[::-1])

# Daxil edilmiş ədədin 100-dən böyük və cüt ədəd olduğunu göstərən funksiya

# a=int(input('ededi daxil edin:'))
# def eded ():
#     if a>100 and a%2==0:
#         print (a)
#     else:
#         print('eded 100 den kiçik tekdir')
# eded()

# Daxil edilmiş cümləni hərflərə ayıraraq ekrana çıxaran funksiya

# a=input('cumleni daxil edin:')
# def cumle():
#     b=list(a)
#     print(b)
# cumle()

# Ədəd 100-dən böyük olduqda True əks halda false qaytaran funksiya

# a=int(input('ededi daxil edin;'))
# def eded():
#     if a>100:
#         print(True)
#     else:
#         print(False)
# eded()

# 1-dən 2000-ə qədər bütün cüt ədədlərin cəmini və tək ədədlərin hasilini ekrana çıxarmaq

# s=0
# p=1
# for i in range (1,2001):
#     if i%2==0:
#         s=s+i
#     elif i%2==1:
#         p=p*i

# print("hasil",p)
# print("cem",s)

# 15-dən 60-a qədər 50-dən böyük ədədlərin içindən cüt ədədi ekrana çıxaran funksiya

# for i in range (15,61):
#     if i>50 and i%2==0:
#         print(i)

# Daxil edilmiş ədədin 50-dən kiçik və ya tək olduğunu göstərən funksiya
# a=int(input('ededi daxil edin:'))
# def eded():
#     if a<50 or a%2==1:
#         print(a)  
# eded()  

# daxil edilen ededi 10 defe tekrarla
# a= input('ededi daxil edin:')
# print(a*10)

# 0-dan 100-e kimi ededlerden 15 ile 20 arasinda olan ededlerin ceminin 4/1 ve 25 ile 30 arasinda olanlarin ceminin 6/1

# s = 0
# v=0
# for i in range(0,101):
#     if(i >= 15 and i<=20):
#         s=s+i
#     elif(i>=25 and i<=30):
#         v=v+i

# print(s*(1/4))
# print(v*(1/6))

# ilk herfi boyuk eden funk

# a=input("Sozu daxil edin: ")
# print(a.capitalize())

# ilk ve son herfin yerini deyisdiren

# =input("Sozu daxil edin: ")a
# ilkHerf = a[0]
# sonHerf = a[-1]
# digerHerfler = a[1:-1]

# yeniYarananSoz = sonHerf + digerHerfler + ilkHerf

# print(yeniYarananSoz)

# 1) daxil edilən birinci ədədin və ikinci ədədin cəminin 3cü daxil edilən ədəddən böyük olduğu halda ekrana 1-ci ilə 3-cü ədədin cəminin 2-ci ədədə olan nisbətini çıxarmaq əks halda False

# a=int(input('1 ededi daxil edin: '))
# b=int(input('2 ededi daxil edin: '))
# c=int(input('3 ededi daxil edin: '))

# if a+b>c:
#     print((a+c/b))
# else:
#     print(False)


# 2) birinci daxil edilən ədədin ikinci və üçüncü daxil edilən ədəddən böyük olduğu halda ekrana birinci və üçüncü ədədin hasilini çıxarmaq
# a=int(input('1 ededi daxil edin: '))
# b=int(input('2 ededi daxil edin: '))
# c=int(input('3 ededi daxil edin: '))

# if a>b and a>c:
#     print(a*c)
# else:
#     print(False)

# 3) daxil edilmis ədədlərin içərisindən təkrarlananları silmək (eyni anda daxil edilən ədədlər)

# a=int(input('1 ededi daxil edin: '))


# 4) daxil edilmiş sözün və ya cümlənin içərisindən rəqəmləri seçib ekrana çıxaran funksiya

# a=str(input('sozu daxil edin: '))

# reqemler = ["0","1","2","3","4","5","6","7","8","9"]

# for i in a:
#     if reqemler.count(i) > 0:
#         print(i)

# -----------------------------------------------------------------

# 1) 1-dən daxil edilmiş ədədə-ə qədər olan ədədlər içərisindən cüt olanı və 10-a tam bölünən ədədləri ekrana çıxaran funksiya (funksiya!)

# a=int(input('ededi daxil edin: '))
# def eded():
#     for i in range (1,a):
#         if i%2 == 0 and i%10 == 0:
#             print(i)
# eded()

# 3) daxil edilmis ədədlərin içərisindən təkrarlananları silmək (eyni anda daxil edilən ədədlər)



# 2) a = [1,2,4,5,4,9,9,4,1,2,2,3,5,6,75,15,15,15,45,15,45,78,89]  massivində ikidən çox təkrarlanan elementləri silmək

# a = [1,2,4,5,4,9,9,4,1,2,2,3,5,6,75,15,15,15,45,15,45,78,89]
# b=[]

# for i in a:
#     if b.count(i) == 0:
#         b.append(i)

# print(b)

# 3) Daxil ededin ededin polindrom olub olmamasini yoxlayan funksiya

# a=input('ededi daxil edin: ')
# if a[::-1] == a:
#     print("yes")
# else:
#     print("No")

# 4) Daxil edilen ededin sonuncu ededinden 1 vahid evvelde yerlesen ededi teyin eden funksiya

# a=int(input('ededi daxil edin: '))
# b=list(str(a))
# print(b[-2])

# ------------------------------------
# 1) Daxil edilən ədədin 4-də bir hissəsini ekrana çixarmaq

# a=int(input('ededi daxil edin: '))
# b=a*(1/4)
# print(b)

# 2) Daxil edilmiş cümlədə ilk və son sözü göstərən funksiya 

# a=input('cumleni daxil edin: ')
# b=a.split()
# ilk_soz=b[0]
# son_soz=b[-1]   
# print(ilk_soz, son_soz)

# 3) 1-den 20-yə qədər 2 rəqəmli və cüt ədədləri ekrana çıxaran funksiya
# def eded():
#     for i in range(1,21):
#         if i%2==0 and len(str(i))>1 :
#             print(i)
# eded()           
   

# 4) Daxil edilmiş cümlədə olan butun (tekrarlanmadan) reqemlerin kvadratlari cemi

# a=input('cumleni daxil edin: ')

# reqemler = ["0","1","2","3","4","5","6","7","8","9"]
# cumledeki_reqemler=[]
# tekrarlamadan=[]
# kvadrat = []
# ayriayri = ""

# for i in a:
#     if reqemler.count(i) > 0:
#         cumledeki_reqemler.append(i)

# for i in cumledeki_reqemler:
#     if tekrarlamadan.count(i) != 1:
#         tekrarlamadan.append(i)

# for i in tekrarlamadan:
#     kvadrat.append(int(i) ** 2)

# for i in kvadrat:
#     ayriayri += str(i) + ","

# print(ayriayri)

# 5) Daxil edilen ededin 100-den boyuy olub olmadigini ve cut eded olub olmadigini yoxlayan funksiya
# a=int(input('ededi daxil edin:'))
# def eded():
#     if a>100 and a%2==0 :
#         print('eded 100den boyuk ve cutdur')
#     else:
#         print('false')
# eded()

# ----------------------------------

# 1) Daxil ededin ededin polindrom olub olmamasini yoxlayan funksiya

# a=input('ededi daxil edin: ')
# def eded():
#     if a[::-1]== a :
#         print('eded polidromdur')
#     else:
#         print('false')   
# eded()        



# 2) Daxil edilen ededin sonuncu ededinden 1 vahid evvelde yerlesen ededi teyin eden funksiya
# a=int(input('ededi daxil edin: '))

# print(a - 1)


# 3) Daxil edilmiş cümlədə ilk və son sözü göstərən funksiya, əgər cümlə 2 hərflidirsə ekrana sözün özünü çıxartmaq

# a=str(input('cumleni daxil edin: '))
# b=a.split()
# print("Ilk soz: ",b[0])
# print("Son soz: ",b[-1])

# 3 reqemli ededin ozunun butun reqemlerine bolunub bolunmemesi

eded= int(input("ededi daxil edin: "))

def reqemlere_bolunme(sayi):
    reqemler = list(str(sayi))

    for reqem in reqemler:
        if reqem == '0' or sayi % int(reqem) != 0:
            return False

    return True

print(reqemlere_bolunme(eded))