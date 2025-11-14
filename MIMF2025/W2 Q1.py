def ip(v1, v2):

    ip_out=0

    if len(v1) == len(v2):
        
        for i in range (len(v1)):
            
            ip_out += v1[i]*v2[i]

        return ip_out
    else:
        return print("Vectors must be of the same length")

#put test cases here...
v1 = [ 1, 2, 3,-1]
v2 = [-2, 1, 1, 3]

#print the output
print(f'The inner product(aka dot product) of {v1} and {v2} is: {ip(v1,v2)}')

#The inner product(aka dot product) of [1, 2, 3, -1] and [-2, 1, 1, 3] is: 0##
#Done!
