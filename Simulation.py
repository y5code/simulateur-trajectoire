import numpy as np
import matplotlib.pyplot as plt
# 1 Paramètres physiques

g= 9.81  #Pesanteur ,m/s^2
m=0.045  #Masse du projectile ,kg
r= 0.021 #Rayon du projectile ,m
A= np.pi * r**2  #Surface frontale ,m^2
rho = 1.2 #Masse volumique de l'air ,kg/m^3
Cd= 0.47  #Coefficient de trainée ,sphère 

v0 =45.0 #Vitesse intiale ,m/s
alpha = 45.0 #Angle de tir , degrés
dt= 0.005 #Pas de temps très fin pour Euler , s

# 2 Fonction de résolution en direct , méthode d'Euler

def calculer_trajectoire(avec_frottement=True):
    x, y = [0.0], [0.0]
    vx = [V0 *np.cos(np.radians(alpha))]
    vy = [V0 * np.sin(np.radians(alpha))]
    
    # Constante de frottement k= 0.5 * rho * Cd * A
    k= 0.5 * rho * Cd * A if avec_frottement else 0.0

    while y[-1] >=0 :
        # vitesse instantanné v
        v= np.sqrt(vx[-1]**2 + vy[-1]**2)
    
        # Calcul des accéleration, PFD
        ax = - (k/m) * v * vx[-1]
        ay = -g - (k/m) * v *vy[-1]
    
        # Equations de la méthode d'euler
        x.append(x[-1] + vx[-1] *dt )
        y.append( y[-1] + vy[-1] *dt)
        vx.append( vx[-1] + ax * dt)
        vy.append(vy[-1] + ay*dt)

    return x[-1]  #rETOURNE LA PORTEE MAXIMALE 

# 3 Comparaison physique

x_vide, y_vide = calculer_trajectoire(avec_frottement=False)
x_air, y_air = calculer_trajectoire(avec_frottement=True)

print("--- Résultats du TP DE PHYSIQUE ---")
print(f"Portée théorique dans le vide : {porte_vide: .2f} mètres. ")
print(f"Portée réelle avec frottement dans l'air : {porte_air: .2f} mètres. ")
print(f"Perte de distance due à l'air : {porte_vide - porte_air: .2f} mètres. ")


plt.figure(figsize=(10, 5))
plt.plot(x_vide, y_vide , '--r' , label = "Trajectoire théorique (Vide/ Parabole)")
plt.plot(x_air, y_air  , '-b' , label = "Trajectoire réelle (avec frottement de l'air)")
plt.title("Influence de la résistance de l'air sur un projectile ")
plt.xlabel("Distance Horizontale  x en mètres ")
plt.ylabel("Altitude y en mètres")
plt.grid(True)

# Sauvegarde du TP

plt.savefig("trajectoire_ballistique.png")
print(" Graphique généré (Trajectoire_ballistique)")

plt.show()

