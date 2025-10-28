from rdkit import Chem
from standardiser import standardise
import numpy as np

def standardise_smiles(smiles):
    st_smiles = []
    for smi in smiles:
        if smi is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        smi = str(smi)
        smi = smi.strip()
        mol = Chem.MolFromSmiles(smi)
        if mol is None:
            st_smi = np.nan
            st_smiles += [st_smi]
            continue
        try:
            std_mol = standardise.run(mol)
            st_smi = Chem.MolToSmiles(std_mol, canonical=True)
            st_smiles += [st_smi]
        except:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
        if std_mol is None:
            st_smi = Chem.MolToSmiles(mol, canonical=True)
            st_smiles += [st_smi]
            continue
    return st_smiles