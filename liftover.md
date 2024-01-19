ctrl+shift+v to preview in vs code.
# LiftOver: Convert Genome Build
grch38=hg38  
grch37=hg19  
grch36=hg18

All of the LiftOver files(executable,script, chain file) are in:  
/mnt/data_schen_1/yimei/software_and_tools/liftover/

## 1. LiftOver Plink binary files(fam,bed,bim)
Run LiftOverPlink.py   
Detailed guide see: https://github.com/sritchie73/liftOverPlink  

1. Most of our plink format files are in binary file set form(bed,fam,bim). The liftover script need ped,map file set. So you will need to convert it to ped,map files first:  
```
#activate the plink conda envrionemnt if you haven't done so
conda activate /mnt/data_schen_1/jingchun/miniconda3/envs/plink-env
#Run plink to convert the file
plink --bfile <bed/fam/bim file dir(just prefix)> --recode --out <output file dir(just prefix)>
#example:
#plink --bfile /mnt/data_schen_1/jingchun/dbgap_AI_project/dbGaP_dataset/AD_microglia_dbgap/phs000168_ADc1234/ad_c1234/preimputation/ad_c1234 --recode --out /path/to/output/ad_c1234
``` 
2. Run liftover python script(and rmbadlift if you need) in python2 otherwise it would return error:  
`python2 /mnt/data_schen_1/yimei/software_and_tools/liftover/liftOverPlink.py ...`
3. Convert the lifted file set back to binary file set after liftover:  
`plink --file <ped/map file dir(prefix)> --make-bed --out <out file` 





## 2. LiftOver with LiftOver executable
Reference: https://genome.sph.umich.edu/wiki/LiftOver
1. Convert the files need to be lifted to .bed file(Browser Extensible Data, not binary file format in plink).   
bed file:  
    - no header, contains 4 columns: chr, pos_start,pos_end,snpid.  
    - chr: "chr" + chromosome number(like chr1)  
    - pos_start: pos_end -1  
    - pos_end: the pos in the original file(like gwas file, the pos/bp column).   
    - snpid: usually will be rs id.  
    
    Reference script: convert_gwas_to_bedfile.py

2. Run liftover  
`/mnt/data_schen_1/yimei/software_and_tools/liftover/liftOver <input bed> <chain> <output bedfile name> <unlifted file name>`  
chain file: can be found in the liftover folder. It contain different contig between 2 genome build. There are multiple version for different genome build conversion. Chooose the right one for your conversion.

3. Merge lifted bed file to the old gwas file. Keep columns necessary for PRS or MR(chr, bp, rsid,snpid1,snpid2,a1,a2,beta/or,p,se,allele frequency)  
Reference script : lifted_bed_to_gwas.py

