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