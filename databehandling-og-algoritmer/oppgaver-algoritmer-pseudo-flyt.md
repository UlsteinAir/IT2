# Oppgaver - Algoritmer, pseudokode og flytdiagram 

## Oppgave 1 

svar: en løkke som kjører så lenge en bestemt betingelse er sann

## Oppgave 2

svar: en for-løkke er best egnet når du vet hvor mange ganger du vil at løkken skal kjøre

## Oppgave 3

svar: å representere data og funksjoner som objekter

## Oppgave 4

svar: den ligner på vanlig menneskespråk

## Oppgave 5
```pseudo
SET m TO 3
SET i TO 1
WHILE i GREATER THAN m
  DISPLAY "Lykkelig dag!"
  INCREMENT i
ENDWHILE
```

```python
m = 3
i = 1
while i > m:
    print("Lykkelig dag!")
    i += 1
```
svar: ingen ganger

## Oppgave 6
```pseudo
SET i TO 1
FOR hver i LESSER OR EQUAL 5
  PRINT i
ENDFOR
```
```python
i = 1
for i in range(i,6):
    print(i)
```
(1,2,3,4,5)

```pseudo
SET i TO 1
WHILE i < 5
  PRINT i
  INCREMENT i 
ENDWHILE
```
```python
i = 1 
while i < 5:
    print(i)
    i += 1
```
(1,2,3,4)

```pseudo
SET i TO 0
FOR hver i LESSER OR EQUAL 4
  PRINT i+1
ENDFOR
```
```python
i = 0 
for i in range(i,5):
    print(i+1)
```
(1,2,3,4,5)

```pseudo
SET i TO 1
WHILE i <= 5
  PRINT i
  INCREMENT i BY 2
ENDWHILE
```
```python
i = 1
while i <= 5
    print(i)
    i += 2
```
(1,3,5)

svar: 1 og 3

## Oppgave 7

svar: flytdiagram.png

## Oppgave 8
```pseudo
FUNCTION trekanttall (n)
  SET tn TO n * (n+1)/2
  RETURN tn
ENDFUNCTION
```
```python
def trekanttall(n):
  tn = n * (n+1)/2
  return tn

trekanttall(1)
```

## Oppgave 9

# 1 
```pseudo
SET n TO 1
WHILE n LESSER THAN OR EQUAL TO 10
  INCREMENT n
  DISPLAY n
ENDWHILE
```
(2,3,4,5,6,7,8,9,10,11)

# 2
```pseudo
SET n TO 0
FOR hver n LESSER THAN OR EQUAL TO 10
  DISPLAY n
ENDFOR
```

```python
n = 0
for n in range(11):
  print(n)
```
(0,1,2,3,4,5,6,7,8,9,10)

# 3
```pseudo
SET n TO 1
WHILE n LESSER THAN 10
  DISPLAY n
  INCREMENT n
ENDWHILE
```

```python
n = 1
while n < 10:
  print(n)
  n += 1
```
(1,2,3,4,5,6,7,8,9)

# 4 
```pseudo
SET n TO 1
FOR hver n LESSER THAN OR EQUAL TO 10
  DISPLAY n
ENDFOR
```

```python
n = 1 
for n in range(n, 11):
  print(n)
```
(1,2,3,4,5,6,7,8,9,10)

# svar = 4

## Oppgave 10

# svar:
1-F
2-H
3-A
4-B
5-C
6-G
7-E
8-D


## Oppgave 11

```python
listen = [32, 10, -5, 99, 1]
# 1. (Riktig)
størst = float("-inf")
for tall in listen:
  if tall > størst:
    størst = tall 
listen.remove(størst)
nestStørst = float("-inf")
for tall in listen:
  if tall > nestStørst:
    nestStørst = tall
print(nestStørst)

# 2. (Feil)
størst = listen[0]
nestStørst = listen[1]

if nestStørst > størst:
  størst, nestStørst = nestStørst, størst # bytter verdier på variablene
for tall in listen[2:]:
  if tall > størst:
    nestStørst = størst 
    størst = tall
  elif tall > nestStørst and tall != størst:
    nestStørst = tall
print(nestStørst)

# 3. (Feil)
størst = float("-inf")
nestStørst = float("-inf")
for tall in listen:
  if tall > størst:
    nestStørst = størst 
    størst = tall
  elif tall > nestStørst:
    nestStørst = tall 
print(nestStørst)

# 4.

```

# svar: 1 og 4

