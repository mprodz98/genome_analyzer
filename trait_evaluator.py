import csv


def read_dna_file(file_path):
    """Read the raw DNA file and store SNP data in a dictionary."""
    snp_data = {}
    with open(file_path, 'r') as dna_file:
        reader = csv.reader(dna_file, delimiter='\t')
        for row in reader:
            # Skip the header line if present
            if row[0].startswith('#') or row[0] == 'rsid':
                continue
            rsid, chromosome, position, genotype = row
            snp_data[rsid] = genotype
    return snp_data


def load_traits_information(traits_file):
    """Load genetic markers and traits information from a file."""
    traits_info = {}
    with open(traits_file, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            trait, rsid, reference_allele, effect_allele, impact = row
            if trait not in traits_info:
                traits_info[trait] = []
            traits_info[trait].append((rsid, reference_allele, effect_allele, impact))
    return traits_info


def evaluate_traits(dna_data, traits_info):
    """Evaluate traits based on DNA data and traits information."""
    trait_evaluations = {}
    for trait, markers in traits_info.items():
        for rsid, reference_allele, effect_allele, impact in markers:
            # Check if the SNP is present in the DNA data
            if rsid in dna_data:
                genotype = dna_data[rsid]
                # Determine if the genotype matches the effect allele
                if effect_allele in genotype:
                    if trait not in trait_evaluations:
                        trait_evaluations[trait] = []
                    trait_evaluations[trait].append((rsid, effect_allele, impact))
    return trait_evaluations


def main():
    dna_file_path = "path_to_your_dna_file.txt"  # Provide the path to the DNA file
    traits_file_path = "path_to_your_traits_info_file.csv"  # Provide the path to the traits information file

    # Read the DNA file and load the SNP data
    dna_data = read_dna_file(dna_file_path)

    # Load the traits information
    traits_info = load_traits_information(traits_file_path)

    # Evaluate the traits
    trait_evaluations = evaluate_traits(dna_data, traits_info)

    # Display the results
    for trait, evaluations in trait_evaluations.items():
        print(f"Trait: {trait}")
        for rsid, effect_allele, impact in evaluations:
            print(f"  - rsid: {rsid}, Effect allele: {effect_allele}, Impact: {impact}")


if __name__ == '__main__':
    main()
