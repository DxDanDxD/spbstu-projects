import pandas as pd

'''dz nomer 1'''

f = pd.read_csv('./NISPUF17.csv', sep=',')
def proportion_of_education(dataframe):
    flen = len(f)
    lt12 = round(float(f['EDUC1'].where(f['EDUC1'] == 1).count() / flen), 2)
    e12 = round(float(f['EDUC1'].where(f['EDUC1'] == 2).count() / flen), 2)
    mt12 = round(float(f['EDUC1'].where(f['EDUC1'] == 3).count() / flen), 2)
    c = round(float(f['EDUC1'].where(f['EDUC1'] == 4).count() / flen), 2)
    a = {"Lesser than high school:": lt12,
            "Exactly in the high school:": e12,
            "Higher than the high school:": mt12,
            "In the college:": c}
    print(a)
proportion_of_education(f)

'''dz nomer 2'''

f = pd.read_csv('./NISPUF17.csv', sep=',')
f = f.dropna(subset=['P_NUMFLU'])
a = f.groupby('CBF_01')['P_NUMFLU'].mean()
print(round(float(a[1]), 1), round(float(a[2]), 1))

'''dz nomer 3'''

file = 'NISPUF17.csv'
def chickenpox_by_sex(a):
    f = pd.read_csv(a, sep=',')
    print(f['HAD_CPOX'].unique())
chickenpox_by_sex(file)
