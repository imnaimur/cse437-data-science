# Filter for rows where individuals is greater than 10000
ind_gt_10k = homelessness[
    homelessness['individuals']>10000
] 
# See the result
print(ind_gt_10k)

# Filter for rows where region is Mountain
mountain_reg = homelessness[
    homelessness['region'].str.lower() == 'mountain'
]

# See the result
mountain_reg.head()

# Filter for rows where family_members is less than 1000 
# and region is Pacific
fam_lt_1k_pac =homelessness[

    (homelessness['family_members'] < 1000) &
    (homelessness['region'].str.lower() == 'pacific')
]

# See the result
print(fam_lt_1k_pac)