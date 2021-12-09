def maskify(cc):
    masked = ''
    for i in cc[0:-4]:
        masked += '#'
    masked += cc[-4:]
    return masked
