listen = [32, 99, 99, 99, 99]
størst = float("-inf")
nestStørst = float("-inf")
for tall in listen:
  if tall > størst:
    nestStørst = størst 
    størst = tall
  elif tall > nestStørst:
    nestStørst = tall 
print(nestStørst)