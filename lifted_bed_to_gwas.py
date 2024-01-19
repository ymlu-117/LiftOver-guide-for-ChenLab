#python lifted_bed_to_gwas.py -i <original gwas file> -b <lifted bed file>
import sys
import getopt
import gzip
import pandas as pd

def main():
    (old_gwas_filename,bedfilename) = take_input_2var()
    # old_gwas_filename="test"
    # bedfilename="bedtest"
    outputfile_base = bedfilename.split(".")[0]
    header=["CHR","BP_start","BP_end","SNP"]
    dfoldgwas=pd.read_csv(old_gwas_filename, sep='\s+')
    dfbed=pd.read_csv(bedfilename,sep='\s+',names=header)
    dfbed['CHR']=dfbed['CHR'].str.replace("chr","")
    dfmerge=pd.merge(dfoldgwas, dfbed, how='right', left_on=['rsids'], right_on=['SNP'])
    dfmerge=dfmerge[["CHR","BP_end","SNP","alt","ref","beta","pval","sebeta","af_alt","nearest_genes"]]
    dfmerge.set_axis(["CHR","BP","SNP","A1","A2","BETA","P","SE","AF","nearest_genes"], axis=1, inplace=True)
    dfmerge['SNP1']=dfmerge.CHR.astype(str) + ':' + dfmerge.BP.astype(str)
    dfmerge['SNP2'] = dfmerge.CHR.astype(str) + ':' + dfmerge.BP.astype(str)+":"+dfmerge.A2.astype(str)+":"+dfmerge.A1.astype(str)
    dfmerge=dfmerge[['CHR', 'BP', "SNP",'SNP1','SNP2','A1','A2','BETA','P','SE','AF','nearest_genes']]
    dfmerge.to_csv(outputfile_base + ".addsnp.txt.gz", sep='\t', index=False, compression="gzip")
    return


def take_input_2var():
    argv = sys.argv[1:]
    opts, args = getopt.getopt(argv, "i:b:")
    for opt, arg in opts:
        if opt in ['-i']:
            old_gwas_filename = arg
        elif opt in ['-b']:
            bedfilename=arg
    return old_gwas_filename,bedfilename

main()