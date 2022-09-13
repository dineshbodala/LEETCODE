x=[1,2,3,4,5,6]
def ls(x,y):
    if x[0]==y:
        return 'blah'
    else:
        return ls(x[1:],y)
print(ls(x,3))