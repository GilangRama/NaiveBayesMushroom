import pandas as pd
import numpy as np
import scipy.stats as stats
from scipy.stats import chi2_contingency

class ChiSquare:
    def __init__(self, dataframe):
        self.df = dataframe
        self.p = None # nilai P
        self.chi2 = None # Chi Test Statistic
        self.dof = None

        self.dfObserved = None
        self.dfExpected = None

    def _print_chisquare_result(self, colX, alpha):
        # result = ""
        print("====================================")
        if self.p < alpha:
            print("{0} fitur penting untuk prediksi".format(colX))
            print("chi2     : ", self.chi2)
            print("p-value  : ", self.p)
            print("Degree of Freedom    : ", self.dof)
        else:
            print("{0} tidak penting untuk di jadikan prediksi. (Discard {0} from Model)".format(colX))
            print("chi2     : ", self.chi2)
            print("p-value  : ", self.p)
            print("Degree of Freedom    : ", self.dof)
        return

    def TestIndependence(self, colX, colY, alpha=0.05):
        X = self.df[colX].astype(str)
        Y = self.df[colY].astype(str)

        self.dfObserved = pd.crosstab(Y, X)
        chi2, p, dof, expected = stats.chi2_contingency(self.dfObserved.values)
        self.p = p
        self.chi2 = chi2
        self.dof = dof

        self.dfExpected = pd.DataFrame(expected, columns=self.dfObserved.columns, index=self.dfObserved.index)

        self._print_chisquare_result(colX, alpha)

df = pd.read_csv('jamur_corrected.csv')
# df.drop(['bruises', 'gill-attachment', 'veil-type'], axis=1).head(1)
print(df.head())

cT = ChiSquare(df)

testColumns = ['class', 'cap_shape', 'cap_surface', 'cap_color', 'bruises', 'odor',
               'gill_attachment', 'gill_spacing', 'gill_size', 'gill_color',
               'stalk_shape', 'stalk_root', 'stalk_surface_above_ring',
               'stalk_surface_below_ring', 'stalk_color_above_ring',
               'stalk_color_below_ring', 'veil_type', 'veil_color', 'ring_number',
               'ring_type', 'spore_print_color', 'population', 'habitat']
for var in testColumns:
    print(cT.TestIndependence(colX=var, colY="class"))

mushroom = df.drop(['bruises', 'gill_attachment', 'veil_type'], axis=1)

mushroom.to_csv('jamur.csv', index=False)