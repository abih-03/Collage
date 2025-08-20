#include <iostream>
using namespace std;

class Number
{
private:
    int value;
public:
    // Constructor
    Number(int v = 0)
    {
        value = v;
    }
    // Overloading '*' operator
    Number operator*(const Number& obj) 
    {
        Number result;
        result.value = this->value * obj.value;
        return result;
    }
    void display()
    {
        cout << "Value: " << value << endl;
    }
};
int main()
{
    int a, b;
    cout << "Enter two numbers: ";
    cin >> a >> b;
    Number num1(a), num2(b);
    Number result;
    result = num1 * num2;  // Using overloaded '*' operator
    cout << "Result of multiplication ";
    result.display();
    return 0;
}
