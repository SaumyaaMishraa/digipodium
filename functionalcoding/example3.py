data= '' # global variable
def data_appender (s):
    global data  #this line tells data_appender that we a global var data
    if len(s)>0:
        data += s

#calls
print(data_appender('hello'))
print(data_appender('world'))
print(data_appender('this is simple '))
print(data_appender('abcd'))