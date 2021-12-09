def maskify(cc):
    masked = ''
    masked += '#'*len(cc[0:-4])
    masked += cc[-4:]
    return masked