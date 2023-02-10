data_path='../domains/data/'
cndm_file='./cndm.txt'

import re
cndm=open(cndm_file,'w')
# referring to https://github.com/v2fly/domain-list-community
def handle_file(file): # param: file
    try:
        fp=open(data_path+file)
    except:
        print('file "',data_path+file,'" doesn\'t exist')
        return
    while True:
        line = fp.readline() 
        if not line:
            break
        line=line[:-1] # remove line break
        line=re.sub(r'#.*$','',line) # clear comment
        line=re.sub(r'@.*$','',line) # issue v2fly/domain-list-community/issues/390
        line=re.sub(r' +$','',line) # clear spaces
        if line=="": # skip empty lines
            continue
        # handle
        ll=line.split(":")
        #print(ll)
        # error
        if len(ll)<1 or len(ll)>2:
            print("invalid line: ",ll)
        # raw domain
        elif len(ll)==1:
            cndm.write('.'+ll[0]+'\n')
        # include
        elif ll[0]=="include":
            handle_file(ll[1])
        # regexp and full
        elif ll[0]=="full" or ll[0]=="regexp":
            cndm.write(ll[1]+'\n')
        # domain
        elif ll[0]=="domain":
            cndm.write('.'+ll[1]+'\n')
        # else
        else:
            print("invalid line: ",ll)
    fp.close()

if __name__=='__main__':
    handle_file("geolocation-cn")
