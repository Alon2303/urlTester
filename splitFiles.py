NUM_OF_LINES=2000000
filename = 'goodUrls.csv'
with open(filename) as fin:
    fout = open("output0.txt","wb")
    for i,line in enumerate(fin):
      fout.write(line)
      if (i+1)%NUM_OF_LINES == 0:
        fout.close()
        fout = open("output%d.txt"%(i/NUM_OF_LINES+1),"wb")

    fout.close()