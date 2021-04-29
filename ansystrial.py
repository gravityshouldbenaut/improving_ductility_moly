import pandas as pd 

df = pd.read_csv("straintest.csv")

def getPerturbationsFromANSYSStrain():
    results = []
    for strain in df['Equivalent Elastic Strain (m/m)']:
        results.append(strain)

    return results

getPerturbationsFromANSYSStrain()