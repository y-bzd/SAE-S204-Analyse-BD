# Récupérer les données, les transformer si nécessaire, puis afficher sous forme de tableau

dataCompagnie = requete_vers_dataframe(conn,
f"""SELECT PaysCompagnie,Count(idCompagnie) as nbCompagnie FROM {SCHEMA}.PLATEFORME
NATURAL JOIN {SCHEMA}.DATESORTIE
NATURAL JOIN {SCHEMA}.JEU
NATURAL JOIN {SCHEMA}.COMPAGNIEJEU
NATURAL JOIN {SCHEMA}.COMPAGNIE  
WHERE idplateforme = 15 and PaysCompagnie is not null and estDeveloppeur = 1
Group by PaysCompagnie
"""
)
liste1=\[\]  
for elt in [dataCompagnie["PAYSCOMPAGNIE"\]\[i] for i in range(len(dataCompagnie))]:
x=requete_vers_dataframe(conn,f"Select NomPays From PaysIso where Code_Numerique={elt}")
liste1.append(x["NOMPAYS"\]\[0])

# Affichage

liste2 = \[\[liste1[i],str(dataCompagnie["NBCOMPAGNIE"\]\[i])] for i in range (len(dataCompagnie))]

fig, ax = plt.subplots()
ax.axis('off')

table = ax.table(
cellText=liste2,
colLabels=["Pays", "Compagnie"],
cellLoc='center',
loc='center'
)

table.scale(1, 1.5)

#style pour l'entête
for col in range(2):
table[(0, col)].set_facecolor("mediumvioletred")
table[(0, col)].get_text().set_color("white")
table[(0, col)].get_text().set_fontweight("bold")

# remplit les doubles cellules en vert

for i in range(len(liste2)):
for j in range(2):
table[(i+1, j)].set_facecolor("lightgreen")

plt.title("Nombre de jeux par catégorie", pad=20, color="black")
[plt.show](http://plt.show)()