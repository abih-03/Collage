#include <iostream>
using namespace std;
// Base class
class Student
{
protected:
    int rollno;
    string name;
    int age;

public:
    void getStudentData()
    {
        cout << "Enter Roll No: ";
        cin >> rollno;
        cin.ignore();  // to clear input buffer
        cout << "Enter Name: ";
        getline(cin, name);
        cout << "Enter Age: ";
        cin >> age;
    }

    void displayStudentData()
    {
        cout << "\nRoll No: " << rollno << endl;
        cout << "Name: " << name << endl;
        cout << "Age: " << age << endl;
    }
};
// Derived class
class Result : public Student
{
private:
    int mark1, mark2, mark3;

public:
    void getMarks()
    {
        cout << "Enter Mark 1: ";
        cin >> mark1;
        cout << "Enter Mark 2: ";
        cin >> mark2;
        cout << "Enter Mark 3: ";
        cin >> mark3;
    }

    void displayResult()
    {
        int total = mark1 + mark2 + mark3;
        float average = total / 3.0;
        displayStudentData();
        cout << "Marks: " << mark1 << ", " << mark2 << ", " << mark3 << endl;
        cout << "Total: " << total << endl;
        cout << "Average: " << average << endl;
    }
};
// Main function
int main()
{
    Result r;
    r.getStudentData();
    r.getMarks();
    r.displayResult();

    return 0;
}
