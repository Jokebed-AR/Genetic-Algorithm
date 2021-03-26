import numpy as np
import random

class DNA():
    def __init__(self, chromosome, mutation_rate, n_ind, n_selection, n_generations, imp = True):
        self.chromosome = chromosome;
        self.mutation_rate = mutation_rate;
        self.n_ind = n_ind;
        self.n_selection = n_selection;
        self.n_generations = n_generations;
        self.imp = imp;

    #creates new individuals with random binary values
    def new_ind(self, min = 0, max = 2):
        ind = [np.random.randint(min, max) for i in range(len(self.chromosome))]
        return ind;

    #creates the population
    def population(self):
        population = [self.new_ind() for i in range(self.n_ind)]
        return population;

    #evaluates one individual
    def fitness(self, ind):
        fitness = 0;
        #this function will return the number of genes with the correct value
        for i in range(len(ind)):
            if ind[i] == self.chromosome[i]:
                fitness += 1
        #the best fitness in this case is 8
        return fitness;

    def selection(self, population):
        values = [(self.fitness(i),i) for i in population]
        #sort individuals from worst value to the best
        values = [(i[1]) for i in sorted(values)]
        #returns the selected individuals (the best individuals)
        selected = values[len(values) - self.n_selection :]
        return selected;

    def crossover(self, population, selected):
        point = 0;
        parents = []

        for i in range(len(population)):
            point = np.random.randint(1, len(self.chromosome) - 1)  #a point is generated on a chromosome to do the crossover
            parents = random.sample(selected, 2)
            population[i][:point] = parents[0][:point]  #takes the values from the beginning to the point
            population[i][point:] = parents[1][point:]  #takes the values from the point to the end
        return population;

    def mutation(self, population):
        for i in range (len(population)):
            if random.random() <= self.mutation_rate:
                point = random.randint(1, len(self.chromosome) - 1)
                gen = np.random.randint(0, 2)

                #different value than before
                while gen == population[i][point]:
                    gen = np.random.randint(0, 2)

                population[i][point] = gen
        return population;

    def run_ga(self):

        population = self.population()

        for i in range(self.n_generations):

            if self.imp:
                print('----')
                print('Goal:       ', self.chromosome)
                print('Generation: ', i)
                print('Population: ', population)

        selected = self.selection(population)
        population = self.crossover(population, selected)
        population = self.mutation(population)


def main():
    chromosome = [1, 1, 1, 1, 1, 1, 1, 1] #this is the chromosome we want to reach
    #you can modify some of the parameters down below
    model = DNA(chromosome = chromosome, mutation_rate = 0.08,  n_ind = 20, n_selection = 5, n_generations = 40, imp = True)

    model.run_ga()

if __name__ == '__main__':
    main()
