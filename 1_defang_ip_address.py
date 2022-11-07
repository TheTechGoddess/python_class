'''def ip_address(address):
	new_address = ''
	split_address = address.split('.')
	#print(address)
	print(split_address)
	seperator = '[.]'
	new_address = seperator.join(split_address)
	print(new_address)


ip_address('https://favour-cell.github.io/NASA-API-project/')'''
'''def outer_function(a, b):
    def inner_function(c, d):
        return c + d
    return inner_function(a, b)
 
result = outer_function(5, 10)
print(result)'''

def foo(a, b=4, c=6):
    print(a, b, c)

foo(5, c=12)    
