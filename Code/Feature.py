import pandas as pd
import iFeatureOmegaCLI

# 定义输入和输出文件路径
input_csv = "/Users/ggcl7/Desktop/药机器学习特征/Total_dataset.csv"
temp_smiles_file = "/Users/ggcl7/Desktop/药机器学习特征/Total_dataset.txt"
output_csv = "/Users/ggcl7/Desktop/药机器学习特征/Total_dataset_feature.csv"

# 读取CSV文件
df = pd.read_csv(input_csv)

# 创建iLigand实例并加载SMILES数据文件
ligand = iFeatureOmegaCLI.iLigand(temp_smiles_file)

# 打印所有可用的特征描述符类型（可选）
ligand.display_feature_types()

# 定义需要提取的特征类型
feature_types = [
    "Constitution",
    "Pharmacophore",
    "MACCS fingerprints",
    "E-state fingerprints"
]

# 初始化一个空DataFrame用于存储所有特征
all_features_df = pd.DataFrame()

# 遍历每种特征类型并提取特征
for feature_type in feature_types:
    print(f"提取 {feature_type} 特征...")
    ligand.get_descriptor(feature_type)  # 提取特征
    feature_df = pd.DataFrame(ligand.encodings)  # 转换为DataFrame
    all_features_df = pd.concat([all_features_df, feature_df], axis=1)  # 拼接特征

# 检查特征数量是否与原始数据一致
if len(all_features_df) != len(df):
    raise ValueError("提取的特征数量与原始数据数量不匹配，请检查数据。")

# 合并提取的特征与原始的 SMILES、Label 和 ref 信息
merged_df = pd.concat([df.reset_index(drop=True), all_features_df.reset_index(drop=True)], axis=1)

# # 保存所有特征到新的CSV文件
merged_df.to_csv(output_csv, index=False)

print(f"特征提取完成，结果已保存为：{output_csv}")




