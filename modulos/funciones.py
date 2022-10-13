import datetime

def substr(msg,inicial, final):
    return msg.strip()[inicial:final] 
 

def printlog(prompt):
    """
        Funcion para imprimir logs 
    """
    year, mon, mday, hour, min, sec, wday, yday, isdst = time.localtime()
    print("%04d-%02d-%02d %02d:%02d:%02d %s" % (year, mon , mday, hour, min, 
sec, prompt))
