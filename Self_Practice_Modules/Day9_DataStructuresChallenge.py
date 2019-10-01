# Print out the 10th item in each.
#
# Print out the 45th key in the dictionary.
#
# Print out the 27th value in the dictionary.

import os, sys

# Import the data file
print(os.getcwd())
base_dir = os.getcwd().split("\\")
separator = "\\"
proj_directory_path = separator.join(base_dir[:-1])
data_file_dir = os.path.join(proj_directory_path, "days\\07-09-data-structures\\code")
sys.path.insert(1, data_file_dir)
print(sys.path)

import data

us_state_abbrev_dict = data.us_state_abbrev
# print(us_state_abbrev_dict)

us_states_list = data.states_list
# print(us_states_list)

sorted(us_state_abbrev_dict)
print(us_state_abbrev_dict)

# print the 10th item in the dict
tenth_item = {k: us_state_abbrev_dict[k] for k in sorted(us_state_abbrev_dict.keys())[9:10]}
print(tenth_item)

# print the 10th item in list
us_states_list.sort()
tenth_in_list = us_states_list[9]
print(tenth_in_list)


# Print out the 45th key in the dictionary.
forty_fifth_key = {k for k in sorted(us_state_abbrev_dict.keys())[44:45]}
print(forty_fifth_key)

# Print out the 27th value in the dictionary if sorted on values.
twenty_seventh_val = {k for k in sorted(us_state_abbrev_dict.values())[26:27]}
print(twenty_seventh_val)
