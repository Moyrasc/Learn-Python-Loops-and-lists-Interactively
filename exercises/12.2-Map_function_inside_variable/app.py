names = ['Alice','Bob','Marry','Joe','Hilary','Stevia','Dylan']


#Your code go here:
def prepender(name):
    return f"My name is: {name}"

new_list = list(map(prepender, names))
print(new_list)