import csv

# Define the information about traits and SNPs
traits_snp_info = [
    # Snacking tendencies
    {'trait': 'Snacking tendencies', 'rsid': 'rs1234', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Increased snacking tendencies'},
    {'trait': 'Snacking tendencies', 'rsid': 'rs5678', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Decreased snacking tendencies'},
    {'trait': 'Snacking tendencies', 'rsid': 'rs679123', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Higher likelihood of snacking'},
    {'trait': 'Snacking tendencies', 'rsid': 'rs908765', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Reduced tendency to snack'},

    # Power-to-weight ratio
    {'trait': 'Power-to-weight ratio', 'rsid': 'rs91011', 'reference_allele': 'G', 'effect_allele': 'T',
     'impact': 'Higher power-to-weight ratio'},
    {'trait': 'Power-to-weight ratio', 'rsid': 'rs121314', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Lower power-to-weight ratio'},
    {'trait': 'Power-to-weight ratio', 'rsid': 'rs314159', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Improved muscle efficiency'},
    {'trait': 'Power-to-weight ratio', 'rsid': 'rs271828', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Reduced muscle power'},

    # Cholesterol
    {'trait': 'Cholesterol', 'rsid': 'rs161718', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Higher cholesterol levels'},
    {'trait': 'Cholesterol', 'rsid': 'rs192021', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lower cholesterol levels'},
    {'trait': 'Cholesterol', 'rsid': 'rs223344', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Increased LDL cholesterol'},
    {'trait': 'Cholesterol', 'rsid': 'rs556677', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Decreased HDL cholesterol'},

    # Caffeine consumption
    {'trait': 'Caffeine consumption', 'rsid': 'rs222324', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Higher caffeine consumption'},
    {'trait': 'Caffeine consumption', 'rsid': 'rs252627', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Lower caffeine consumption'},
    {'trait': 'Caffeine consumption', 'rsid': 'rs334455', 'reference_allele': 'G', 'effect_allele': 'T',
     'impact': 'Increased caffeine metabolism'},
    {'trait': 'Caffeine consumption', 'rsid': 'rs667788', 'reference_allele': 'C', 'effect_allele': 'A',
     'impact': 'Decreased sensitivity to caffeine'},
    {'trait': 'Caffeine consumption', 'rsid': 'rs2472297', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Higher caffeine consumption'},
    {'trait': 'Caffeine consumption', 'rsid': 'rs762551', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Faster caffeine metabolism'},

    # Cilantro/coriander preference
    {'trait': 'Cilantro/coriander preference', 'rsid': 'rs282930', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Cilantro aversion'},
    {'trait': 'Cilantro/coriander preference', 'rsid': 'rs313233', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Cilantro preference'},
    {'trait': 'Cilantro/coriander preference', 'rsid': 'rs343536', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Dislike of cilantro taste'},
    {'trait': 'Cilantro/coriander preference', 'rsid': 'rs373839', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Enjoyment of cilantro flavor'},
    {'trait': 'Cilantro preference', 'rsid': 'rs72921001', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Cilantro aversion'},

    # Magnesium levels
    {'trait': 'Magnesium levels', 'rsid': 'rs404142', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Higher magnesium levels'},
    {'trait': 'Magnesium levels', 'rsid': 'rs434445', 'reference_allele': 'G', 'effect_allele': 'T',
     'impact': 'Lower magnesium levels'},
    {'trait': 'Magnesium levels', 'rsid': 'rs454647', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Increased magnesium absorption'},
    {'trait': 'Magnesium levels', 'rsid': 'rs484950', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Decreased magnesium retention'},
    {'trait': 'Magnesium levels', 'rsid': 'rs11144134', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Higher serum magnesium'},

    # Vitamin B12 and folate
    {'trait': 'Vitamin B12 and folate', 'rsid': 'rs505152', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Higher vitamin B12 levels'},
    {'trait': 'Vitamin B12 and folate', 'rsid': 'rs535455', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Lower folate levels'},
    {'trait': 'Vitamin B12 and folate', 'rsid': 'rs565758', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Improved folate metabolism'},
    {'trait': 'Vitamin B12 and folate', 'rsid': 'rs595960', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Reduced vitamin B12 absorption'},
    {'trait': 'Vitamin B12 levels', 'rsid': 'rs602662', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lower serum vitamin B12'},
    {'trait': 'Folate levels', 'rsid': 'rs1801133', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Reduced folate levels'},

    # Lactose intolerance
    {'trait': 'Lactose intolerance', 'rsid': 'rs616263', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lactose intolerance'},
    {'trait': 'Lactose intolerance', 'rsid': 'rs646566', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Lactose tolerance'},
    {'trait': 'Lactose intolerance', 'rsid': 'rs676869', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Decreased lactase production'},
    {'trait': 'Lactose intolerance', 'rsid': 'rs707172', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Increased lactase persistence'},
    {'trait': 'Lactose intolerance', 'rsid': 'rs4988235', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lactose tolerance'},

    # Osteoporosis
    {'trait': 'Osteoporosis', 'rsid': 'rs737475', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Increased risk of osteoporosis'},
    {'trait': 'Osteoporosis', 'rsid': 'rs767778', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lower risk of osteoporosis'},
    {'trait': 'Osteoporosis', 'rsid': 'rs798081', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Reduced bone density'},
    {'trait': 'Osteoporosis', 'rsid': 'rs828384', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Enhanced bone strength'},
    {'trait': 'Osteoporosis', 'rsid': 'rs3736228', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Increased risk of osteoporosis'},

    # Sleep duration
    {'trait': 'Sleep duration', 'rsid': 'rs858687', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Short sleep duration'},
    {'trait': 'Sleep duration', 'rsid': 'rs888990', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Longer sleep duration'},
    {'trait': 'Sleep duration', 'rsid': 'rs919293', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Shortened sleep cycles'},
    {'trait': 'Sleep duration', 'rsid': 'rs949596', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Extended sleep periods'},
    {'trait': 'Sleep duration', 'rsid': 'rs5569', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Shorter sleep duration'},

    # Attention span
    {'trait': 'Attention span', 'rsid': 'rs979899', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Shorter attention span'},
    {'trait': 'Attention span', 'rsid': 'rs1010101', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Longer attention span'},
    {'trait': 'Attention span', 'rsid': 'rs103104', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Improved focus'},
    {'trait': 'Attention span', 'rsid': 'rs105106', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Reduced distractibility'},
    {'trait': 'Attention span', 'rsid': 'rs7171755', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Reduced attention span'},

    # Working memory
    {'trait': 'Working memory', 'rsid': 'rs107108', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Enhanced working memory'},
    {'trait': 'Working memory', 'rsid': 'rs109110', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Impaired working memory'},
    {'trait': 'Working memory', 'rsid': 'rs111112', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Better cognitive flexibility'},
    {'trait': 'Working memory', 'rsid': 'rs113114', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Poorer short-term memory'},
    {'trait': 'Working memory', 'rsid': 'rs4680', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Improved working memory'},

    # Glaucoma risk
    {'trait': 'Glaucoma risk', 'rsid': 'rs115116', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Increased risk of glaucoma'},
    {'trait': 'Glaucoma risk', 'rsid': 'rs117118', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Decreased risk of glaucoma'},
    {'trait': 'Glaucoma risk', 'rsid': 'rs119120', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Higher intraocular pressure'},
    {'trait': 'Glaucoma risk', 'rsid': 'rs121122', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Lower intraocular pressure'},
    {'trait': 'Glaucoma risk', 'rsid': 'rs10483727', 'reference_allele': 'T', 'effect_allele': 'C',
     'impact': 'Increased risk of glaucoma'},

    # Alcohol sensitivity
    {'trait': 'Alcohol sensitivity', 'rsid': 'rs123124', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Increased alcohol sensitivity'},
    {'trait': 'Alcohol sensitivity', 'rsid': 'rs125126', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Decreased alcohol sensitivity'},
    {'trait': 'Alcohol sensitivity', 'rsid': 'rs127128', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Higher alcohol tolerance'},
    {'trait': 'Alcohol sensitivity', 'rsid': 'rs129130', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Lower alcohol tolerance'},
    {'trait': 'Alcohol sensitivity', 'rsid': 'rs671', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Increased alcohol sensitivity'},

    # Pain sensitivity
    {'trait': 'Pain sensitivity', 'rsid': 'rs131132', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Higher pain sensitivity'},
    {'trait': 'Pain sensitivity', 'rsid': 'rs133134', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lower pain sensitivity'},
    {'trait': 'Pain sensitivity', 'rsid': 'rs135136', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Increased pain threshold'},
    {'trait': 'Pain sensitivity', 'rsid': 'rs137138', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Decreased pain threshold'},
    {'trait': 'Pain sensitivity', 'rsid': 'rs4680', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Decreased pain sensitivity'},

    # Testosterone levels
    {'trait': 'Testosterone levels', 'rsid': 'rs139140', 'reference_allele': 'C', 'effect_allele': 'T',
     'impact': 'Higher testosterone levels'},
    {'trait': 'Testosterone levels', 'rsid': 'rs141142', 'reference_allele': 'G', 'effect_allele': 'A',
     'impact': 'Lower testosterone levels'},
    {'trait': 'Testosterone levels', 'rsid': 'rs143144', 'reference_allele': 'A', 'effect_allele': 'C',
     'impact': 'Increased androgen production'},
    {'trait': 'Testosterone levels', 'rsid': 'rs145146', 'reference_allele': 'T', 'effect_allele': 'G',
     'impact': 'Decreased androgen production'},
    {'trait': 'Testosterone levels', 'rsid': 'rs5934505', 'reference_allele': 'A', 'effect_allele': 'G',
     'impact': 'Lower testosterone levels'}
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