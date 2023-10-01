import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

df_animes = pd.read_csv("animeTest.csv")
df_usuarios = pd.read_csv("profileTest.csv")

nodos = {}
bordes = []

for _, row in df_animes.iterrows():
    anime_uid = row["uid"]
    nodos[anime_uid] = {"tipo": "anime", "data": row, "title": row["title"]}

for _, row in df_usuarios.iterrows():
    user_profile = row["profile"]
    nodos[user_profile] = {"tipo": "usuario", "data": row, "nombre_perfil": user_profile}

for _, row in df_usuarios.iterrows():
    user_profile = row["profile"]
    
    # Utilizar split para dividir la cadena y luego eliminar los corchetes y espacios
    favorite_animes_str = row["favorites_anime"]
    favorite_animes = [anime_id.strip(" '[]") for anime_id in favorite_animes_str.split(',')]

    for anime_uid in favorite_animes:
        if anime_uid:
            try:
                anime_uid = int(anime_uid)
                bordes.append((user_profile, anime_uid, {"tipo_interaccion": "favorito"}))
            except ValueError as e:
                print(f"Error al convertir a entero el valor '{anime_uid}' para el usuario {user_profile}: {e}")

G = {"nodos": nodos, "bordes": bordes}

print("Número de nodos:", len(G["nodos"]))
print("Número de bordes:", len(G["bordes"]))

print("Valores de los nodos:")
for node, data in G["nodos"].items():
    tipo = data.get('tipo', 'Desconocido')
    if tipo == 'anime':
        print(f"Anime: {node}, Título: {data.get('title', 'Desconocido')}")
    elif tipo == 'usuario':
        print(f"Usuario: {node}, Nombre de perfil: {data.get('nombre_perfil', 'Desconocido')}")

G_nx = nx.DiGraph()
G_nx.add_nodes_from(G["nodos"].items())
G_nx.add_edges_from(G["bordes"])

pos = nx.spring_layout(G_nx)
labels_anime = nx.get_node_attributes(G_nx, 'title')
labels_usuario = nx.get_node_attributes(G_nx, 'nombre_perfil')

colores_nodos = ['skyblue' if data.get('tipo', 'Desconocido') == 'anime' else 'orange' for node, data in G_nx.nodes(data=True)]

# nx.draw(G_nx, pos, with_labels=True, labels={**labels_anime, **labels_usuario},
#         node_size=500, node_color=colores_nodos, font_size=10, font_color='black')

# plt.show()

G = nx.Graph(G_nx)

pos= nx.spring_layout(G, k=0.5, iterations=1000)
_, ax = plt.subplots(figsize=(20, 20))

nx.draw_networkx(G, pos, with_labels=False, node_size=10, ax=ax, node_color=colores_nodos)
ax.axis('off')

plt.show()
