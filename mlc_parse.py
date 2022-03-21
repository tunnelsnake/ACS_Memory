

files = ["mem_2_256.txt", "mem_2_64.txt", "mem_3_256.txt", "mem_3_64.txt", "mem_4_256.txt", "mem_4_64.txt", "mem_5_256.txt", "mem_5_64.txt"]
files = ["output/" + x for x in files]

if __name__ == "__main__":

    for filename in files:

        lines = []
        with open(filename, 'r') as f:
            lines = f.readlines()

        # discard all the lines before the ====== divider
        tmp = []

        table_begins_at = -1
        for i in range(len(lines)):
            if '=' in lines[i]:
                table_begins_at = i
                break

        lines = lines[i+1:]
        # print(str([line.split() for line in lines]))

        out = ["Inject_Delay,Latency(ns),Bandwidth(MiB/s),\n"]
        for line in lines:
            line = ",".join(line.split()) + ",\n"
            out.append(line)

        with open(filename.split(".")[0] + ".csv", 'w') as f:
            f.writelines(out)
