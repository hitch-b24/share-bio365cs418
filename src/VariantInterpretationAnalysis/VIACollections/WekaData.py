################################################################################
# WekaData - Data Structure
#
# Contains a map of mutation objects that store information about features
# associated with each mutation
#
from VariantInterpretationAnalysis.VIACollections.Mutation import Mutation


class WekaData:

    def __init__(self):
        self.__mutations = dict()
        self.__features = list()

    def getMutation(self,mutation):
        if mutation in self.__mutations.keys():
            return self.__mutations[mutation]

    def addMutation(self,mutation):
        if mutation in self.__mutations.keys():
            return False
        else:
            m = Mutation(mutation)
            self.__mutations[mutation] = m
