__version__ = "0.0.2"
import numpy as np

alf = 'abcdefghijklmnopqrstuvwxyvç ,ãé'
alfabeto_ident = np.identity(len(alf))


def para_one_hot(msg):
    l = list()
    for a in msg:
        i = alf.index(a)
        l.append(alfabeto_ident[i])
    l = np.array(l)
    return l.transpose()

def para_string(array):
    saida = ''
    array = array.transpose()

    for l in array:
        
        saida += alf[ np.where(l == 1)[0][0] ]
        
    return saida

def cifrar(msg, P):
    msg = para_one_hot(msg)
    saida = np.dot(P,msg)
    return para_string(saida)

def de_cifrar(msg,P):
    return para_string(np.dot(np.linalg.inv(P),para_one_hot(msg)))


def enigma_simples(msg,P,E):
    msg = para_one_hot(msg)
    m_ = E@P@msg
    return para_string(m_)

def de_nigma_simples(msg,P,E):
    msg = para_one_hot(msg)
    m_ = np.linalg.inv(P)@np.linalg.inv(E)@msg
    return para_string(m_)

def enigma(msg,P,E):
    n = len(msg)
    msg = para_one_hot(msg)
    cont = 0
    final = list()
    for i in range(n):
        c = E
        for _ in range(cont):
            c=c@E
        l = msg[:,i].transpose()
        arr = c@P@l
        final.append(arr)
        cont+=1

    return para_string(np.array(final).transpose())

def de_nigma(msg,P,E):
    n = len(msg)
    msg = para_one_hot(msg)
    cont=0
    saida = list()
    e_ = np.linalg.inv(E)
    p_ = np.linalg.inv(P)
    for i in range(n):
        c = e_
        for _ in range(cont):
            c=c@e_
        l = msg[:,i].transpose()
        arr = p_@c@l
        saida.append(arr)
        cont+=1
    
    return para_string(np.array(saida).transpose())