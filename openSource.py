# Open source library to scrap the details

from scholarly import scholarly
import pandas as pd

# List of Google Scholar IDs

faculty_ids = [
    'tuUO7DQAAAAJ',
    '-ZYIiGAAAAAJ',
    '5Dl7tEYAAAAJ',
    '2rePIXIAAAAJ',
    'jTCHV4kAAAAJ',
    '_bbxYHsAAAAJ',
    'bn6WQUoAAAAJ',
    'ThELNO0AAAAJ',
    'ryhyx4IAAAAJ',
    'prcv4fAAAAAJ',
    'eu_o414AAAAJ',
    'uZXv4XIAAAAJ',
    'Cf2I4OoAAAAJ',
    'Li0r8uMAAAAJ',
    'FlLJ1SYAAAAJ',
    'vjZ4yC0AAAAJ',
    'AIdTGncAAAAJ',
    'XPjU9AIAAAAJ',
    'Z34wmvMAAAAJ',
    'vGJxAzEAAAAJ',
    'hlTGb-0AAAAJ',
    'hC5psv4AAAAJ',
    'cE0jxPcAAAAJ',
    'IJvuo6cAAAAJ',
    'GYjXshwAAAAJ',
    'HKK_hlsAAAAJ',
    'qIFXtnYAAAAJ',
    'FmtW9kIAAAAJ',
    '_89sYcIAAAAJ',
    'qVkPhiAAAAAJ',
    'Hj3_OtwAAAAJ',
    'kNdafyoAAAAJ',
    'TIywHAYAAAAJ',
    'YzvzznoAAAAJ',
    'Mz8UAz8AAAAJ',
    '5DpheNgAAAAJ',
    'ORmwBEQAAAAJ',
    '6_DGZukAAAAJ',
    'BmSboYDhzK0C',
    'IkDN14UAAAAJ',
    'i4ZqOsMAAAAJ',
    '3pimobEAAAAJ',
    'xfJLs0UAAAAJ',
    'fYTPxK8AAAAJ',
    'Ac5HrokAAAAJ',
    '-M-lmeUAAAAJ'
]

all_faculty_data = pd.DataFrame()

for faculty_id in faculty_ids:
    author = scholarly.search_author_id(faculty_id)
    author = scholarly.fill(author)

    publications_data = []  # For storing publication data
    total_citations = 0

    for pub in author['publications']:
        pub_filled = scholarly.fill(pub)
        title = pub_filled['bib'].get('title', 'Title not available')
        pub_year = pub_filled['bib'].get('pub_year', 'Year not available')
        citations = pub_filled.get('num_citations', 0)
        total_citations += citations

        publications_data.append({
            'Title': title,
            'Year': pub_year,
            'Citations': citations
        })

    df = pd.DataFrame(publications_data)
    df['Author'] = author['name']
    df['Affiliation'] = author['affiliation']
    df['H-Index'] = author['hindex']
    df['i10-Index'] = author['i10index']
    df['Total Citations'] = total_citations


    all_faculty_data = pd.concat([all_faculty_data, df], ignore_index=True) # Concatenating

excel_filename = 'all_faculty_publications_data.xlsx'
all_faculty_data.to_excel(excel_filename, index=False)

print(f"Saved all faculty publication data to {excel_filename}")


# Single faculty

# author_id = 'bn6WQUoAAAAJ'
# author = scholarly.search_author_id(author_id)
# author = scholarly.fill(author)

# publications_data = []  # For storing publication data
# total_citations = 0

# for pub in author['publications']:  # Iterating over the author's publications
#     pub_filled = scholarly.fill(pub)
#     title = pub_filled['bib'].get('title', 'Title not available')
#     pub_year = pub_filled['bib'].get('pub_year', 'Year not available')
#     citations = pub_filled.get('num_citations', 0)
#     total_citations += citations

#     publications_data.append({
#         'Title': title,
#         'Year': pub_year,
#         'Citations': citations
#     })

# df = pd.DataFrame(publications_data)
# df['Author'] = author['name']
# df['Affiliation'] = author['affiliation']
# df['H-Index'] = author['hindex']
# df['i10-Index'] = author['i10index']
# df['Total Citations'] = total_citations

# excel_filename = 'publications_data6.xlsx'
# df.to_excel(excel_filename, index=False)

# print(f"Saved publication data to {excel_filename}")
