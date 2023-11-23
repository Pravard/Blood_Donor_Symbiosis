from names import *
import random

hosps = ['H001','H002','H003','H004','H005','H006','H007','H008','H009','H010']
blood = ['O+','O-','A+','A-','B+','B-','AB+','AB-']
orgs = ['ORG001','ORG002','ORG003','ORG004','ORG005','ORG006']

date = [12,1,2012]
def date_increment(tup):
    p = random.randint(4,10)
    if tup[0]+p > 28:
        if tup[1] == 12:
            tup[1] = 1
            tup[2]+=1
        else:
            tup[1]+=1
        
    return [((tup[0]+p)%27)+1,tup[1],tup[2]]

def stringify(a):
    if a<10:
        return '00'+str(a)
    if a<100:
        return '0'+str(a)
    else:
        return str(a)
    

for k in range(1,100):
    n = random.randint(1,100)
    print(f"UPDATE Patient SET blood_grp = '{random.choice(blood)}' where pat_id = 'P{stringify(k)}';")
    date = date_increment(date)