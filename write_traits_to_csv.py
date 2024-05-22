import csv

# Define the information about traits and SNPs
traits_snp_info = [
    # Snacking tendencies
    {
        'trait': 'Snacking tendencies',
        'rsid': 'rs1234',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Increased snacking tendencies',
    },
    {
        'trait': 'Snacking tendencies',
        'rsid': 'rs5678',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Decreased snacking tendencies',
    },
    # Power-to-weight ratio
    {
        'trait': 'Power-to-weight ratio',
        'rsid': 'rs91011',
        'reference_allele': 'G',
        'effect_allele': 'T',
        'impact': 'Higher power-to-weight ratio',
    },
    {
        'trait': 'Power-to-weight ratio',
        'rsid': 'rs121314',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Lower power-to-weight ratio',
    },
    # Cholesterol
    {
        'trait': 'Cholesterol',
        'rsid': 'rs161718',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Higher cholesterol levels',
    },
    {
        'trait': 'Cholesterol',
        'rsid': 'rs192021',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Lower cholesterol levels',
    },
    # Caffeine consumption
    {
        'trait': 'Caffeine consumption',
        'rsid': 'rs222324',
        'reference_allele': 'T',
        'effect_allele': 'C',
        'impact': 'Higher caffeine consumption',
    },
    {
        'trait': 'Caffeine consumption',
        'rsid': 'rs252627',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Lower caffeine consumption',
    },
    # Cilantro/coriander preference
    {
        'trait': 'Cilantro/coriander preference',
        'rsid': 'rs282930',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Cilantro aversion',
    },
    {
        'trait': 'Cilantro/coriander preference',
        'rsid': 'rs313233',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Cilantro preference',
    },
    # Magnesium
    {
        'trait': 'Magnesium',
        'rsid': 'rs343536',
        'reference_allele': 'G',
        'effect_allele': 'T',
        'impact': 'Higher magnesium levels',
    },
    {
        'trait': 'Magnesium',
        'rsid': 'rs373839',
        'reference_allele': 'C',
        'effect_allele': 'A',
        'impact': 'Lower magnesium levels',
    },
    # Vitamin B12 and folate
    {
        'trait': 'Vitamin B12 and folate',
        'rsid': 'rs404142',
        'reference_allele': 'A',
        'effect_allele': 'C',
        'impact': 'Lower vitamin B12 and folate levels',
    },
    {
        'trait': 'Vitamin B12 and folate',
        'rsid': 'rs434445',
        'reference_allele': 'G',
        'effect_allele': 'T',
        'impact': 'Higher vitamin B12 and folate levels',
    },
    # Lactose intolerance
    {
        'trait': 'Lactose intolerance',
        'rsid': 'rs464748',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Lactose intolerance',
    },
    {
        'trait': 'Lactose intolerance',
        'rsid': 'rs495051',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Lactose tolerance',
    },
    # Osteoporosis
    {
        'trait': 'Osteoporosis',
        'rsid': 'rs525354',
        'reference_allele': 'A',
        'effect_allele': 'C',
        'impact': 'Increased risk of osteoporosis',
    },
    {
        'trait': 'Osteoporosis',
        'rsid': 'rs555657',
        'reference_allele': 'G',
        'effect_allele': 'T',
        'impact': 'Lower risk of osteoporosis',
    },
    # Sleep duration
    {
        'trait': 'Sleep duration',
        'rsid': 'rs585960',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Short sleep duration',
    },
    {
        'trait': 'Sleep duration',
        'rsid': 'rs616263',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Longer sleep duration',
    },
    # Attention span
    {
        'trait': 'Attention span',
        'rsid': 'rs646566',
        'reference_allele': 'A',
        'effect_allele': 'C',
        'impact': 'Shorter attention span',
    },
    {
        'trait': 'Attention span',
        'rsid': 'rs676869',
        'reference_allele': 'G',
        'effect_allele': 'T',
        'impact': 'Longer attention span',
    },
    # Working memory
    {
        'trait': 'Working memory',
        'rsid': 'rs707172',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Improved working memory',
    },
    {
        'trait': 'Working memory',
        'rsid': 'rs737475',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Reduced working memory',
    },
    # Glaucoma risk
    {
        'trait': 'Glaucoma risk',
        'rsid': 'rs767778',
        'reference_allele': 'T',
        'effect_allele': 'C',
        'impact': 'Increased risk of glaucoma',
    },
    {
        'trait': 'Glaucoma risk',
        'rsid': 'rs798081',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Decreased risk of glaucoma',
    },
    # Alcohol sensitivity
    {
        'trait': 'Alcohol sensitivity',
        'rsid': 'rs828384',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Increased alcohol sensitivity',
    },
    {
        'trait': 'Alcohol sensitivity',
        'rsid': 'rs858687',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Decreased alcohol sensitivity',
    },
    # Pain sensitivity
    {
        'trait': 'Pain sensitivity',
        'rsid': 'rs888990',
        'reference_allele': 'T',
        'effect_allele': 'C',
        'impact': 'Increased pain sensitivity',
    },
    {
        'trait': 'Pain sensitivity',
        'rsid': 'rs919293',
        'reference_allele': 'G',
        'effect_allele': 'A',
        'impact': 'Decreased pain sensitivity',
    },
    # Testosterone
    {
        'trait': 'Testosterone',
        'rsid': 'rs949596',
        'reference_allele': 'A',
        'effect_allele': 'G',
        'impact': 'Higher testosterone levels',
    },
    {
        'trait': 'Testosterone',
        'rsid': 'rs979899',
        'reference_allele': 'C',
        'effect_allele': 'T',
        'impact': 'Lower testosterone levels',
    },
]

# Define the file path for the CSV file
output_csv_file = 'traits_snp_info.csv'


# Write the information to the CSV file
def write_traits_snp_csv(file_path, traits_snp_info):
    # Define the header for the CSV file
    header = ['trait', 'rsid', 'reference_allele', 'effect_allele', 'impact']

    with open(file_path, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)

        # Write the header
        writer.writeheader()

        # Write the rows containing traits and SNPs information
        for info in traits_snp_info:
            writer.writerow(info)

    print(f'Traits and SNPs information has been written to {file_path}')


# Write the traits and SNPs information to the CSV file
write_traits_snp_csv(output_csv_file, traits_snp_info)