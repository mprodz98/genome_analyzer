import csv
from argparse import ArgumentParser


def read_dna_file(file_path: str) -> dict:
    """Read the raw DNA file and store SNP data in a dictionary."""
    snp_data = {}
    with open(file_path, 'r') as dna_file:
        reader = csv.reader(dna_file, delimiter='\t')
        for row in reader:
            # Skip the header line if present
            if row[0].startswith('#') or row[0] == 'rsid':
                continue
            rsid, chromosome, position, allele1, allele2 = row
            genotype = allele1 + allele2
            snp_data[rsid] = genotype
    return snp_data


def load_traits_information(traits_file: str) -> dict:
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


def evaluate_traits(dna_data: dict, traits_info: dict):
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


def estimate_height(rsid_data, rsid_effects):
    """
    Estimate height based on RSID data.

    Parameters:
    - rsid_data (dict): A dictionary where keys are RSIDs and values are genotypes.
    - rsid_effects (dict): A dictionary where keys are RSIDs and values are effects (positive for increase, negative for decrease).

    Returns:
    - Estimated height in cm.
    """

    base_height = 170  # Base height in cm (average height, can be adjusted)
    height_adjustment = 0

    for rsid, effect_allele, impact in rsid_data:
        if rsid in rsid_effects:
            effect = rsid_effects[rsid]
            height_adjustment += effect

    estimated_height = base_height + height_adjustment
    return estimated_height


def main():
    parser = ArgumentParser()
    parser.add_argument('--dna_file_path', default='AncestryDNA.txt')
    args = parser.parse_args()
    dna_file_path: str = args.dna_file_path
    traits_file_path = "traits_snp_info.csv"  # Provide the path to the traits information file

    # Read the DNA file and load the SNP data
    dna_data = read_dna_file(dna_file_path)

    # Load the traits information
    traits_info = load_traits_information(traits_file_path)

    # Evaluate the traits
    trait_evaluations = evaluate_traits(dna_data, traits_info)
    print(trait_evaluations['Height'])

    # Display the results
    for trait, evaluations in trait_evaluations.items():
        print(f"Trait: {trait}")
        for rsid, effect_allele, impact in evaluations:
            print(f"  - rsid: {rsid}, Effect allele: {effect_allele}, Impact: {impact}")

    height_effects = {
        'rs1042713': 1.5,  # Increased height
        'rs1862513': -1.2,  # Decreased height
        'rs4975605': 2.0,  # Increased height
        'rs1455680': -1.8,  # Decreased height
        'rs11603041': 1.7,  # Increased height
        'rs671': -1.5,  # Decreased height
        'rs2043644': 1.6,  # Increased height
        'rs947083': -1.4,  # Decreased height
        'rs1562101': 1.8,  # Increased height
        'rs7310409': -1.3,  # Decreased height
        'rs2908301': 1.4,  # Increased height
        'rs7733878': -1.2,  # Decreased height
        'rs1483856': 1.5,  # Increased height
        'rs7465337': -1.6,  # Decreased height
        'rs2155242': 1.7,  # Increased height
        'rs559217': -1.1,  # Decreased height
        'rs7968219': 1.9,  # Increased height
        'rs6580954': -1.5,  # Decreased height
        'rs11645825': 1.6,  # Increased height
        'rs11895655': -1.4,  # Decreased height
        'rs7632341': 1.5,  # Increased height
        'rs1552638': -1.2,  # Decreased height
        'rs2289694': 1.7,  # Increased height
        'rs6804177': -1.3,  # Decreased height
        'rs6735163': 1.8,  # Increased height
        'rs1860236': -1.5,  # Decreased height
        'rs2170071': 1.6,  # Increased height
        'rs8100407': -1.2,  # Decreased height
        'rs6825241': 1.4,  # Increased height
        'rs1980626': -1.1,  # Decreased height
        'rs1390950': 1.7,  # Increased height
        'rs7102701': -1.4,  # Decreased height
        'rs13289382': 1.5,  # Increased height
        'rs1390508': -1.2,  # Decreased height
        'rs11120016': 1.6,  # Increased height
        'rs1995584': -1.3,  # Decreased height
        'rs1570885': 1.8,  # Increased height
        'rs1149944': -1.1  # Decreased height
    }


    print(estimate_height(trait_evaluations["Height"], height_effects))

if __name__ == '__main__':
    main()
