# gff_to_featurestable
NCBI accepts phage genome annotations through Bankit. Bankit requires the annotation data in features table format which can be annoying to make. gff_to_featurestable will help you convert gff files into NCBI features table format. Works on RAST an Pharokka annotations.

#Usage
python3 /path/to/gff_to_featurestable.py <path_to_gff_file> <path_to_output_file> <transl_table_code>
