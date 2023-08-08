# MISC FUNCTIONS
def deformatter( num ):
    deformatted = ""

    for i in num:
        if not ( i.isspace() or i == "," ):
            deformatted += i
        
    return deformatted

def formatter( number, dig ):
    num = deformatter( str( number ) )
    num_r = num[-1 : : -1]
    if( dig == 2 or dig == 16 ): grp = 4
    elif( dig == 8 or dig == 10 ): grp = 3

    formated = ""
    counter = 1
    for i in num_r:
        if ( counter <= grp ): 
            formated += i
            counter += 1
        else: 
            if( dig == 10 ): formated += ","
            else: formated += " "

            formated += i
            counter = 1
    
    return formated[-1 : : -1]

# CONVERSION FUNCTIONS
def al_num( num ):
    dic_n = { 10 : "A", 11 : "B", 12 : "C", 13 : "D", 14 : "E", 15 : "F" }
    dic = { "A" : 10, "B" : 11, "C" : 12, "D" : 13, "E" : 14, "F" : 15 }
    
    if( num in dic ): result = str( dic[num] ) 
    
    if( num in dic_n ): result = str( dic_n[num] )
    
    return result

def any_dec( number, dig, power ):
    num = deformatter( str( number ) )
    if ( num == "" ): return 0
    
    if( num[-1].isnumeric() ): result = int( num[-1] )
    else: result = int( al_num(num[-1] ) )
    
    return ( result ) * ( dig ** power ) + any_dec( num[0 : -1], dig, power + 1 )

def decany( num, dig ):
    if( num == 0 ): return "0"
    elif( num == 1 ): return "1"

    if( dig == 16 and ( num % dig ) > 9 ): result = al_num( num % dig )
    else: result = str( num % dig )

    return result + str( decany( num // dig, dig ) )

def dec_any( number, dig ):
    num = int ( deformatter( str ( number ) ) )

    temp_result = decany( num, dig )
    result = temp_result[-1: : -1]
        
    if not ( result[0] == "0" ): return result
    else: return result[1:]

# ARITHMETIC FUNCTIONS
def arithmetic( num1, num2, op ):
    if( op == "+" ): return int( num1 ) + int( num2 )
    elif( op == "-" ): return int( num1 ) - int( num2 )
    elif( op == "x" ): return int( num1 ) * int( num2 )
    elif( op == "/" ): return int( num1 ) / int( num2 ) 

# EXTRAS
"""
def negative( num, carry ):
    if( num == 0 and carry == 1): return "1" 
    a = ( num % 10 ) + carry
    if( a == 0 ): b = c = 0
    elif( a == 1 ): 
        b = 1
        c = 0
    elif( a == 2 ): 
        b = 0 
        c = 1
    return str( b ) + negative( num // 10, c )
"""