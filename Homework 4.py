4.1 Easy

import random
our_list = [random.randint (-100, 100) for _ in range(10)]
print(our_list)
sqr_list = list(map(lambda x: x*x, our_list))
print(sqr_list)


4.2 Easy

fruits_one = ["apple", "pear", "pineapple", "plum", "cherry",]
fruits_two = ["strawberry", "pear", "watermelon", "cherry", "plum"]
common_fruits = [fruit for fruit in fruits_two if fruit in fruits_one]
print(common_fruits)


4.3 Easy

import random
ran_list = [random.randint(-100, 100) for _ in range(20)]
print(ran_list)
new_list = [num for num in ran_list if num % 3 == 0 and num > 0 and num % 4 != 0]
print (new_list)


4.1 Normal

import re
instr = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
result = re.split(r'[A-Z]+', instr )
print(result)


4.2 Normal

import re
instr = "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
result = re.findall(r'([a-z][a-z])([A-Z]+)([A-Z][A-Z])', instr)
answer = [i[1] for i in result]
print(answer)


4.1 Hard

# Не получилось в одну строчку

matrix = [
    [1, 0, 8],
    [3, 4, 1],
    [0, 4, 2]
]
print("matrix_rotate = " )
for line in list(map(list, zip(*matrix))):
    print(line)



4.2 Hard

# Никак не получилось короче. И мне не нравится, как я записал это большое число. Ничего не придумал. Но работает

n = 0
max = 0
number = '73167176531330624919225119674426574742355349194934'\
'96983520312774506326239578318016984801869478851843'\
'85861560789112949495459501737958331952853208805511'\
'12540698747158523863050715693290963295227443043557'\
'66896648950445244523161731856403098711121722383113'\
'62229893423380308135336276614282806444486645238749'\
'30358907296290491560440772390713810515859307960866'\
'70172427121883998797908792274921901699720888093776'\
'65727333001053367881220235421809751254540594752243'\
'52584907711670556013604839586446706324415722155397'\
'53697817977846174064955149290862569321978468622482'\
'83972241375657056057490261407972968652414535100474'\
'82166370484403199890008895243450658541227588666881'\
'16427171479924442928230863465674813919123162824586'\
'17866458359124566529476545682848912883142607690042'\
'24219022671055626321111109370544217506941658960408'\
'07198403850962455444362981230987879927244284909188'\
'84580156166097919133875499200524063689912560717606'\
'05886116467109405077541002256983155200055935729725'\
'71636269561882670428252483600823257530420752963450'



for count in range(n, len(number) - 4):
    mult = 1

    for i in range(count, count+5):
        mult = mult * int(number[i])
        if mult > max:
            max, index = mult, count
    # print("index: ", count, "multiplication: ", mult)     Это я проверял
print("max_index:", index, ",", "max_mult:", max)


