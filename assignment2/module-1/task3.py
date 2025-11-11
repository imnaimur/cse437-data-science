# Sort homelessness first by region (default is ascending), 
# then by family_members in descending order (False)

homelessness_reg_fam = homelessness.sort_values(
    by=["region", "family_members"], 
    ascending=[True, False]
)

# Print the head of the sorted DataFrame
print(homelessness_reg_fam.head())