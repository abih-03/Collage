#include <iostream>
using namespace std;
// Base class
class Student 
{
protected:
    string name;
    int rollNo;
public:
    // Constructor
    Student(string n, int r) 
    {
        name = n;
        rollNo = r;
    }
    // Display common student details
    void displayStudent() 
    {
        cout << "Name: " << name << endl;
        cout << "Roll No: " << rollNo << endl;
    }
};
// Derived class - Arts
class Arts : public Student 
{
public:
    // Constructor
    Arts(string n, int r) : Student(n, r) {}
    // Display subject
    void displaySubjects() 
    {
        displayStudent();
        cout << "Subjects: History, Political Science, Sociology" << endl;
    }
};
// Derived class - Science
class Science : public Student 
{
public:
    // Constructor
    Science(string n, int r) : Student(n, r) {}
    void displaySubjects() 
    {
        displayStudent();
        cout << "Subjects: Physics, Chemistry, Mathematics" << endl;
    }
};
// Derived class - Commerce
class Commerce : public Student 
{
public:
    // Constructor
    Commerce(string n, int r) : Student(n, r) {}
    void displaySubjects() 
    {
        displayStudent();
        cout << "Subjects: Accounting, Economics, Business Studies" << endl;
    }
};
// Main function
int main() 
{
    // Creating objects of each derived class
    Arts a("Raj", 101);
    Science s("Priya", 102);
    Commerce c("Amit", 103);

    cout << "\n--- Arts Student ---\n";
    a.displaySubjects();
    cout << "\n--- Science Student ---\n";
    s.displaySubjects();
    cout << "\n--- Commerce Student ---\n";
    c.displaySubjects();
    return 0;
}
