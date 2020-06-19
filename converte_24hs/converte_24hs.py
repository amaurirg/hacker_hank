def converte_24hs(s):
    h = int(s[0:2])
    if s.endswith('AM'):
        if not h == 12:
            s = s[0:-2]
        else:
            s = s.replace(s[0:2], '00')[0:-2]
    elif s.endswith('PM'):
        if not h == 12:
            s = s.replace(s[0:2], str(h + 12))[0:-2]
        else:
            s = s.replace(s[0:2], '12')[0:-2]
    return s
