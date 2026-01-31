import neat
import os
from main import game

# -----------------------------------------
# FONCTION D'ÉVALUATION DES GÉNOMES
# -----------------------------------------
def eval_genomes(genomes, config, game_instance):
    # genomes -> LISTE de tuple qui contient le génome et l'id du génome (genome_id)
    # un génome ->  un réseau de nerones qui va évaluer 

    #On parcourt chaque génome du tuple 
    for genome_id, genome in genomes:

# Cette ligne crée un "raisonnement" ou un réseau de neurones EXÉCUTABLE.
# On prend en argument le génome actuel (plan du réseau) et la configuration (config)
# pour construire un réseau concret en mémoire qui contient :
#   - les neurones avec leur bias et fonctions d'activation
#   - les connexions avec leurs poids
#   - la structure exacte selon le génome (entrées, sorties, éventuels neurones cachés)
# Le résultat est un objet 'net' qui peut être utilisé pour calculer des sorties à partir d'entrées.
# Cet objet possède la méthode net.activate(inputs) qui permet d'envoyer des données dans le réseau
# et de récupérer la réponse (output) du réseau.

# config = réglages de fabrication : définit les règles pour créer le réseau, 
# fonctions d'activation, nombre de neurones, feed-forward ou recurrent, etc.
        net = neat.nn.FeedForwardNetwork.create(genome, config)

        genome.fitness = 0.0

        #inputs = ##on veux acceder au donné sur le joueur sans passer par Game juste par le joueur
        #On calcule la sortie à partir des entrées
        output = net.activate(())

        if output[0] > 0.5:
            genome.fitness += 1

#On définit le chemin du config
local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, "config-neat.txt")


#On crée la configuration neat
config = neat.Config(
    neat.DefaultGenome,
    neat.DefaultReproduction,
    neat.DefaultSpeciesSet,
    neat.DefaultStagnation,
    config_path
)

#On crée une population avec des génomes au hasard
p = neat.Population(config)

# -----------------------------------------
# LANCEMENT DE L'ENTRAÎNEMENT
# -----------------------------------------
# NEAT va exécuter la fonction eval_genomes sur chaque génération
# Ici on fait 5 générations
winner = p.run(eval_genomes, 5)

print("Terminé")