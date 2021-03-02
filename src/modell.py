import math
import numpy as np
import cv2

class coronaSIR:
    pop = 1 #Verdens populasjon
    Y = 0.1 #Hvor lang tid det tar før en passient bblir frisk
    deltaT = 1
    
    def __init__(self, posisjon, sted_populasjon, beta):
        self.posisjon = posisjon #Område navn. 
        self.pop = sted_populasjon #Populasjonen til det område
        self.beta = beta #Beta verdien er hvor ofte folk omgås i det område
        self.suseptible = [sted_populasjon] #Hvor mange som er "Suseptible" i område
        self.infected = [0] #Hvor mange som er "infected" i område
        #self.recoverd = [0] #Hvor mange som har "recoverd" i område
        
    def ny_S(self): #Sette ny verdi til "suseptible"
        self.suseptible.append(self.suseptible[-1] + 
            ((-self.beta*self.suseptible[-1]*self.infected[-1])/self.pop))
            #Funksjonen for å finne ut ny S: S - (B * S * I)/Pop
        
    def ny_I(self): #Sette ny verdie til "infected"
        self.infected.append(self.infected[-1] + 
            (self.beta*self.suseptible[-2]*self.infected[-1])/self.pop)
            #- Y*self.infected[-1]))
            #Funksjon for å finne ut ny I: I + (B * S * I)/Pop - (Y * I)
    
    #def ny_R(self): #Sette ny verdi til "recoverd"
        #self.recoverd.append(self.recoverd[-1] + (Y*self.infected[-2]))
            #Funksjon for å finne ut ny R: R + (Y * I)
            