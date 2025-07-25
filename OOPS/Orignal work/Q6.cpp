#include <iostream>
using namespace std;

class Weight
{
private:
    int kg;
    int gram;
public:
    // Constructor that accepts kg and gram
    Weight(int k, int g)
    {
        int totalGrams = k * 1000 + g;
        kg = totalGrams / 1000;
        gram = totalGrams % 1000;
    }
    // Static method to create object from total grams
    static Weight fromGrams(int totalGrams)
    {
        int k = totalGrams / 1000;
        int g = totalGrams % 1000;
        return Weight(k, g);
    }
    void display()
    {
        cout << "Weight: " << kg << " kg and " << gram << " gram" << endl;
    }
};
int main()
{
    int choice;
    cout << "1. Enter weight as Kg and Gram\n";
    cout << "2. Enter weight as total Grams\n";
    cout << "Enter your choice: ";
    cin >> choice;
    if (choice == 1)
    {
        int kg, g;
        cout << "Enter Kilograms: ";
        cin >> kg;
        cout << "Enter Grams: ";
        cin >> g;
        Weight w(kg, g);
        w.display();
    } else if (choice == 2)
    {
        int totalGrams;
        cout << "Enter total grams: ";
        cin >> totalGrams;
        Weight w = Weight::fromGrams(totalGrams);
        w.display();
    } else
    {
        cout << "Invalid choice." << endl;
    }
    return 0;
}
