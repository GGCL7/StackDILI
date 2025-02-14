# Welcome to StackDILI: Enhancing drug-induced liver injury prediction through stacking strategy with effective molecular representations
Drug-induced liver injury (DILI) is a major challenge in drug development, often leading to clinical trial failures and market withdrawals due to liver toxicity. This study presents StackDILI, a computational framework designed to accelerate toxicity assessment by predicting DILI risk. StackDILI integrates multiple molecular descriptors to extract structural and physicochemical features, including constitution, pharmacophore, MACCS, and E-state descriptors. Additionally, a genetic algorithm is employed for feature selection and optimization, ensuring that the most relevant features are used. These optimized features are processed through a stacking ensemble model comprising multiple tree-based machine learning models, improving prediction accuracy and interpretability. Notably, StackDILI demonstrates strong performance on the DILIrank test set and maintains robustness across cross-validation. Moreover, interpretability analysis reveals key molecular features associated with DILI risks, providing valuable insights into toxicity prediction. To further improve accessibility, a user-friendly web interface is developed, allowing users to input SMILES sequences and receive rapid predictions with ease. The StackDILI model provides a powerful tool for efficient DILI assessment, supporting safer drug development.

This DILI risk prediction tool developed by a team from the Chinese University of Hong Kong (Shenzhen)

<span style="color: red;">**Notice:** Due to a change in the university's server domain, some of the URLs mentioned in the paper might no longer be accessible. However, the web server link provided above remains valid and can be used without any issues (https://awi.cuhk.edu.cn/~biosequence/StackDILI/).

![The workflow of this study](https://github.com/GGCL7/StackDILI/blob/main/workflow.png)


# Dataset for this study
We provided our dataset and you can find them [Dataset](https://github.com/GGCL7/StackDILI/tree/main/Data)


# Model source code
The source code for training our models can be found here [Model source code](https://github.com/GGCL7/StackDILI/tree/main/Code).

# Web server
We also provide a web server to the users,  which you can access from the [Web server](https://awi.cuhk.edu.cn/~biosequence/StackDILI/).


