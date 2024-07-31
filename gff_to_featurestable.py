import argparse


def convert_gff_to_feature_table(gff_file, output_file, transl_table):
    with open(gff_file, "r") as gff:
        with open(output_file, "w") as output:
            for line in gff:
                # Change this is you have accordingly if the format is not GFF3
                if not line.startswith("#"):
                    fields = line.strip().split("\t")
                    seqid = fields[0]
                    source = fields[1]
                    feature = fields[2]
                    start = fields[3]
                    end = fields[4]
                    score = fields[5]
                    strand = fields[6]
                    phase = fields[7]
                    attributes = fields[8]
                    # This is for GFF3 files from RAST. The attribute field may be in a different format
                    # Extract the product value from attributes
                    product_value = None
                    for attribute in attributes.split(";"):
                        if attribute.startswith("product="):
                            product_value = attribute.split("=")[1]
                            break

                    # Swap start and end if strand is negative
                    if strand == "-":
                        start, end = end, start

                    # Write the feature table entry
                    output.write(f"{start}\t{end}\t{feature}\n")
                    output.write(f"\t\t\tproduct\t{product_value}\n")
                    output.write(f"\t\t\ttransl_table\t{transl_table}\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert GFF file to feature table")
    parser.add_argument("gff_file", help="Path to the input GFF file")
    parser.add_argument("output_file", help="Path to the output feature table file")
    parser.add_argument("transl_table", help="Transl_table code", type=int)
    args = parser.parse_args()

    convert_gff_to_feature_table(args.gff_file, args.output_file, args.transl_table)
    # Usage: python3 /Users/pjoglekar/work/software/gff_to_featurestable.py <path_to_gff_file> <path_to_output_file> <transl_table_code>
