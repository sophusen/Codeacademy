inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'], # Assigned a new list to 'pouch' key
    'backpack' : ['xylophone','dagger', 'bedroll','bread loaf']
}
#print inventory

# Adding a key 'burlap bag' and assigning a list to it
inventory['burlap bag'] = ['apple', 'small ruby', 'three-toed sloth']
#print inventory

# Sorting the list found under the key 'pouch'
inventory['pouch'].sort() 
#print inventory

# Your code here
#adding pocket key and assigning list of strings:
inventory['pocket']=['seashell', 'strange berry', 'lint']
#print inventory

# Sorting the list found under the key 'backpack'
inventory['backpack'].sort()
#print inventory

#removing dagger from backpack key:
inventory['backpack'].remove('dagger')
#print inventory

#adding 50 to the existing value in the gold key:
inventory['gold']=inventory['gold']+50
print inventory
