import pandas as pd

df = pd.read_csv('mushrooms.csv')
# data = df.drop(['class', 'bruises', 'gill_attachment', 'veil_type'], axis=1).head(3)
# data.to_csv('jamur_coba.csv', index=False)

df.rename(
    columns = ({'cap-shape' : 'cap_shape',
                'cap-surface' : 'cap_surface',
                'cap-color' : 'cap_color',
                'gill-attachment' : 'gill_attachment',
                'gill-spacing' : 'gill_spacing',
                'gill-size' : 'gill_size',
                'gill-color' : 'gill_color',
                'stalk-shape' : 'stalk_shape',
                'stalk-root' : 'stalk_root',
                'stalk-surface-above-ring' : 'stalk_surface_above_ring',
                'stalk-surface-below-ring' : 'stalk_surface_below_ring',
                'stalk-color-above-ring' : 'stalk_color_above_ring',
                'stalk-color-below-ring' : 'stalk_color_below_ring',
                'veil-type' : 'veil_type',
                'veil-color' : 'veil_color',
                'ring-number' : 'ring_number',
                'ring-type' : 'ring_type',
                'spore-print-color' : 'spore_print_color'}),
    inplace=True,
)

print(df.columns)

df.to_csv('jamur_corrected.csv', index=False)