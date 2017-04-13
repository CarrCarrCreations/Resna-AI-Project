__author__ = 'rsimpson'

import random
from geneticAlgorithm import *
import Workshop_platform as Wp

class ResnaBlockGene(Gene):
    '''
    Each gene represents a state (e.g., the platform and workshop in each block of the resna conference ).
    The value of each state includes the 4 papers and 5 workshops
    '''
    def __init__(self, _name):
        # call the parent constructor
        Gene.__init__(self)
        # choose a random value to start
        self.randomInit()
        # keep track of which state in Australia this gene represents
        self.name = _name

    def printGene(self):
        print "**********************************"
        print "name = " + self.name
        print "Platform"
        print "Paper 1" + self.P1Value['n'] + self.P1Value['t'] + self.P1Value['p']
        print "Paper 2" + self.P2Value['n'] + self.P2Value['t'] + self.P2Value['p']
        print "Paper 3" + self.P3Value['n'] + self.P3Value['t'] + self.P3Value['p']
        print "Paper 4" + self.P4Value['n'] + self.P4Value['t'] + self.P4Value['p']
        print "WorkShop 1" + self.W1Value['n'] + self.W1Value['t'] + self.W1Value['p']
        print "WorkShop 2" + self.W2Value['n'] + self.W2Value['t'] + self.W2Value['p']
        print "WorkShop 3" + self.W3Value['n'] + self.W3Value['t'] + self.W3Value['p']
        print "WorkShop 4" + self.W4Value['n'] + self.W4Value['t'] + self.W4Value['p']
        print "WorkShop 5" + self.W5Value['n'] + self.W5Value['t'] + self.W5Value['p']
        print "**********************************"

    def randomInit(self):
        global GRIDSIZE
        # P1 - P4 stand for the 4 papers that are in a platform
        # W1 - W5 stand for the 5 workshops in the block
        # each list is a list of dictionaries of all possible papers or workshops
        self.P1Value = random.choice(Wp.paperLst)
        self.P2Value = random.choice(Wp.paperLst)
        self.P3Value = random.choice(Wp.paperLst)
        self.P4Value = random.choice(Wp.paperLst)
        self.W1Value = random.choice(Wp.workShopLst)
        self.W2Value = random.choice(Wp.workShopLst)
        self.W3Value = random.choice(Wp.workShopLst)
        self.W4Value = random.choice(Wp.workShopLst)
        self.W5Value = random.choice(Wp.workShopLst)


class ResnaChromosome(Chromosome):
    '''
    A chromosome platform and 5 workshops for each state. The chromosome stores a list of gene objects in
    self.genes
    '''
    def __init__(self, length):
        # call the parent constructor
        Chromosome.__init__(self, length)
        # choose random values for the chromosome
        self.randomInit()
        # initialize fitness score
        self.fitness = self.fitnessFunction()

    def randomInit(self):
        """
        choose random values for the chromosome
        """
        # create a list of state names
        states = ['Block One', 'Block Two', 'Block Three', 'Block Four', 'Block Five',
                  'Block Six', 'Block Seven', 'Block Eight', 'Block Nine']
        # for each position in the chromosome (i.e., each block of the conference)...
        for state in range(0, self.length):
            # create a new gene
            newGene = ResnaBlockGene(states[state])
            # add the gene to the chromosome
            self.genes.append(newGene)

    def BlockLogicPaperP(self, chrome):
        # p1p means paper 1 presentor, and so on
        p1p = chrome.P1Value['p']
        p2p = chrome.P2Value['p']
        p3p = chrome.P3Value['p']
        p4p = chrome.P4Value['p']
        fitness = 0
        # if p1p presentor is in the list of paper 2 presentor, add 1 to the fitness because they need
        # to be different people. continues these checks for each unique combination
        for name in p1p:
            for names in p2p:
                if name in names:
                    fitness += 1
        for name in p1p:
            for names in p3p:
                if name in names:
                    fitness += 1
        for name in p1p:
            for names in p4p:
                if name in names:
                    fitness += 1
        for name in p2p:
            for names in p3p:
                if name in names:
                    fitness += 1
        for name in p2p:
            for names in p4p:
                if name in names:
                    fitness += 1
        for name in p3p:
            for names in p4p:
                if name in names:
                    fitness += 1
        return fitness

    def BlockLogicPaperT(self, chrome):
        # p1t means paper 1 topic, and so on
        p1t = chrome.P1Value['t']
        p2t = chrome.P2Value['t']
        p3t = chrome.P3Value['t']
        p4t = chrome.P4Value['t']
        fitness = 0
         # if the topic of paper 1 is not the topic of the rest, add 1 to the fitness
        for topic in p1t:
            for topics in p2t:
                if topic not in topics:
                    fitness += 1
        for topic in p1t:
            for topics in p3t:
                if topic not in topics:
                    fitness += 1
        for topic in p1t:
            for topics in p4t:
                if topic not in topics:
                    fitness += 1
        return fitness


    def BlockLogicWorkShopP(self, chrome):
        # this checks the fitness of the workshop presentors. Since the same person
        # cannot present in multiple workshops in the same block, +1 is added to the
        #fitness if it is the same person
        w1p = chrome.W1Value['p']
        w2p = chrome.W2Value['p']
        w3p = chrome.W3Value['p']
        w4p = chrome.W4Value['p']
        w5p = chrome.W5Value['p']
        fitness = 0

        for name in w1p:
            for names in w2p:
                if name in names:
                    fitness += 1
        for name in w1p:
            for names in w3p:
                if name in names:
                    fitness += 1
        for name in w1p:
            for names in w4p:
                if name in names:
                    fitness += 1
        for name in w1p:
            for names in w5p:
                if name in names:
                    fitness += 1
        for name in w2p:
            for names in w3p:
                if name in names:
                    fitness += 1
        for name in w2p:
            for names in w4p:
                if name in names:
                    fitness += 1
        for name in w2p:
            for names in w5p:
                if name in names:
                    fitness += 1
        for name in w3p:
            for names in w4p:
                if name in names:
                    fitness += 1
        for name in w3p:
            for names in w5p:
                if name in names:
                    fitness += 1
        for name in w4p:
            for names in w5p:
                if name in names:
                    fitness += 1
        return fitness

    def BlockLogicWorkShopT(self, chrome):
        # each workshop has to be a different topic, so if a workshop has the same topic
        # +1 is added to the fitness score
        w1t = chrome.W1Value['t']
        w2t = chrome.W2Value['t']
        w3t = chrome.W3Value['t']
        w4t = chrome.W4Value['t']
        w5t = chrome.W5Value['t']
        fitness = 0

        for topic in w1t:
            for topics in w4t:
                if topic in topics:
                    fitness += 1
        for topic in w1t:
            for topics in w5t:
                if topic in topics:
                    fitness += 1
        for topic in w2t:
            for topics in w3t:
                if topic in topics:
                    fitness += 1
        for topic in w2t:
            for topics in w4t:
                if topic in topics:
                    fitness += 1
        for topic in w2t:
            for topics in w5t:
                if topic in topics:
                    fitness += 1
        for topic in w3t:
            for topics in w4t:
                if topic in topics:
                    fitness += 1
        for topic in w3t:
            for topics in w5t:
                if topic in topics:
                    fitness += 1
        for topic in w4t:
            for topics in w5t:
                if topic in topics:
                    fitness += 1
        return fitness

    def BlockLogicP_and_WS(self, chrome):
        fitness = 0
        w1p = chrome.W1Value['p']
        w2p = chrome.W2Value['p']
        w3p = chrome.W3Value['p']
        w4p = chrome.W4Value['p']
        w5p = chrome.W5Value['p']
        Ws_List = [w1p, w2p, w3p, w4p, w5p]
        p1p = chrome.P1Value['p']
        p2p = chrome.P2Value['p']
        p3p = chrome.P3Value['p']
        p4p = chrome.P4Value['p']
        P_List = [p1p, p2p, p3p, p4p]

        # for the presentor in the paper list
        for i in P_List:
            # for the presentor in the workshop list
            for j in Ws_List:
                # if paper presentor in workshop presentor
                if i in j:
                    # add 1 to the fitness score
                    fitness += 1
        return fitness


    def fitnessFunction(self):
        """
        Calculate the 'fitness' of each chromosome, which represents how
        close the chromosome is to a valid solution
        """
        # start accumulator at zero
        fitness = 0
        """
        perform a fitness test on each block. This tests weather the papers have the same presentors,
        papers have the same topic, if each platform paper and workshop have different presentors, and
        if all the workshops have different topics
        """
        ChromosomeList = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        for chromosome in ChromosomeList:
            gene = self.genes[chromosome]
            fitness += self.BlockLogicPaperP(gene)
        for chromosome in ChromosomeList:
            gene = self.genes[chromosome]
            fitness += self.BlockLogicPaperT(gene)
        for chromosome in ChromosomeList:
            gene = self.genes[chromosome]
            fitness += self.BlockLogicWorkShopP(gene)
        for chromosome in ChromosomeList:
            gene = self.genes[chromosome]
            fitness += self.BlockLogicWorkShopT(gene)
        for chromosome in ChromosomeList:
            gene = self.genes[chromosome]
            fitness += self.BlockLogicP_and_WS(gene)

        # constraint list for grouping topics in consective blocks for the objective function(still to be made)
        constraintList = [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8)]
        print fitness
        return fitness



class ResnaPopulation(Population):
    def __init__(self, populationSize, chromosomeSize):
        # call the parent constructor
        Population.__init__(self, populationSize)
        # create a random population
        self.randomPopulation(chromosomeSize)

    def randomPopulation(self, chromosomeSize):
        for i in range(0, self.populationSize):
            self.generation.put(ResnaChromosome(chromosomeSize))


geneticAlgorithm(ResnaPopulation(20, 9))