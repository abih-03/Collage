#include <iostream>
using namespace std;

class Student
{
private:
    int rollNo;
    string name;
public:
    void getData()
    {
        cout << "Enter Roll Number: ";
        cin >> rollNo;
        cin.ignore(); // Clear newline from buffer
        cout << "Enter Name: ";
        getline(cin, name);
    }
    void displayData()
    {
        cout << "Roll Number: " << rollNo << endl;
        cout << "Name: " << name << endl;
    }
};
int main()
{
    Student s1;          // Create object
    Student* ptr;        // Declare pointer to object
    ptr = &s1;           // Assign address of object to pointer
    cout << "Enter student details\n";
    ptr->getData();      // Access using pointer
    cout << "\nStudent details are:\n";
    ptr->displayData();  // Access using pointer
    return 0;
}
