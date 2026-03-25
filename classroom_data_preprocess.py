import pandas as pd
import numpy as np
import pickle

drug = pd.read_csv("classroom_data/Drug_sensitivity_AUC_(Sanger_GDSC1)_subsetted.csv")
expression = pd.read_csv("classroom_data/Expression_Public_25Q3_subsetted.csv")

gefitinib = drug.loc[:, ["Unnamed: 0", "GEFITINIB (GDSC1:1010)"]]
gefitinib = gefitinib.rename(columns={'GEFITINIB (GDSC1:1010)': 'GEFITINIB'})
gefitinib_expression = gefitinib.merge(expression)
gefitinib_expression = gefitinib_expression.drop(columns="Unnamed: 0")
gefitinib_expression = gefitinib_expression.dropna(subset=["GEFITINIB"])

with open("classroom_data/GEFITINIB_Expression.pickle", 'wb') as file:
  pickle.dump(gefitinib_expression, file)


docetaxel = drug.loc[:, ["Unnamed: 0", "DOCETAXEL (GDSC1:1007)"]]
docetaxel = docetaxel.rename(columns={'DOCETAXEL (GDSC1:1007)': 'DOCETAXEL'})
docetaxel_expression = docetaxel.merge(expression)
docetaxel_expression = docetaxel_expression.drop(columns="Unnamed: 0")
docetaxel_expression = docetaxel_expression.dropna(subset=["DOCETAXEL"])

docetaxel_expression_s = docetaxel_expression.sample(n=600, random_state=1)

with open("classroom_data/DOCETAXEL_Expression.pickle", 'wb') as file:
  pickle.dump(docetaxel_expression_s, file)
