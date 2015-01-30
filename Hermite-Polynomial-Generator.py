#Quantum Mechanics Problem G(2.26)



print('======================Program Start============================')
print('Quantum Mechanics, Spring 2015, HW 2, Problem 6, (G2.16), Matthew Cavener')
"a[j+2] = -2(n-j)/((j+1)(j+2)) * a[j] for n = 5 and n = 6"
"Set Coefficient of highest power of ksi to 2^n"
from fractions import Fraction
import timeit

#generates order n Hermite Polynomial
def hermitePoly(n):


#special case that breaks code (out of range of general lists used
    if n == 0:
        e = ('1')
        return e
        
#another special case
    if n == 1:
        e = ('2*k')
        return e

                                            
#creating the lists to be used
    a = []
    b = []
    c = []
    d = []

#performs the calculation, sets it into a reasonable fraction
    for j in range(n % 2,n,2):
        x = Fraction.from_float(-2 * (n - j) / ((j + 1)*(j + 2))).limit_denominator()
        a.append((x))

#solves the recursive function, getting each value in terms of a(n mod 2) by multiplying each term in the list by all the ones preceding it.
    for i in range(len(a) - 1, 0, -1):                                            
                                                                                        
        for k in range(0, i):                                                            
            a[i] = a[i] * a[k]
            
#finds the coefficient of the highest power and thus a(n mod 2)
    x = 2**n / a[len(a) - 1]

#plugs the a(n mod 2) in each term
    b = [y * x for y in a]
                                    
#adds the coefficient of the highest power to the list                                    
    b.insert(0,x)

#removes relic from Fraction.from_float *extraneous    
    #b = list(map(str,b))#removes relic from Fraction.from_float *extraneous

#reverses list order to give coefficient of highest power first
    b.reverse()                                                                             

#form is now (a(n), a(n-2), a(n-4), ... ,a(0)


#generating list of powers of ksi, and giving them the appropriate exponent
    for h in range (n,0,-2):                
        c.append('*k^'+str(h))      
        

#needs even/odd power distinction to include constant term at end for even degrees
    if n % 2 == 1:                          
        for g in range (0,len(b)):          #combines the coefficient list (b) with power list (c)
            d.append(str(b[g]) + str(c[g]))
    else:
        i = 0
        for i in range (0,len(c)):
            d.append(str(b[i]) + str(c[i])) #combines coeff. with powers
        d.append(str(b[len(b)-1]))          #adds constant ter to end


#now a(n)*k^n, a(n-2)*k^n-2,... a(1)*k, a0

            
    sep = ' + '                             #defines seperator of each term in the list
    e = sep.join(d)                         #creates the polynomial by adding each term

#now a(n)*k^n + a(n-2)*k^n-2 + ... + a(1)*k + a0

    return e


    #check = timeit.default_timer()          
    #t = check - start
    #print('Runtime was ' + str(t) + 'seconds.')
    
""" ########END HERMITEPOLY ##################### END HERMITEPOLY ##################### END HERMITEPOLY ##################### END HERMITEPOLY ####################

#-----------------------------------------------------------------------------------------------------------------------

#########Begin User interface########Begin User interface########Begin User interface########Begin User interface########Begin User interface#######"""

print('')

#asks user if they need all up to a certain amount to be asked later
t = str(input('Would you like a table of Hermite polynomials? [Y/n] '))

if t not in ( "n", "N", "Y", "y"):
    print('Invalid input. Fleeing dangerous user. ')          
    start = timeit.default_timer()
    print('')
    
    
elif t in ("y", "Y"):

    n = int(input('What is the highest degree needed? '))
    start = timeit.default_timer()
    print('')

#calls the function for each integer from 0 to the highest degree needed    
    for Ca in range (0 , n + 1):                                                        
        print('H' + str(Ca) + ' = ' + str(hermitePoly(Ca)))

elif t in ("N", "n"):

    n = int(input('What degree polynomial is needed? '))
    start = timeit.default_timer()
    print('')

    print('H' + str(n) + ' = ' + hermitePoly(n))

#times the function
check = timeit.default_timer()          
t = str(check - start)[:7]
print('')
print('Runtime was ' + str(t) + ' seconds.')
print('===================================Program End==========================')

####### END SCRIPT ############ END SCRIPT ############ END SCRIPT ############ END SCRIPT ############ END SCRIPT #####


