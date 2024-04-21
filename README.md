**Iran Inheritance Calculator**

This Python project, developed as part of the second-semester curriculum at Azarbaijan Shahid Madani University, serves as an educational tool for learning object-oriented programming inheritance concepts and Pandas library in Python. The program implements inheritance calculation based on (simplified) Iran's laws; If the man passes away, his wife inherits 1/8 of his estate. If the woman passes away, her husband inherits 1/4 of her estate. If one parent passes away, after deducting the spouse's share (as per previous rules), the remaining estate is divided among the children. If both parents pass away, the combined estate is divided among the children. **Sons inherit twice as much as daughters!** No inheritance share for the spouse and children if the parents are alive. Each family member, besides inheriting from their parent, also has their own money that adds to their overall wealth. Consideration for scenarios where a parent may have no children or no sons or daughters shall be implemented.

**Note:** This project aims to provide a hands-on learning experience with OOP inheritance and Pandas in Python. Some functions may be unnecessary, and certain aspects may deviate from real-world scenarios to align with educational objectives.

**Features:**
- Define classes for various inheritance levels: grandfather, grandmother, father, mother, son (father/son), daughter (father/daughter).
- Calculate each family member's share of the inheritance based on predefined rules.
- Generate a DataFrame representing the family structure and inheritance shares.
- Interactive functionality prompts users to input the deceased family member for inheritance distribution.

**Usage:**
1. Modify family member attributes and relationships in the `create_family()` function to simulate different scenarios.
2. Run the program and input the deceased family member name as shown in the first DataFrame when prompted to calculate inheritance distribution.
3. View the inheritance distribution and the updated family structure in the generated DataFrame.

