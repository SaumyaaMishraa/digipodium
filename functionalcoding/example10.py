def saveInfo(file='info.text',**kwargs):
    with open (file,'a') as f:
        for k,v in kwargs.items():
            f.write(f'{k}->{v}\n')
saveInfo(mobile='motorola',prive='200000',expiry='2023',features='whatever')