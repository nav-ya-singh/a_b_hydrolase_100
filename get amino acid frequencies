from __future__ import print_function
import sys
import os
from collections import Counter
from gemmi import cif, CifWalk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_file_paths_from_args():
    for arg in sys.argv[1:]:
        if os.path.isdir(arg):
            for path in CifWalk(arg):
                yield path
        else:
            print('input acceptable argument; needs to be a directory')


totals = Counter()
for path in get_file_paths_from_args():
    block = cif.read(path).sole_block()
    seq = block.find('_entity_poly_seq.', ['entity_id', 'mon_id'])
    entity_types = dict(block.find('_entity_poly.', ['entity_id', 'type']))
    aa_counter = Counter(row.str(1) for row in seq
                         if 'polypeptide' in entity_types[row.str(0)])
    totals += aa_counter
    f = 100.0 / sum(totals.values())
    df_percentages = pd.DataFrame(tuple((m, c*f) for (m, c) in totals.most_common(20)))
    x_p = df_percentages.iloc[:,0]
    y_p = df_percentages.iloc[:,1]
    # create graphs for percentages of amino acids
    plt.figure(figsize=(20,10))
    bp = sns.barplot(x_p,y_p)
    for i in bp.patches:
        bp.annotate(str(round(i.get_height(), 2)),xy=(i.get_x() + i.get_width()/2, i.get_height()),ha='center',va='bottom')
    plt.title(str(block.name) + ' amino acid percentages')
    plt.xlabel('amino acids')
    plt.ylabel('percentages')
    plt.show()
    # now for the number counts graphs
    df_frequency = pd.DataFrame(aa_counter.most_common())
    x_f = df_frequency.iloc[:,0]
    y_f = df_frequency.iloc[:,1]
    plt.figure(figsize=(20,10))
    bp_2 = sns.barplot(x_f,y_f)
    for j in bp_2.patches:
        bp_2.annotate(str(int(j.get_height())),xy=(j.get_x() + j.get_width()/2, j.get_height()),ha='center',va='bottom')
    plt.title(str(block.name) + ' amino acid frequencies')
    plt.xlabel('amino acids')
    plt.ylabel('frequency/counts')
    plt.show()
