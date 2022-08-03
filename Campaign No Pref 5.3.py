import random
random.seed()
All_Shifts=5
Shifts=[[0]]
Shift=1
n=4
Ps=10   # Preferance Same
Lp=0    # Lowest Pref
Volunteers= {
    'A':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps},
    'B':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps},
    'C':{1:Ps, 2:Ps, 3:Ps, 4:Lp, 5:Ps},
    'D':{1:Lp, 2:Ps, 3:Ps, 4:Lp, 5:Lp},
    'E':{1:Lp, 2:Ps, 3:Lp, 4:Lp, 5:Ps},
    'F':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps},
    'G':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps},
    'H':{1:Ps, 2:Ps, 3:Ps, 4:Lp, 5:Ps},
    'I':{1:Lp, 2:Ps, 3:Ps, 4:Lp, 5:Lp},
    'J':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps},
    'K':{1:Ps, 2:Lp, 3:Ps, 4:Lp, 5:Ps}
}

Popular=[]
while Shift<=All_Shifts:
    Sum=0
    for key in Volunteers:
        Sum+=Volunteers[key][Shift]
    Sum=str(Sum).zfill(4)
    Popular.append(f"{Sum} {Shift}")
    Shift+=1
Popular.sort()

for i in Popular:
    Shift=int(i[5])
    Vol_Sub=Volunteers
    Vol_Sort=[]
    for key in Vol_Sub:
        if Vol_Sub[key][Shift]>0:
            Vol_Sub[key][Shift]+=round(random.random()/100, 4)
        else:
            Vol_Sub[key][Shift]-=round(random.random()/100, 4)

    Vol_Sub=dict(sorted(Vol_Sub.items(), key=lambda item: item[1][Shift], reverse=True))

    Picked=0
    Vol_Sort.append(Shift)
    for key in Vol_Sub:
        if n>Picked:
            Vol_Sort.append(key)
            Picked+=1
            for shft in Volunteers[key].keys():
                Volunteers[key][shft]=round(Volunteers[key][shft]-0.5 , 3)
    # Ce sont pour les subtitutions:
        elif n<=Picked<=n:
            Vol_Sort.append(['Subtitute', key])
            Picked+=1

    Shifts.append(Vol_Sort)

Shifts.sort()
#print(Shifts)
A,B,C,D,E,F,G,H,I,J,K=0,0,0,0,0,0,0,0,0,0,0
for a in range(1,len(Shifts)):
    A+=Shifts[a].count('A')
    B+=Shifts[a].count('B')
    C+=Shifts[a].count('C')
    D+=Shifts[a].count('D')
    E+=Shifts[a].count('E')
    F+=Shifts[a].count('F')
    G+=Shifts[a].count('G')
    H+=Shifts[a].count('H')
    I+=Shifts[a].count('I')
    J+=Shifts[a].count('J')
    K+=Shifts[a].count('K')
for indx in range(1,All_Shifts+1):
    print(Shifts[indx])
print(f'\nA:{A}, B:{B}, C:{C}, D:{D}, E:{E}\nF:{F} G:{G}, H:{H}, I:{I}, J:{J} K:{K}\n_____________')
