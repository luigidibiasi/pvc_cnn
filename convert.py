writer = open("./pvc_string.fasta","w")
reader = open ("./pvc.csv")
i=0
for ecg in reader:
    ecg = ecg.replace("\n","")
    last_val = None
    writer.write(">ecg_"+str(i)+"\n")
    i+=1
    for sample in ecg.split("\t"):
        if (last_val!=None):
            if (sample>last_val):
                writer.write("a")
            else:
                if(sample<last_val):
                    writer.write("c")
                else:
                    writer.write("t")
        else:
            writer.write("s")
        last_val=sample
    writer.write("e\n")
