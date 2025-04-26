league_name="champions league"
print(len(league_name))
print("first character:",league_name[0])
print("secound character:",league_name[2])
print("third character:",league_name[-1])

#slicing
print("first word:",league_name[0:9])
print("secound word:",league_name[10:])

#concotenation
year="2024"
full_name=league_name +" " + year
print(full_name)
print(league_name.lower())
print(league_name.upper())

text=input('enter string: ')
revtext=text[::-1]
print(revtext)
