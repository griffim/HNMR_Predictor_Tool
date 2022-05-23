import pandas as pd
import sys

# Stores the directory location of the input file.
#
# Example Input File:
# Peak       PPM
#    1        0.9
#    2        1.6
#    3        5.4
#
input_path = input("Please enter the directory location of the input CSV (omit .csv): ")
directory_path = str(input_path + ".csv")

# READ ME !!!
# The code below stores the user inputted file name as a variable csv file, then saves the OS directory as a variable.
#
# NOTE: Can manipulate the file directory if keeping all input files in one place to only require input of the file name.
#
# If this is desired, read below:
#
# COMMENT OUT lines 12 and 13
# UNCOMMENT the chunk of code below; lines 25, 26, and 27.
#
# input_csv = str(input("Enter the import file name: ") + ".csv")
# directory_path = \
#     (os.path.join(r"C:\Users\griff\PycharmProjects\NMR_Functional_Group_Predictor\DATA_INPUT_FOLDER" + "\\" + input_csv))


# Creates function vector to multiply array by 10 (normalizes to range assignments later on).
def x10(x):
    return x * 10


# Opens CSV through directory through Pandas.
try:
    col_list = ["Peak", "PPM"]
    df = (pd.read_csv(str(directory_path), usecols=col_list))
    df_x10 = x10(pd.read_csv(str(directory_path), usecols=col_list))
    s = pd.Series(df_x10["PPM"])
except FileNotFoundError:
    print("Unable to find file. Perhaps file name misspelled or in wrong folder?")
    sys.exit()


# Maps boolean return from s.between function to string of whether values are in functional group range or not.

# Functional Group Assignments:
# Variables here are defined functional groups, assigned to the common range of ppm values that show up in H-NMR spectra.
# Sources for these values can be found in "Techniques in Organic Chemistry, 3rd Edition" by Mohrig.

# Alkanes range (C-C-H), 0.8 to 1.9
s_alkane = s.between(8, 19, 'both')
s_alkane = s_alkane.map({True: "Alkane", False: ""})
df = pd.concat([df, s_alkane.rename('')], axis=1)

# Amines (C-N-H), 0.6 to 4.5
s_amine = s.between(6, 45, 'both')
s_amine = s_amine.map({True: "Amine", False: ""})
df = pd.concat([df, s_amine.rename('')], axis=1)

# Alcohols (C-O-H), 0.5 to 5.0
s_alcohol = s.between(5, 50, 'both')
s_alcohol = s_alcohol.map({True: "Alcohol", False: ""})
df = pd.concat([df, s_alcohol.rename('')], axis=1)

# Allylic Alkenes (C=C-C-H), 1.5 to 2.6
s_allyl_alke = s.between(15, 26, 'both')
s_allyl_alke = s_allyl_alke.map({True: "Allylic Alkene", False: ""})
df = pd.concat([df, s_allyl_alke.rename('')], axis=1)

# Alkyne, triple bond, (C=_C-H), 1.7 to 3.1
s_alkyne = s.between(17, 31, 'both')
s_alkyne = s_alkyne.map({True: "Alkyne", False: ""})
df = pd.concat([df, s_alkyne.rename('')], axis=1)

# Carbonyl (O=C-C-H), 1.9 to 3.3
s_carbonyl = s.between(19, 33, 'both')
s_carbonyl = s_carbonyl.map({True: "Carbonyl", False: ""})
df = pd.concat([df, s_carbonyl.rename('')], axis=1)

# Halide (X-C-H), 2.1 to 4.5
s_halide = s.between(21, 45, 'both')
s_halide = s_halide.map({True: "Halide", False: ""})
df = pd.concat([df, s_halide.rename('')], axis=1)

# Benzylic Aromatic (Ar-C-H), 2.2 to 3.0
s_benzylic_ar = s.between(22, 30, 'both')
s_benzylic_ar = s_benzylic_ar.map({True: "Benzylic Aromatic", False: ""})
df = pd.concat([df, s_benzylic_ar.rename('')], axis=1)

# Alpha position to alcohol, ester, or ether (O-C-H), 3.2 to 5.3
s_alpha_alcEstEth = s.between(32, 53, 'both')
s_alpha_alcEstEth = s_alpha_alcEstEth.map({True: "Alpha to Alc, Est, or Eth", False: ""})
df = pd.concat([df, s_alpha_alcEstEth.rename('')], axis=1)

# Alkene (C=C-H), 4.5 to 8.5
s_alkene = s.between(45, 85, 'both')
s_alkene = s_alkene.map({True: "Alkene", False: ""})
df = pd.concat([df, s_alkene.rename('')], axis=1)

# Phenol (Ar-O-H), 4.0 to 8.0
s_phenol = s.between(40, 80, 'both')
s_phenol = s_phenol.map({True: "Phenol", False: ""})
df = pd.concat([df, s_phenol.rename('')], axis=1)

# Amide (O=C-N-H), 5.5 to 9.5
s_amide = s.between(55, 95, 'both')
s_amide = s_amide.map({True: "Amide", False: ""})
df = pd.concat([df, s_amide.rename('')], axis=1)

# Aromatic (Ar-H), 6.5 to 9.0
s_aromatic = s.between(65, 90, 'both')
s_aromatic = s_aromatic.map({True: "Aromatic", False: ""})
df = pd.concat([df, s_aromatic.rename('')], axis=1)

# Aldehyde (O=C-H), 9.5 to 10.5
s_aldehyde = s.between(95, 105, 'both')
s_aldehyde = s_aldehyde.map({True: "Aldehyde", False: ""})
df = pd.concat([df, s_aldehyde.rename('')], axis=1)

# Carboxylic Acid (O=C-O-H), 9.7 to 12.5
s_carboxylic = s.between(97, 125, 'both')
s_carboxylic = s_carboxylic.map({True: "Carboxylic Acid", False: ""})
df = pd.concat([df, s_carboxylic.rename('')], axis=1)


# Appends to the CSV file if file is closed, otherwise prints Error message if file is open.
try:
    df.to_csv(directory_path, index=False)
except PermissionError:
    print("Permission Denied to edit CSV. Check if file is already open.")
    sys.exit()
