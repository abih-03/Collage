#include <iostream>
using namespace std;
// Base class
class Base
{
public:
    virtual void show()
    {
        cout << "Base class show() function called." << endl;
    }
};
// Derived class
class Derived : public Base
{
public:
    void show() override
    {
        cout << "Derived class show() function called." << endl;
    }
};
int main()
{
    Base* basePtr;         // Pointer of base class
    Base baseObj;          // Object of base class
    Derived derivedObj;    // Object of derived class
    // Pointing to base class object
    basePtr = &baseObj;
    basePtr->show();       // Calls Base class version
    // Pointing to derived class object
    basePtr = &derivedObj;
    basePtr->show();       // Calls Derived class version due to virtual function
    return 0;
}
