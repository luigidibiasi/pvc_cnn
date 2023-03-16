writer = open("pvc.pattern.1.csv","w");
with open("pvc.out") as reader:
    for i in range(0,3):
        reader.readline()
    for line in reader:
        line = line.replace("\n","")
        if (line==""):
            break

        #remove spaces
        while ("  " in line):
            line = line.replace("  "," ")
        ldata = line.split(" ")
        ecg_name = ldata[0]
        ecg_signal = ldata[1]
        isStarted = 0
        ecg_mapped = "";
        signal_val=0 
        writer.write(ecg_name)
        writer.write(",")
        for c in ecg_signal:
            if (c=="A"):
                signal_val+=1
            if (c=="C"):
                signal_val-=1
            if (c=="-"):
                signal_val=0;
            writer.write(str(signal_val));
            writer.write(",")
        writer.write("\n")

