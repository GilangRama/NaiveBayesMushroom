import pandas as pd

# df = pd.read_csv('jamur.csv')
#
# print(df.head(21))
#
# data = df.head(20)
#
# data.to_csv('studikasus.csv', index=False)

df = pd.read_csv('studikasus.csv')

# class to cap_shape
print("===================================")
class_capshape_crosstab = pd.crosstab(df['cap_shape'], df['class'],
                                      margins=True)
print(class_capshape_crosstab)

# class to cap_surface
print("===================================")
class_capsurface_crosstab = pd.crosstab(df['cap_surface'], df['class'],
                                      margins=True)
print(class_capsurface_crosstab)

# class to cap_color
print("===================================")
class_capcolor_crosstab = pd.crosstab(df['cap_color'], df['class'],
                                      margins=True)
print(class_capcolor_crosstab)

# class to odor
print("===================================")
class_odor_crosstab = pd.crosstab(df['odor'], df['class'],
                                      margins=True)
print(class_odor_crosstab)

# class to gill_spacing
print("===================================")
class_gillspacing_crosstab = pd.crosstab(df['gill_spacing'], df['class'],
                                      margins=True)
print(class_gillspacing_crosstab)

# class to gill_size
print("===================================")
class_gillsize_crosstab = pd.crosstab(df['gill_size'], df['class'],
                                      margins=True)
print(class_gillsize_crosstab)

# class to gill_color
print("===================================")
class_gillcolor_crosstab = pd.crosstab(df['gill_color'], df['class'],
                                      margins=True)
print(class_gillcolor_crosstab)

# class to stalk_shape
print("===================================")
class_stalkshape_crosstab = pd.crosstab(df['stalk_shape'], df['class'],
                                      margins=True)
print(class_stalkshape_crosstab)

# class to stalk_root
print("===================================")
class_stalkroot_crosstab = pd.crosstab(df['stalk_root'], df['class'],
                                      margins=True)
print(class_stalkroot_crosstab)

# class to stalk_surface_above_ring
print("===================================")
class_stalksurface_above_ring_crosstab = pd.crosstab(df['stalk_surface_above_ring'], df['class'],
                                      margins=True)
print(class_stalksurface_above_ring_crosstab)

# class to stalk_surface_below_ring
print("===================================")
class_stalksurface_below_ring_crosstab = pd.crosstab(df['stalk_surface_below_ring'], df['class'],
                                      margins=True)
print(class_stalksurface_below_ring_crosstab)

# class to stalk_color_above_ring
print("===================================")
class_stalkcolor_above_ring_crosstab = pd.crosstab(df['stalk_color_above_ring'], df['class'],
                                      margins=True)
print(class_stalkcolor_above_ring_crosstab)

# class to stalk_color_below_ring
print("===================================")
class_stalkcolor_below_ring_crosstab = pd.crosstab(df['stalk_color_below_ring'], df['class'],
                                      margins=True)
print(class_stalkcolor_below_ring_crosstab)

# class to veil_color
print("===================================")
class_veil_colorcrosstab = pd.crosstab(df['veil_color'], df['class'],
                                      margins=True)
print(class_veil_colorcrosstab)

# class to ring_number
print("===================================")
class_ring_numbercrosstab = pd.crosstab(df['ring_number'], df['class'],
                                      margins=True)
print(class_ring_numbercrosstab)

# class to ring_type
print("===================================")
class_ring_typecrosstab = pd.crosstab(df['ring_type'], df['class'],
                                      margins=True)
print(class_ring_typecrosstab)

# class to spore_print_color
print("===================================")
class_spore_print_colorcrosstab = pd.crosstab(df['spore_print_color'], df['class'],
                                      margins=True)
print(class_spore_print_colorcrosstab)

# class to population
print("===================================")
class_populationcrosstab = pd.crosstab(df['population'], df['class'],
                                      margins=True)
print(class_populationcrosstab)

# class to habitat
print("===================================")
class_habitatcrosstab = pd.crosstab(df['habitat'], df['class'],
                                      margins=True)
print(class_habitatcrosstab)


