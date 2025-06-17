# Hello dweller,
#
# I'm the overseer of our vault, in which we all live.
#
# I make it short: We are out of water. The only question is when!
# Here is a list of all dwellers with their respective age int[] ageOfDweller.
# In our tank currently are int water liters of water.
# I want to know from you: How long will rich our supplies.
#
# Remember!
# Each dweller has a different water consumption.
# A dweller under 18 consumes 1 liter per day, everyone older than 50 needs 1.5 liters and the rest needs 2 liters per day.
# Each dweller must get its prescribed ration of water, every day!
# If not satisfied all dweller, then our days are numbered.
#
# Good luck! I'll bet on you!
#
#
# Note from Vault Technicians:
# Your program returns a positive integer. The residual water is not calculated.
# return -1; - If no dweller living inside of the Vault.
#
#
# Imagine further "Vault experience":
#
# Vault experience (1): Enough water for how many days?
# Vault experience (2): Hack my terminal!
# Vault experience (3): Populate the vaults
# Fundamentals
# Solution
int thirstyIn(int water, std::vector<int> ageOfDweller)
{
    if (ageOfDweller.empty()) return -1;
    double daily = 0;
    for (int &cost : ageOfDweller) {
        if (cost < 18) ++daily;
        else if (cost <= 50) daily += 2;
        else daily += 1.5;
    }
    return static_cast<int>(water / daily);
}