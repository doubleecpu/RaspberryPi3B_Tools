import subprocess as sp

def hasPHP():
    try:
        sp.check_call(['php','-v'])
        return True
    except:
        print("Not Installed")
        return False
    
#hasPHP()