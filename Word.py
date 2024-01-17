input = str(input(""))

if sum(map(str.islower, input)) > sum(map(str.isupper, input)) :
    # ja ir vairāk ar mazajiem burtiem
    print(input.lower())
elif sum(map(str.isupper, input)) > sum(map(str.islower, input)) :
    # ja ir vairāk ar lielajiem burtiem
    print(input.upper())
elif sum(map(str.islower, input)) == sum(map(str.isupper, input)) :
    # ja ir vienādi
    print(input.lower())
else :
    print("err")
