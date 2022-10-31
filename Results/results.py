import dictionary_file_based_class as df
import time
import csv


# All inputs used for testing: 
input_filenames = ['words500.txt','words1000.txt','words5000.txt','words10000.txt','words20000.txt','words50000.txt','words100000.txt']
methods = ['array','linkedlist','trie']
command_filenames = ['testconstruct.in','testadd.in','testdel.in','testsearch.in','testAC.in','testfull.in']
commandout_filenames = ['testconstruct.out','testadd.out','testdel.out','testsearch.out','testAC.out','testfull.out']


output = open('output.csv','w')
writer=csv.writer(output)

# Iterate through every unique set of inputs 20 times and compute the average time
for data in input_filenames:
    for approach in methods:
        row = []
        for i,file in enumerate(command_filenames):
            times=[]
            for w in range(0,20):
                args=['',approach,data,file,commandout_filenames[i]]
                if file == 'testconstruct.in' or file == 'testfull.in':
                    starttime = time.time()
                    df.dict_file().main(args=args)
                    endtime = time.time()
                    timetaken = endtime - starttime
                    times.append(timetaken)
                else:
                    a= df.dict_file()
                    a.main(args)
                    times.append(a.time)

            avg_time = (sum(times)/len(times))
            print(f"Time taken = {(avg_time ):.8f} sec",file,approach,data)
            row.append(avg_time)
        
        writer.writerow(row)
        

output.close()
