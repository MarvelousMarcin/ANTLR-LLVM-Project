## Język LOVELang

### 1. Zmienne

Przypisanie zmiennej wartości odbywa się przy pomocy polecenie LOVE

`a LOVE 2`

`b LOVE 4.0`

`c LOVE "test"`

`d LOVE {1, 2, 3, 4}`

### 2. Operacja na liczbach całkowitych

`a LOVE 3 + 4`

`a LOVE 3 * 4`

`a LOVE 3 - 4`

### 3. Operacja na liczbach rzeczywistych

```
a LOVE 1.0
b LOVE 2.0
z LOVE 3.0

p LOVE  (float)1.0
d LOVE  (float)3.0

c LOVE p / d

show c
```

### 4. Strings

```
gets b

a LOVE "ma kota "

z LOVE "ala " + "ma kota "

show b
show z
```

### 5. Tablice

```
a LOVE {11,32,33,22}

show a

a[3]
```

### 6. Funkcje

```
fLOVE pow
  x LOVE 100
  pow LOVE x * x
endfLOVE

z LOVE pow
```

### 7. Struktury

```
struct Person
     age
     height
     bmi
endstruct

Person HEART person
person.age LOVE 13

show person.age
```

### 7. Dynamiczna typizacja

```
a LOVE 13
b LOVE 16.0
c LOVE {1,2,3,4}
d LOVE "ala"

show a
show b
show c
show d

```

### 8. Klasy

```
fLOVE pow
  x LOVE 100
  pow LOVE x * x
endfLOVE

class Person
    age
    call
endclass

Person CLASS person

person->age LOVECLASS 13
person->call LOVECLASS pow

show person->age


```
