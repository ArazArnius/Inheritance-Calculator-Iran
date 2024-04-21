import pandas as pd

class Person:
    def __init__(self, name, parent_name, status, money, spouse, son=0, daughter=0):
        self.name = name
        self.parent_name = parent_name
        self.status = status
        self.money = money
        self.spouse = spouse
        self.son = son
        self.daughter = daughter
        self.share = 0

# ++++++++
class GrandFather(Person):
    def __init__(self, name, parent_name, status, money, spouse, son=0, daughter=0):
        super().__init__(name, parent_name, status, money, spouse, son, daughter)
        self.sex = "male"

    def __str__(self):
        return self.name
    
# ++++++++
class GrandMother(Person):
    def __init__(self, name, parent_name, status, money, spouse, son=0, daughter=0):
        super().__init__(name, parent_name, status, money, spouse, son, daughter)
        self.sex = "female"    

    def __str__(self):
        return self.name
    
# ++++++++
class Father(Person):
    def __init__(self, name, parent_name, status, money, spouse, son=0, daughter=0):
        super().__init__(name, parent_name, status, money, spouse, son, daughter)
        self.sex = "male"

    def __str__(self):
        return self.name
    
# ++++++++
class Mother(Person):
    def __init__(self, name, parent_name, status, money, spouse, son=0, daughter=0):
        super().__init__(name, parent_name, status, money, spouse, son, daughter)
        self.sex = "female"

    def __str__(self):
        return self.name
    
# ++++++++
class SonFather:
    def __init__(self, name, parent_name, status, money):
        self.name = name
        self.parent_name = parent_name
        self.status = status
        self.money = money
        self.sex = "male"
        self.share = 0

    def __str__(self):
        return self.name
    
# ++++++++
class DaughterFather:
    def __init__(self, name, parent_name, status, money):
        self.name = name
        self.parent_name = parent_name
        self.status = status
        self.money = money
        self.sex = "female"
        self.share = 0

    def __str__(self):
        return self.name
    
# ++++++++
class SonMother:
    def __init__(self, name, parent_name, status, money):
        self.name = name
        self.parent_name = parent_name
        self.status = status
        self.money = money
        self.sex = "male"
        self.share = 0

    def __str__(self):
        return self.name
    
# ++++++++
class DaughterMother:
    def __init__(self, name, parent_name, status, money):
        self.name = name
        self.parent_name = parent_name
        self.status = status
        self.money = money
        self.sex = "female"
        self.share = 0

    def __str__(self):
        return self.name
    
# ++++++++
# A function to create the whole family
def create_family():
    family = {}
    grandfather = GrandFather(name="grandfather", parent_name=None, status=True, money=10000, spouse=True, son=2, daughter=1)
    grandmother = GrandMother(name="grandmother", parent_name=None, status=grandfather.spouse, money=8000, spouse=grandfather.status, son=grandfather.son, daughter=grandfather.daughter)
    family["grandfather"] = grandfather
    family["grandmother"] = grandmother

    # Create fathers based on the number of sons of the grandfather
    # We should either get the information of each person from the input or set them ourselves which will be the same as the others of the same class
    for i in range(grandfather.son):
        father_name = "father_" + str(i + 1)
        father = Father(name=father_name, parent_name="grandfather", status=True, money=100, spouse=False, son=1, daughter=1)
        family[father_name] = father

        # Create children of father
        for j in range(father.son):
            son_father_name = "son_father_" + str(i + 1) + "_" + str(j + 1)
            son_father = SonFather(name=son_father_name, parent_name=father_name, status=True, money=4)
            family[son_father_name] = son_father

        for k in range(father.daughter):
            daughter_father_name = "daughter_father_" + str(i + 1) + "_" + str(k + 1)
            daughter_father = DaughterFather(name=daughter_father_name, parent_name=father_name, status=False, money=4)
            family[daughter_father_name] = daughter_father

    # Create mothers based on the number of daughters of the grandfather
    for i in range(grandfather.daughter):
        mother_name = "mother_" + str(i + 1)
        mother = Mother(name=mother_name, parent_name="grandfather", status=True, money=15, spouse=True, son=2, daughter=2)
        family[mother_name] = mother

        # Create children of mother
        for j in range(mother.son):
            son_mother_name = "son_mother_" + str(i + 1) + "_" + str(j + 1)
            son_mother = SonMother(name=son_mother_name, parent_name=mother_name, status=True, money=4)
            family[son_mother_name] = son_mother

        for k in range(mother.daughter):
            daughter_mother_name = "daughter_mother_" + str(i + 1) + "_" + str(k + 1)
            daughter_mother = DaughterMother(name=daughter_mother_name, parent_name=mother_name, status=True, money=4)
            family[daughter_mother_name] = daughter_mother

    return family

# ++++++++
# Function that calculates the share of each member of the family
def cal_share(dead, family):
    total_wealth = dead.money
    dead.status = False
    print(f"\nDead family member:\t{dead.name}\nTotal wealth:\t{dead.money}\n")

    # If the parents are grandfather or grandmother and at least one of them is alive,
    if isinstance(dead, (Father, Mother)) and (family["grandfather"].status or family["grandmother"].status):
        if family["grandfather"].status and family["grandmother"].status:
            family["grandfather"].share = 2 * total_wealth / 3
            family["grandfather"].money += family["grandmother"].share
            family["grandmother"].share =  total_wealth / 3
            family["grandmother"].money += family["grandmother"].share
        elif family["grandfather"].status:
            family["grandfather"].share = total_wealth
            family["grandfather"].money += family["grandfather"].share
        elif family["grandmother"].status:
            family["grandmother"].share = total_wealth
            family["grandmother"].money += family["grandmother"].share

        spouse_share = 0
        son_share = 0
        daughter_share = 0
        total_wealth = 0

    # assuming the grandchildren in the family wont die, we wont need to check for parents anymore
    else:
        # Deal with the spouse share. If they were alive, calculate the share and subtract the total wealth from it else just keep going
        if dead.spouse:
            if dead.sex == "male":
                spouse_share = total_wealth / 8
                # Grandparents are the only people who are married and have exclusive classes
                if isinstance(dead, GrandFather):
                    family["grandmother"].money += spouse_share
                    family["grandmother"].share = spouse_share
            elif dead.sex == "female":
                spouse_share = total_wealth / 4
                if isinstance(dead, GrandMother):
                    family["grandfather"].money += spouse_share
                    family["grandfather"].share = spouse_share
            total_wealth -= spouse_share
        else:
            spouse_share = 0

        # Deal with the children's share
        son_count = 0
        daughter_count = 0
        # Count the alive children. In this program all of the children are defined as alive
        # But it will work quite well if you decide to change the create_family to input each person's info
        for member in family.values():
            # Since children were named after their fathers and not mothers, when grandmother dies, the children
            # Won't be considered as her children:))) this is getting so big
            if dead.name == "grandmother":
                if member.parent_name == "grandfather" and member.status:
                    if member.sex == "male":
                        son_count += 1
                    else:
                        daughter_count += 1
            # Else, just check the parent name
            elif member.parent_name == dead.name and member.status:
                if member.sex == "male":
                    son_count += 1
                else:
                    daughter_count += 1

        children_count = son_count + daughter_count
        print("*children count: ", children_count, "\n*son(s): ", son_count, "\n*daughter(s): ", daughter_count, "\n")

        if children_count == 0:
            son_share = 0
            daughter_share = 0
            print("No children.. ")
        elif daughter_count == 0:
            daughter_share = 0
            son_share = total_wealth / son_count
        elif son_count == 0:
            son_share = 0
            daughter_share = total_wealth / daughter_count
        else:
            son_share = 2 * total_wealth / (son_count * 2 + daughter_count)
            daughter_share = total_wealth / (son_count * 2 + daughter_count)

        for member in family.values():
            # Same thing we did for the problem with grandmother
            if dead.name == "grandmother":
                if member.parent_name == "grandfather" and member.status:
                    if member.sex == "male":
                        member.share = son_share
                        member.money += son_share
                        total_wealth -= son_share
                    elif member.sex == "female":
                        member.share = daughter_share
                        member.money += daughter_share
                        total_wealth -= daughter_share
                    children_count -= 1
                if (children_count <= 0):
                    break
            # If the dead is not Grandmother, then just simply do it
            elif member.parent_name == dead.name and member.status:
                if member.sex == "male":
                    member.share = son_share
                    member.money += son_share
                    total_wealth -= son_share
                elif member.sex == "female":
                    member.share = daughter_share
                    member.money += daughter_share
                    total_wealth -= daughter_share
                children_count -= 1
            if (children_count <= 0):
                break # In case we reached what we wanted, the program wont run for nothing

    print("The money left from the legacy: ", total_wealth)
    show_shares(family, spouse_share, son_share, daughter_share)

# ++++++++
def show_shares(family, spouse_share, son_share, daughter_share):
    # Parent's share: 
    if family["grandfather"].share != 0 and family["grandmother"].share != 0:
        print(f"Grandfather's share: {family['grandfather'].share}\nGrandmother's share: {family['grandmother'].share} ")
    elif family["grandfather"].share != 0:
        print(f"Grandfather's share: {family['grandfather'].share}\nand grandmother is dead. ")
    elif family["grandmother"].share != 0:
        print(f"Grandmother's share: {family['grandmother'].share}\nand grandfather is dead. ")

    # Spouse share:
    if family[dead].spouse:
        print(f"The spouse took {spouse_share}. ")

    # Children's share
    if family[dead].son != 0:
        print(f"Each son took {son_share}. ")
    if family[dead].daughter != 0:
        print(f"Each daughter took {daughter_share}. ")

# ++++++++
def family_dataframe(family):
    # Create a dictionary to hold the family members' attributes
    data = {"Status": [], "Money": [], "Spouse": [], "Son": [], "Daughter": [], "share": []}
    index = []

    # Iterate through the family dictionary and assign the values to data{}
    for member_name, member in family.items():
        if isinstance(member, (GrandFather, GrandMother, Father, Mother)):
            data["Status"].append(member.status)
            data["Money"].append(member.money)
            data["Spouse"].append(member.spouse)
            data["Son"].append(member.son)
            data["Daughter"].append(member.daughter)
            data["share"].append(member.share)
        else:
            data["Status"].append(member.status)
            data["Money"].append(member.money)
            data["Spouse"].append(None)
            data["Son"].append(None)
            data["Daughter"].append(None)
            data["share"].append(member.share)
            
        index.append(member_name)

    # Create the DataFrame using the dictionary and set the index to the name of each object
    df = pd.DataFrame(data, index=index)
    return df

# --------
# MAIN
family = create_family()
print(family_dataframe(family))
dead = input("\n********\n\nWho is the dead family member whose legacy will be distributed among the family? ").lower() # choose the names as shown in the df

if isinstance(family[dead], (SonFather, SonMother, DaughterFather, DaughterMother)):
    print("You may not k!ll the children. ")
elif not family[dead].status:
    print(f"{family[dead].name} is already dead </3 ")
else:
    cal_share(family[dead], family)
    print("\n\nThe family after the loss:\n\n", family_dataframe(family), "\n\n********")

# Please modify the values each family member holds in order to check the code.
# You may do that in the 'create_family()' function
