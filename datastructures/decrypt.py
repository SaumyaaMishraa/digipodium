def Drecypt(str):
    ans=input("enter ur word")
    ap =' zyxwvutsrqpomlkjihgfedcba'
    for i in range (0, len(str)):
        ans+= ap [ord (str[i]-97)]
    return ans