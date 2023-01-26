import matplotlib.pyplot as plotter
import pandas as pandas

raw_data = {'names':  ['nick', 'panda', 's', 'ari', 'valos'],
            'jan_ir': [143, 122, 101, 106, 365],
            'feb_ir': [122, 132, 144, 98, 62],
            'mar_ir': [65, 88, 12, 32, 65]}

df = pandas.DataFrame(raw_data, columns=['names', 'jan_ir', 'feb_ir', 'mar_ir'])
df['total_ir'] = df['jan_ir'] + df['feb_ir'] + df['mar_ir']

print(df)