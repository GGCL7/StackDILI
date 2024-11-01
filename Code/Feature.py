import pandas as pd
import iFeatureOmegaCLI


input_csv = "Dataset.csv"
temp_smiles_file = "Dataset.txt"
output_csv = "Dataset_feature.csv"


df = pd.read_csv(input_csv)


ligand = iFeatureOmegaCLI.iLigand(temp_smiles_file)


ligand.display_feature_types()


feature_types = [
    "Constitution",
    "Pharmacophore",
    "MACCS fingerprints",
    "E-state fingerprints"
]


all_features_df = pd.DataFrame()


for feature_type in feature_types:
    ligand.get_descriptor(feature_type)  
    feature_df = pd.DataFrame(ligand.encodings)  
    all_features_df = pd.concat([all_features_df, feature_df], axis=1) 


if len(all_features_df) != len(df):
    raise ValueError("The number of extracted features does not match the number of original data. Please check the data.")


merged_df = pd.concat([df.reset_index(drop=True), all_features_df.reset_index(drop=True)], axis=1)


merged_df.to_csv(output_csv, index=False)




