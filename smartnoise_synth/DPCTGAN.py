from snsynth import Synthesizer
import pandas as pd
from pathlib import Path


local_file = Path('PUMS_large.csv')

pums = pd.read_csv(local_file, index_col=None) 
synth = Synthesizer.create('dpctgan', epsilon=1.0, verbose=True)
sample = synth.fit_sample(pums, preprocessor_eps=0.5)
print(sample)