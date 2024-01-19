#python lifted_bed_to_gwas.py -i <original gwas file>
import sys
import getopt
import gzip
import pandas as pd

def main():
    filename = take_input()
    # filename="test"
    file_basename=filename.split(".")[0]
    df = pd.read_csv(filename, sep='\s+')
    df=df[["#chrom","pos","rsids"]]
    df.set_axis(['CHR', 'BP_end', 'ID'], axis=1, inplace=True)
    df["BP_start"] = df["BP_end"] - 1
    df["CHR"] = "chr" + df["CHR"].astype(str)
    df=df[["CHR","BP_start","BP_end","ID"]]
    df.to_csv(file_basename+".bed", sep='\t', index=False,header=False)
    return
def take_input():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "i:")
    for opt, arg in opts:
        if opt in ['-i']:
            filename = arg
    return filename
main()