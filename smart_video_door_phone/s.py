from multiprocessing import Pool,Manager,Value,Process
import time




def a(i,s,p):
    while(i.value[0]<10):
        time.sleep(s+1)
        print(str(i.value[0])+' '+str(s))
        i.value[0]=i.value[0]+1






# if __name__=='__main__':
#     i=Value('i',[0,10])
#     # with Pool(8) as p:
#     #     p.starmap(a,[(i,'1',1),(i,'2',3)])
#     for j in range(2):
#         Process(target=a, args=[i,j,1]).start()
#
#     print('final'+str(i))
