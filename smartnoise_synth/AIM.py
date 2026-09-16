import pandas as pd
from snsynth import Synthesizer

pums = pd.read_csv("PUMS_large.csv")

synth = Synthesizer.create("aim", epsilon=3.0, verbose=True)
synth.fit(pums, preprocessor_eps=1.0)
pums_synth = synth.sample(1000)
print(pums_synth)