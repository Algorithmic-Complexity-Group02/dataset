import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

# Cargar los datos de animes y usuarios desde los archivos CSV
df_animes = pd.read_csv("animeTest.csv")
df_usuarios = pd.read_csv("profiles2.csv")


# Crear un grafo vacío
G = nx.Graph()  # Para un grafo no dirigido
# O bien
# G = nx.DiGraph()  # Para un grafo dirigido

# Agregar nodos de animes al grafo
for _, row in df_animes.iterrows():
    anime_uid = row["uid"]
    G.add_node(anime_uid, tipo="anime", data=row)

# Agregar nodos de usuarios al grafo
for _, row in df_usuarios.iterrows():
    user_profile = row["profile"]
    G.add_node(user_profile, tipo="usuario", data=row)

for _, row in df_usuarios.iterrows():
    user_profile = row["profile"]
    favorite_animes = row["favorites_anime"]
    
    for anime_uid in favorite_animes:
        G.add_edge(user_profile, anime_uid, tipo_interaccion="favorito")



# Crear un grafo de ejemplo (reemplaza esto con tu grafo real)
G = nx.Graph()
G.add_edge("Usuario1", "Anime1")
G.add_edge("Usuario1", "Anime2")
G.add_edge("Usuario2", "Anime2")
G.add_edge("Usuario3", "Anime3")

# Dibuja el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')

# Muestra el grafo en pantalla
plt.show()
# Crear un grafo de ejemplo (reemplaza esto con tu grafo real)
G = nx.Graph()
G.add_edge("Usuario1", "Anime1")
G.add_edge("Usuario1", "Anime2")
G.add_edge("Usuario2", "Anime2")
G.add_edge("Usuario3", "Anime3")

# Dibuja el grafo
pos = nx.spring_layout(G)  # Posición de los nodos
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black')

# Muestra el grafo en pantalla
plt.show()