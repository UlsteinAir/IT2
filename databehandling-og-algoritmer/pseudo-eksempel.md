## Penger tjent per sang

### Pseudokode i "naturlig språk"
```pseudo
Hent inn land fra bruker (input)
Hvis land er lik Norge:
    Print $0.44 per sang
Ellers hvis land er lik Sverige:
    Print $0.34 per sang
Ellers 
    Print $0.22 per sang
```

### Pseudokode som følger UDIRs standard 
```pseudo
SET land TO READ "Hvor kommer du fra?"
IF land EQUAL TO "Norge"
    THEN DISPLAY "$0.44 per sang"
ELSE IF land EQUAL TO "Sverige"
    THEN DISPLAY "$0.34 per sang"
ELSE
    THEN DISPLAY "$0,22 per sang"
ENDIF
```

### Pyton-kode
```python
land = input("Hvor kommer du fra?")
if land.lower() == "Norge":
    print("$0.44 per sang")
elif land.lower() == "Sverige":
    print("$0.34 per sang")
else:
    print("$0,22 per sang")
```


## Andel penger tjent per sang

### Pseudokode i "naturlig språk"
```pseudo
Hent inn antall streams fra bruker
Hvis antall streams er større enn 30 000 000
    Print "penger tjent per sang lik 70%"
Ellers hvis antall streams er større enn 1 400 000
    Print "penger tjent per sang lik 40%"
Ellers
    Print "penger tjent per sang lik 0%"
```

### Pseudokode som følger UDIRs standard 
```pseudo
SET streams TO READ "Hvor mange streams har du?"
IF streams GREATER THEN 30 000 000
    THEN DISPLAY "penger tjent per sang lik 70%"
ELSE IF streams GREATER THEN 1 400 000
    THEN DISPLAY "penger tjent per sang lik 40%"
ELSE
    THEN DISPLAY "penger tjent per sang lik 0%"
ENDIF
```

### Python-kode
```python
streams = int(input("Hvor mange streams har du?"))
if streams > 30000000:
    print("penger tjent per sang lik 70%")
elif streams > 1400000:
    print("penger tjent per sang lik 40%")
else:
    print("penger tjent per sang lik 0%")
```