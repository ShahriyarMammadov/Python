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


a=int(input('reqemi daxil edin: ' ))
print(a**(1/2))
