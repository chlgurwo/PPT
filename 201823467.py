Python 3.7.8 (v3.7.8:4b47a5b6ba, Jun 27 2020, 04:47:50) 
[Clang 6.0 (clang-600.0.57)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>> a = int(input('첫 번째 숫자를 입력하세요"))
b = int(input('두 번째 숫자를 입력하세요'))

result = a + b
print(a, '+', b,'=',result)

result = a-b
print(a, '-', b,'=',result)
              
              

SyntaxError: EOL while scanning string literal
>>> 
=================== RESTART: /Users/d7703_13/Documents/gg.py ===================
첫 번째 숫자를 입력하세요
Traceback (most recent call last):
  File "/Users/d7703_13/Documents/gg.py", line 1, in <module>
    a = int(input('첫 번째 숫자를 입력하세요'))
ValueError: invalid literal for int() with base 10: ''
>>> a
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> quit
Use quit() or Ctrl-D (i.e. EOF) to exit
>>> 
=================== RESTART: /Users/d7703_13/Documents/gg.py ===================
1st input?
Traceback (most recent call last):
  File "/Users/d7703_13/Documents/gg.py", line 1, in <module>
    a = int(input('1st input?'))
ValueError: invalid literal for int() with base 10: ''
>>> b
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    b
NameError: name 'b' is not defined
>>> 
=================== RESTART: /Users/d7703_13/Documents/gg.py ===================
첫번 째 숫자를 입력하세요10
두번 째 숫자를 입력하세요20
10 + 20 = 30
10 - 20 = -10
10 * 20 = 200
10 / 20 = 0.5
1st input?10
2nd input?10
10 + 10 = 20
10 - 10 = 0
10 * 10 = 100
10 / 10 = 1.0
>>> 20
20
>>> 10
10
>>> 2625665145644654546542135648651015201266
2625665145644654546542135648651015201266
>>> 
=================== RESTART: /Users/d7703_13/Documents/gg.py ===================
1st input?
=================== RESTART: /Users/d7703_13/Documents/gg.py ===================
1st input?9
2nd input?9
9 + 9 = 18
end of block
>>> 5
5
>>> 5
5
>>> 5
5
>>> 5
5
>>> 0
0
>>> 0
0
0
>>> 
>>> 0
0
>>> 0
0
>>> 