/*
In object-orientated programming, classes contain member functions which can be declared 'virtual'. The ability to decide at runtime which virtual method should be invoked on any given object is termed 'polymorphism'.

Polymorphism is achieved by means of a 'Virtual Method Table', or v-table for short. Each object of a class contains the memory address of the v-table for the class. There is only one v-table for each class. If there are 11 objects in existence of the same class, all 11 objects contain the address of the same v-table. See more info on v-tables: https://shaharmike.com/cpp/vtable-part1/

Given a base class and two derived classes as follows:

class SerialNumber {
protected:
    long long unsigned num;

public:
    virtual void Print(void) = 0;
};

class DecimalSerialNumber : public SerialNumber {
public:
    void Print(void) override;
};

struct HexadecimalSerialNumber : public SerialNumber {
public:
    void Print(void) override;
};
Write a function called 'Alter_VTables' which alters the v-tables of the two classes:

DecimalSerialNumber
HexadecimalSerialNumber
so that the former will print in hexadecimal, and the latter will print in decimal. Specifically, you must locate the two v-tables in RAM, then find in each v-table the address of the 'Print' method. Once found, swap the two addresses.

On most operating systems, v-tables are stored in pages of memory which are readonly, and so a function is provided to you to change the permissions for the page of memory containing the v-tables:

void Set_Memory_Writeable(void*);
Hint to get you going:

The pointer to the v-table is located at the very start of the object
Language FeaturesObject-oriented Programming
*/
void Alter_VTables(void)
{
    DecimalSerialNumber d;
    HexadecimalSerialNumber h;
    void*** d_obj = reinterpret_cast<void***>(&d);
    void*** h_obj = reinterpret_cast<void***>(&h);
    void** d_vtable = *d_obj;
    void** h_vtable = *h_obj;
    Set_Memory_Writeable(d_vtable);
    Set_Memory_Writeable(h_vtable);
    std::swap(d_vtable[0], h_vtable[0]);
}