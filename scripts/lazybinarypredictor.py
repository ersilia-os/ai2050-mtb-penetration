import os
import sys
import pandas as pd
from lazyqsar.qsar import LazyBinaryQSAR


root = os.path.dirname(os.path.abspath(__file__))

dataset = sys.argv[1]
models = ["sarathy2016", "janardhan2016", "radchenko2023", "lepori2025_mtb", "lepori2025_msm", "mycpermcheck", "valitalo2016"]
pred_file = os.path.join(root, "..","data", "raw", f"{dataset}.csv")

df = pd.read_csv(pred_file)
x_test = df["smiles"].tolist()

for m in models:
    model_folder = os.path.join(root, "..", "models", f"{m}.zip")
    model = LazyBinaryQSAR.load(model_folder)
    y_pred = model.predict_proba(smiles_list=x_test)[:, 1]
    df[f"{m}"] = y_pred

df.to_csv(os.path.join(root, "..","output", "results", f"{dataset}.csv"), index=False)

