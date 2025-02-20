import sys
import json
import requests
from prettytable import PrettyTable

#Documentation: https://www.uniprot.org/help/api
WEBSITE_API = "https://rest.uniprot.org/"

def get_aaseq(gene):
  r = requests.get(f'{WEBSITE_API}/uniprotkb/stream?query={gene} AND (taxonomy_id:2)&format=fasta')
  with open(f"{gene}.fasta", "w") as arquivo:
      arquivo.write(r.text)


gene_list = ['CpsK', 'Alpha-2,3-N-acetylneuraminyltransferase', 'KpsM', 'KpsT',
             'KpsC', 'KpsD', 'KpsE', 'KpsF', 'KpsS', 'Lic3A', 'Lic3B', 'NeuS',
             'N-acylneuraminate cytidylyltransferase', 'NeuB', 'NeuC', 'NeuD',
             'NeuE', 'NeuO', 'CMP-N-acetylneuraminate-beta-galactosamide-alpha-2,3-sialyltransferase',
             'NagA', 'NagB', 'N-acetylneuraminate-lyase', 'Putative N-acetylmannosamine-6-phosphate-2-epimerase'
             'nanK', 'nanQ', 'N-acylglucosamine-2-epimerase', 'NanU', 'NanO','NanC','NanT', 'NanM', 'OmpC',
             'OmpF', 'SatA', 'SatB', 'SatC', 'SatD', 'SiaP',
             'SiaQ', 'SiaT', 'SiaM', 'Sialate O-acetylesterase', 'nagZ', 'NanH',
             'NanB', 'NanR']

for i in gene_list:
  get_aaseq(i)

