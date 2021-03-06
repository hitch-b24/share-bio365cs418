"""
This module contains class definitions for the objects used in GeneVA. The two main objects are the Mutation object
and the WekaData object.
"""
from Definitions import AMINO_ACIDS_3_1     # used in Mutation object
import copy                                 # used in WekaData object


class Mutation:
    """
    Holds key, value pairs for features associated with a mutation from the ClinVar database
    """

    # Constants to define classifications of mutations
    PATHOGENIC = 1
    BENIGN = 2
    CONFLICTING = 3
    RISK = 4
    UNKNOWN = 5

    CLASSES = ['pathogenic', 'benign', 'conflicting', 'risk', 'unknown']

    def __init__(self, name, symbol="", index=-1, gene="NONE",
                 clinical_significance=UNKNOWN,
                 rs_num=-1, chromosome=-1, chrIndex = -1):
        """
        Represents data about a gene mutation from the cleaned_variants file

        :param name: The name containing additional information about the
                     mutation
        :param symbol: The three-character representation of the amino acid
                       mutation (both old and new, so 6 characters)
        :param index: The position at which the mutation takes place in the
                      sequence
        :param gene: The name of the gene in which the mutation was found
        :param clinical_significance: Usually 'pathogenic' or 'benign'
        :param rs_num: The unique identifier of the mutation in the dbSNP
        """
        self.__name = name
        self.__symbol = symbol
        self.__index = index
        self.__gene = gene
        self.__clinical_sig = clinical_significance
        self.__rs_num = rs_num
        self.__chromosome = chromosome
        self.__chrIndex = chrIndex
        self.__features = dict()

    def get_chromosome(self):
        return self.__chromosome

    def get_chr_index(self):
        return self.__chrIndex

    def get_id(self):
        return self.__name

    def get_name(self):
        return self.__name

    def get_symbol(self, two=False):
        if two:
            part1=self.__symbol[:3]
            part2=self.__symbol[3:]
            X = AMINO_ACIDS_3_1.get(part1, "?")
            Y = AMINO_ACIDS_3_1.get(part2, "?")
            return X + Y
        else:
            return self.__symbol

    def get_index(self):
        return self.__index

    def get_gene(self):
        return self.__gene

    def get_clinical_significance_E(self):
        return self.__clinical_sig

    def get_clinical_significance(self):
        if self.__clinical_sig == Mutation.BENIGN:
            return "benign"
        elif self.__clinical_sig == Mutation.PATHOGENIC:
            return "pathogenic"
        elif self.__clinical_sig == Mutation.CONFLICTING:
            return "conflicting"
        elif self.__clinical_sig == Mutation.RISK:
            return "risk"
        else:
            return "unknown"

    def get_rs_number(self):
        return self.__rs_num

    def get_features(self):
        return self.__features

    def add_feature(self, feature,value):
        self.__features[feature] = value
        return True

    def get_feature(self, feature):
        return self.__features.get(feature, None)

    def add_chromosome(self, chrom):
        self.__chromosome = chrom
        return True

    def add_chr_index(self, chrIndex):
        self.__chrIndex = chrIndex
        return True

    def __str__(self):
        out_string = str(self.__name) + "\t" + \
                     str(self.__symbol) + "\t" + \
                     str(self.__index) + "\t" + \
                     str(self.__gene) + "\t" + \
                     str(self.__rs_num) + "\t" + \
                     self.get_clinical_significance()

        return out_string

    def __eq__(self, other):
        if self.__name.equals(other.get_name()) \
            and self.__symbol.equals(other.get_symbol()) \
            and self.__index == other.get_index() \
            and self.__gene.equals(other.get_gene()) \
            and self.__rs_num == other.get_rs_number() \
            and self.__clinical_sig == other.get_clinical_significance_E():
            return True
        return False


class Feature:
    """
    Contains the feature name, the feature data type (a Weka attribute data type), and the filepath
    to the source data used for storing non-default features
    """

    STRING_TYPE = "string"
    NUMERIC_TYPE = "numeric"

    def __init__(self, name, fileName = "DEFAULT", dataType=NUMERIC_TYPE):
        if fileName == "DEFAULT":
            fileName = "data/" + name + '.txt'

        self.__name = name
        self.__fileName = fileName
        self.__data_type = dataType

    def get_name(self):
        return self.__name

    def get_fileName(self):
        return self.__fileName

    def get_datatype(self):
        return self.__data_type

    def set_filename(self, filename):
        self.__fileName = filename



class WekaData:
    """
    Contains a map of mutation objects that store information about features associated with each mutation.
    """

    def __init__(self):
        self.__mutations = list()
        self.__defaultFeatures = list()
        self.__features = list()
        self.__algorithms = list()
        
    def getDefaultFeatures(self):
        return self.__defaultFeatures

    def setDefaultFeatures(self, defaultFeatures):
        self.__defaultFeatures = copy.deepcopy(defaultFeatures)
        return True

    def addDefaultFeature(self, feature):
        if feature not in self.__defaultFeatures:
            self.__defaultFeatures.append(feature)
            return True
        return False

    def getMutations(self):
        return self.__mutations

    def addMutation(self, mutation):
        self.__mutations.append(mutation)
        return True

    def addMutations(self, mutations):
        self.__mutations.extend(mutations)
        return True

    def getFeatures(self):
        return self.__features

    def addFeature(self, feature):
        if feature not in self.__features:
            self.__features.append(feature)
            return True
        else:
            return False

    def getAlgorithms(self):
        return self.__algorithms

    def addAlgorithm(self, algorithm):
        if algorithm not in self.__algorithms:
            self.__algorithms.append(algorithm)
            return True
        else:
            return False
