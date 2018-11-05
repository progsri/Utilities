pid = 24268 #Enter pid here
file_smaps = "/proc/" + str(pid) + "/smaps"

file_smaps_obj = open(file_smaps, "r")
file_smaps_store = file_smaps_obj.readlines()
file_smaps_obj.close()

#print(file_smaps_store)

fields = ['Size','KernelPageSize','MMUPageSize','Rss','Pss','Shared_Clean','Shared_Dirty',
          'Private_Clean','Private_Dirty','Referenced','Anonymous','LazyFree','AnonHugePages',
          'ShmemPmdMapped','Shared_Hugetlb','Private_Hugetlb','Swap','SwapPss','Locked', 'VmFlags']
store = {}
#parts = {'Rss':0,'count':0}

library = '********************' #dummy
for line in file_smaps_store:
    tmp1 = line.split(":")

    if tmp1[0] not in fields:
        #print(line)
        tmp2 = line.split(" ")
        library = tmp2[len(tmp2) - 1]
        library = library.replace("\n","")
        if not library:
            library = "EMPTY AREA"
        #print(library)

        if library in store:
            store[library]['count'] = store[library]['count'] + 1
        else:
            store[library] =  {'Rss':0,'count':1}

    if tmp1[0] == 'Rss':
        if library in store:
           rss = tmp1[1].replace("kB","")
           rss = rss.replace(" ", "")
           store[library]['Rss'] = store[library]['Rss'] + int(rss)
        else:
            print("should not happen for Rss")

#print(store)
total_rss = 0
for key in store:
    total_rss = total_rss + store[key]['Rss']
    print(key + " --- " + str(store[key]['count']) + " --- " + str(store[key]['Rss']))

print("Total Rss " + str(total_rss))
