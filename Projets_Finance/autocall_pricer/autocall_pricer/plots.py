import matplotlib.pyplot as plt
import numpy as np

def plot_paths(paths, n=50, S0=100, barriere_rappel=1.0):

    plt.figure(figsize=(10, 6))
    # On définit le niveau de prix qui déclenche le remboursement (ex: 100)
    niveau_seuil = S0 * barriere_rappel
    
    # On limite le tracé à n trajectoires (pour ne pas surcharger le graphique)
    nombre_a_tracer = min(n, len(paths))
    
    for i in range(nombre_a_tracer):
        trajectoire_actuelle = paths[i]
        
        # On cherche les moments où l'indice dépasse le seuil
        # On ignore l'index 0 (le départ) pour ne pas s'arrêter à t=0
        indices_depassement = np.where(trajectoire_actuelle[1:] >= niveau_seuil)[0] # 1: veut dire qu'on commence à chercher à partir de t=1
        
        if len(indices_depassement) > 0:
            # CAS OU LE PRODUIT EST RAPPELÉ AVANT LA MATURITÉ 
            
            # On récupère l'index du tout premier dépassement
            premier_index_trouve = indices_depassement[0]
            
            # On ajuste l'index car on a commencé à chercher à partir de t=1 (+1)
            # Et on veut inclure ce point dans le tracé (+1), donc total +2
            index_arret_visuel = premier_index_trouve + 2
            
            # On découpe la trajectoire pour qu'elle s'arrête net au rappel
            partie_vivante = trajectoire_actuelle[:index_arret_visuel]
            
            # On trace cette ligne (alpha 0.6 = légèrement transparent)
            plt.plot(partie_vivante, alpha=0.6)
            
            # On place un petit point rose au moment précis du rappel
            temps_rappel = index_arret_visuel - 1
            prix_rappel = trajectoire_actuelle[temps_rappel]
            plt.scatter(temps_rappel, prix_rappel, color='pink', s=10, zorder=5)
            
        else:
            # CAS OU LE PRODUIT VA JUSQU'AU BOUT  ET L'INDICE N'A JAMAIS DÉPASSÉ LE SEUIL
            
            # L'indice est resté sous la barrière pendant 6 ans
            plt.plot(trajectoire_actuelle, alpha=0.3)
            
    # Ajout d'une ligne horizontale violette pour le seuil de rappel
    plt.axhline(niveau_seuil, color='violet', linestyle='--', label='Seuil Rappel (100%)')
    
    # Mise en forme du graphique
    plt.title("Trajectoires Monte-Carlo (Arrêtées au rappel)")
    plt.xlabel("Années")
    plt.ylabel("Indice ( en % de S0) ")
    plt.legend()
    plt.grid(True, alpha=0.3)
    
    # Affichage final
    plt.show()