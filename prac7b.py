def FA(s):
    if len(s)<3:
        return "rejected"
    if s[0]=='1':
        if s[1]=='0':
            #if s[2]=='1':
                for i in range(2,len(s)):
                    if s[i]!='1':	
                        return "rejected"
                    return "Accepted"
            #return "rejected"
        return "rejected"        
    return "rejected"		
inputs=['1','10101','101','10111','010101','100','10111101','10111111']
for i in inputs:
    print(i)
    print(FA(i))