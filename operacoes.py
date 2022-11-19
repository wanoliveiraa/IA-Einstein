from cromossomo import Cromossomo
import random
import numpy.random as npr

def mutacao(cromossomo):
    #Pegar primeiro uma casa aleatória
    numero_casa = random.randint(0,4)
    #Setar a característica que vai ser mudada de forma aleatória
    num_caracteristica = random.randint(0,4)
    pos_caracteristica = 0
    if (num_caracteristica == 0): #Mudar a nacionalidade
        print("MUTAR NACIONALIDADE: "+str(cromossomo.getNacionalidade()))
        mutaAlelo(cromossomo.getNacionalidade())
        print("DEPOIS: "+str(cromossomo.getNacionalidade()))
    elif(num_caracteristica==1):  #Mudar pet
        print("MUTAR PET: "+str(cromossomo.getPet()))
        mutaAlelo(cromossomo.getPet())
        print("DEPOIS: "+str(cromossomo.getPet()))
    elif(num_caracteristica==2): #Mudar cor
        print("MUTAR Cor: "+str(cromossomo.getCor()))
        mutaAlelo(cromossomo.getCor())
        print("DEPOIS: "+str(cromossomo.getCor()))
    elif(num_caracteristica ==3): #Mudar bebida
        print("MUTAR BEBIDA: "+str(cromossomo.getBebida()))
        mutaAlelo(cromossomo.getBebida())
        print("DEPOIS: "+str(cromossomo.getBebida()))
    elif(num_caracteristica==4): #Mudar cigarro
        print("MUTAR CIGARRO: "+str(cromossomo.getCigarro()))
        mutaAlelo(cromossomo.getCigarro())
        print("DEPOIS: "+str(cromossomo.getCigarro()))


def mutaAlelo(lista):
    pos_caracteristica = random.randint(0,4)
    chance = random.randint(0,100)
    if(pos_caracteristica == 0):
        swapSucessor(lista=lista, posicao=pos_caracteristica)
    elif(pos_caracteristica == 4):
        swapAntecessor(lista=lista, posicao=pos_caracteristica)
    else:
        if (chance <=50):
            swapAntecessor(lista=lista, posicao=pos_caracteristica)
        else:
            swapSucessor(lista=lista, posicao=pos_caracteristica)
        


def swapAntecessor(lista, posicao):
    aux = lista[posicao-1] 
    lista[posicao-1] = lista[posicao]
    lista[posicao] = aux 

def swapSucessor(lista, posicao):
    aux = lista[posicao+1] 
    lista[posicao+1] = lista[posicao]
    lista[posicao] = aux 


def roletaCromossomo(population):
    for c in population:
        if (c.getPontos() == 0):
            c.addConsolacao()
            
    max = sum([c.getPontos() for c in population])
    selection_probs = [c.getPontos()/max for c in population]
    for c in population:
        if (c.getPontos() == 0.5):
            c.removeConsolacao(0)

    return population[npr.choice(len(population), p=selection_probs)], selection_probs


