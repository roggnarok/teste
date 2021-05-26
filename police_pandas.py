'''
https://data.world/awram/us-police-involved-fatalities
https://data.world/awram/us-police-involved-fatalities/workspace/file?filename=Police+Fatalities.csv
'''
import pandas as pd
import matplotlib as plt
# Realiza a leitura do arquivo armazenando na variável df (dataframe)
df = pd.read_csv(r'Desktop\py_programas\testes\policefatal.csv')
# Cria um Backup do Data Frame original
df_backup = df.copy()
# Converte em maiúscula as strings da coluna "Armed"
df = df["Armed"].str.upper()

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
# Limpando o df de dados que não quero usar no momento. 
# DROP() - DELETA as colunas. "Name", "UID", "City", "Flee", "Mental_illness".
df = df.drop(columns=["Name", "UID", "City", "Flee", "Mental_illness"])
# Cria um DF somente com as colunas "Race" e "Manner_of_death".
morte_raca = df[["Race", "Manner_of_death"]]

# Grupo por raça. 
white = morte_raca[morte_raca["Race"] == "White"]
black = morte_raca[morte_raca["Race"] == "Black"]
hispanic = morte_raca[morte_raca["Race"] == "Hispanic"]
asian = morte_raca[morte_raca["Race"] == "Asian"]
nativo = morte_raca[morte_raca["Race"] == "Native"]
outro = morte_raca[morte_raca["Race"] == "Other"]

# Valores numéricos sobre a maneira da morte.
morte_raca_numeros = morte_raca.value_counts()
black_mortes = black.value_counts()
white_mortes = white.value_counts()
hispanic_mortes = hispanic.value_counts()
asian_mortes = asian.value_counts()
nativo_mortes = nativo.value_counts()
outro_mortes = outro.value_counts()

# First Graphic
morte_raca_numeros.plot(x = 'Maneira da morte', y = 'Quantidade', kind = 'bar')
plt.show

# VALUE_COUNTS() - Contar a incidência de elementos em uma coluna:
print(df["Manner_of_death"].value_counts())
print(df["Race"].value_counts())
print(df["Armed"].value_counts())
# normalize=True, retorna os dados em percentual.
morte_raca["Race"].value_counts(normalize=True)
# Cria data frames específicos.
Axe = df.loc[df["Armed"] == "AXE"]
Baseball_Bat = df.loc[df["Armed"] == "BASEBALL BAT"]
Vehicle = df.loc[df["Armed"] == "VEHICLE"]
Unknown_Weapon = df.loc[df["Armed"] == "UNKNOWN WEAPON"]
Toy_Weapon = df.loc[df["Armed"] == "TOY WEAPON"]
facas = df.loc[df["Armed"] == "KNIFE"]
Gun = df.loc[df["Armed"] == "GUN"]
Unarmed = df.loc[df["Armed"] == "UNARMED"]

# Crianças mortas de 0 a 5 anos. 
criancas_0_ate_5 = df[df["Age"]<= 5]
# DF somente com os homens
homens = df[df["Gender"] == "Male"]
# DF somente com as mulheres
mulheres = df[df["Gender"] == "Female"]
