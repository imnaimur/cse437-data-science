# Some Important fuctions 

## sort_values 
    (by, *, axis=0, ascending=True, inplace=False, kind='quicksort', na_position='last', ignore_index=False, key=None)


## DataFrame.value_counts
    (subset=None, normalize=False, sort=True, ascending=False, dropna=True)

## pivot_table
    (data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=<no_default>, sort=True)

## groupby
    (by=None, axis=<no_default>, level=None, as_index=True, sort=True, group_keys=True, observed=<no_default>, dropna=True)


# code to watch later:
----------------------------------------------
# Index temperatures by country & city
temperatures_ind = temperatures.set_index(['country','city'])

# List of tuples: Brazil, Rio De Janeiro & Pakistan, Lahore
rows_to_keep = [
    ('Brazil', 'Rio De Janeiro'),
    ('Pakistan', 'Lahore')
]

# Subset for rows to keep
print(temperatures_ind.loc[rows_to_keep])

----------------------------------------------

# Sort temperatures_ind by index values (default: all levels, ascending)
print(temperatures_ind.sort_index())

# Sort temperatures_ind by index values at the city level
print(temperatures_ind.sort_index(level='city'))

# Sort temperatures_ind by country (ascending) then descending city
print(temperatures_ind.sort_index(level=['country', 'city'], ascending=[True, False]))

----------------------------------------------

