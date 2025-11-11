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