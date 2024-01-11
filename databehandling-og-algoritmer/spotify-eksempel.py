# Oppgave: Lag koden for pseudokoden vår

land = input("Hvor kommer du fra?")

if land.lower() == "Norge":
    print("$0.44 per sang")
elif land.lower() == "Sverige":
    print("$0.34 per sang")
else:
    print("$0,22 per sang")

streams = int(input("Hvor mange streams har du?"))

if streams > 30000000:
    print("penger tjent per sang lik 70%")
elif streams > 1400000:
    print("penger tjent per sang lik 40%")
else:
    print("penger tjent per sang lik 0%")

