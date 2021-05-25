'''
https://data.world/awram/us-police-involved-fatalities
https://data.world/awram/us-police-involved-fatalities/workspace/file?filename=Police+Fatalities.csv
'''
import pandas as pd
import matplotlib as plt
# Realiza a leitura do arquivo armazenando na variável df (dataframe)
df = pd.read_csv(r'C:\Users\Priscila\Desktop\py_programas\testes\policefatal.csv')

print('As colunas do df são:\n',df.columns)
print(
    '\nEste projeto visa entender a maineira mais recorrrente de morte por raça.\n'
)
print(
    'This dataset aims to provide insight into individuals'
    ' who were killed during alteractions with police.'
    ' It includes information on their age, race,'
    ' mental health status, weapons they were armed with,'
    ' and if they were fleeing.'
)
print(
f'A primeira ocorrência foi em {df["Date"].min()}\n'
f'A última ocorrência foi em {df["Date"].max()}'
)
# Cria um Backup do Data Frame original
df_backup = df.copy()
# DELETA as colunas "Name", "UID", "City", "Flee", "Mental_illness".
df = df.drop(columns=["Name", "UID", "City", "Flee", "Mental_illness"])

# Cria data frames específicos.
Axe = df.loc[df["Armed"] == "Axe"]
Baseball_Bat = df.loc[df["Armed"] == "Baseball Bat"]
Vehicle = df.loc[df["Armed"] == "Vehicle"]
Unknown_Weapon = df.loc[df["Armed"] == "Unknown Weapon"]
Toy_Weapon = df.loc[df["Armed"] == "Toy weapon"]
Toy_Weapon2 = df.loc[df["Armed"] == "Toy Weapon"]
facas = df.loc[df["Armed"] == "Knife"]
Gun = df.loc[df["Armed"] == "Gun"]
Unarmed = df.loc[df["Armed"] == "Unarmed"]


# Crianças mortas de 0 a 5 anos. 
criancas_0_ate_5 = df[df["Age"]<= 5]
# DF somente com os homens
homens = df[df["Gender"] == "Male"]
# DF somente com as mulheres
mulheres = df[df["Gender"] == "Female"]

