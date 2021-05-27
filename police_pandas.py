'''
https://data.world/awram/us-police-involved-fatalities
https://data.world/awram/us-police-involved-fatalities/workspace/file?filename=Police+Fatalities.csv
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
# Realiza a leitura do arquivo armazenando na variável df (dataframe)
df = pd.read_csv(r'C:\Users\Priscila\Documents\GitHub\teste\policefatal.csv')
# Cria um Backup do Data Frame original
df_backup = df.copy()
# Converte em maiúscula as strings da coluna "Armed"
df["Armed"].str.upper()

print('The columns of Data Frame are:\n',df.columns)
print(
    'This dataset aims to provide insight into individuals'
    ' who were killed during alteractions with police.'
    ' It includes information on their age, race,'
    ' mental health status, weapons they were armed with,'
    ' and if they were fleeing.'
)
print(
f'The first occurrence was in {df["Date"].min()}\n'
f'The last occurrence was in {df["Date"].max()}'
)
# Build a DataFrame with the columns "Race" and "Manner_of_death".
deaths_race = morte_raca = df[["Race", "Manner_of_death"]]

# Values aggreated by Race, Manner of death and both.
'''É PRECISO INCLUIR os 3.965 MORTOS QUE NÃO TIVEREAM A RAÇA CLASSIFICADA'''
        ''' Criar uma categoria RACE_WAS_NOT_DECLARED e atribuir 3965'''
race_not_declared = int(3965)
agg_by_race = deaths_race["Race"].value_counts()
agg_by_kind_of_death = deaths_race["Manner_of_death"].value_counts()
main_values_race_death = deaths_race.value_counts()

# Build the first graph, people that was killed by race.
agg_by_race.plot.bar(color="#dca800")
plt.xticks(rotation=0)  # Way to rotate the label of x and y axis.
plt.yticks(rotation=0)  # Way to rotate the label of x and y axis.
plt.ylabel("Number of deaths")
plt.title("People killed by police in USA, between 2001 and 2016")






# Clean the NaN values in the Race column.
morte_raca = morte_raca.dropna(subset=["Race"])


# Limpando o df de dados que não quero usar no momento. 
# DROP() - DELETA as colunas. "Name", "UID", "City", "Flee", "Mental_illness".
df = df.drop(columns=["Name", "UID", "City", "Flee", "Mental_illness"])

# White, Black, Hispanic
shot = np.array((3665, 2363, 1698))
tesered = np.array((123, 145, 61))
shot_and_tesered = np.array((58, 24, 20))
other = np.array((9, 4, 5))
races = ['White', 'Black', 'Hispanic']
plt.bar(races, shot, color = 'brown')
plt.bar(races, tesered, color = 'olive', bottom = shot)
plt.bar(races, shot_and_tesered, color = 'teal', bottom = shot + tesered)
plt.bar(races, other, color = 'royalblue', bottom = shot + tesered + shot_and_tesered)

plt.xlabel('Races')
plt.ylabel('Quantity')
plt.title('People killed by police in USA, between 2001 and 2016')
plt.legend(('Shot', 'Tesered', 'Shot and Tesered'))

plt.show()

# Grupo por raça. 
white = morte_raca[morte_raca["Race"] == "White"]
black = morte_raca[morte_raca["Race"] == "Black"]
hispanic = morte_raca[morte_raca["Race"] == "Hispanic"]
asian = morte_raca[morte_raca["Race"] == "Asian"]
nativo = morte_raca[morte_raca["Race"] == "Native"]
outro = morte_raca[morte_raca["Race"] == "Other"]

# Valores numéricos sobre a maneira da morte.
black_deaths = black.value_counts()
white_deaths = white.value_counts()
hispanic_deaths = hispanic.value_counts()
asian_deaths = asian.value_counts()
native_deaths = nativo.value_counts()
other_deaths = outro.value_counts()

# First Graphic - Tem que ser nessa ordem
morte_raca_numeros.plot(color='black', kind = 'bar')    
plt.title("Mortos pela polícia nos USA, entre 2001 e 2016")      # Define o título
plt.xlabel("Maneira da Morte por Raça")                   # Define o rótulo do eixo X
plt.ylabel("Quantidade de mortos")                      # Define o rótulo do eixo Y
plt.show()                                              # Mostra o gráfico

# VALUE_COUNTS() - Contar a incidência de elementos em uma coluna:
print(df["Manner_of_death"].value_counts())
print(df["Race"].value_counts())
print(df["Armed"].value_counts())
# normalize=True, retorna os dados em percentual.
morte_raca["Race"].value_counts(normalize=True)
# Build specific data frames. 
axe = df.loc[df["Armed"] == "AXE"]
baseball_bat = df.loc[df["Armed"] == "BASEBALL BAT"]
vehicle = df.loc[df["Armed"] == "VEHICLE"]
unknown_weapon = df.loc[df["Armed"] == "UNKNOWN WEAPON"]
toy_weapon = df.loc[df["Armed"] == "TOY WEAPON"]
knife = df.loc[df["Armed"] == "KNIFE"]
gun = df.loc[df["Armed"] == "GUN"]
unarmed = df.loc[df["Armed"] == "UNARMED"]

# Crianças mortas de 0 a 5 anos. 
criancas_0_ate_5 = df[df["Age"]<= 5]
# DF somente com os homens
homens = df[df["Gender"] == "Male"]
# DF somente com as mulheres
mulheres = df[df["Gender"] == "Female"]
