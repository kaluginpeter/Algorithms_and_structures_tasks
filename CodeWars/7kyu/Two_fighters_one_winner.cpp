/*
Create a function that returns the name of the winner in a fight between two fighters.

Each fighter takes turns attacking the other and whoever kills the other first is victorious. Death is defined as having health <= 0.

Each fighter will be a Fighter object/instance. See the Fighter class below in your chosen language.

Both health and damagePerAttack (damage_per_attack for python) will be integers larger than 0. You can mutate the Fighter objects.

Your function also receives a third argument, a string, with the name of the fighter that attacks first.

Example:
  declare_winner(Fighter("Lew", 10, 2), Fighter("Harry", 5, 4), "Lew") => "Lew"

  Lew attacks Harry; Harry now has 3 health.
  Harry attacks Lew; Lew now has 6 health.
  Lew attacks Harry; Harry now has 1 health.
  Harry attacks Lew; Lew now has 2 health.
  Lew attacks Harry: Harry now has -1 health and is dead. Lew wins.
class Fighter
{
private:
    std::string name;

    int health;

    int damagePerAttack;

public:
    Fighter(std::string name, int health, int damagePerAttack)
    {
        this->name = name;
        this->health = health;
        this->damagePerAttack = damagePerAttack;
    }

    ~Fighter() { };

    std::string getName()
    {
        return name;
    }

    int getHealth()
    {
        return health;
    }

    int getDamagePerAttack()
    {
        return damagePerAttack;
    }

    void setHealth(int value)
    {
        health = value;
    }
};
GamesAlgorithmsLogicFundamentals
*/
// Solution
std::string declareWinner(Fighter* fighter1, Fighter* fighter2, std::string firstAttacker)
{
    bool isFirst = (*fighter1).getName() == firstAttacker;
    while ((*fighter1).getHealth() > 0 && (*fighter2).getHealth() > 0) {
        if (isFirst) (*fighter2).setHealth((*fighter2).getHealth() - (*fighter1).getDamagePerAttack());
        else (*fighter1).setHealth((*fighter1).getHealth() - (*fighter2).getDamagePerAttack());
        isFirst = !isFirst;
    }
    return ((*fighter1).getHealth() > 0 ? (*fighter1).getName() : (*fighter2).getName());
}