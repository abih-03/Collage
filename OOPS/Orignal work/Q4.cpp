#include <iostream>
#include <string>
using namespace std;
class Person
{
protected:
    string name;
    string address;
    string phone_no;
public:
    void getPersonDetails()
    {
        cout << "Enter Name: ";
        getline(cin, name);
        cout << "Enter Address: ";
        getline(cin, address);
        cout << "Enter Phone Number: ";
        getline(cin, phone_no);
    }
    void displayPersonDetails()
    {
        cout << "Name: " << name << endl;
        cout << "Address: " << address << endl;
        cout << "Phone Number: " << phone_no << endl;
    }
};
class Employee : public Person
{
protected:
    int eno;
    string ename;
public:
    void getEmployeeDetails()
    {
        cout << "Enter Employee Number: ";
        cin >> eno;
        cin.ignore(); // To consume newline
        cout << "Enter Employee Name: ";
        getline(cin, ename);
        getPersonDetails();
    }
    void displayEmployeeDetails()
    {
        cout << "Employee No: " << eno << endl;
        cout << "Employee Name: " << ename << endl;
        displayPersonDetails();
    }
};
class Manager : public Employee
{
private:
    string designation;
    string department;
    float basic_salary;
public:
    void getManagerDetails()
    {
        getEmployeeDetails();
        cout << "Enter Designation: ";
        getline(cin, designation);
        cout << "Enter Department Name: ";
        getline(cin, department);
        cout << "Enter Basic Salary: ";
        cin >> basic_salary;
        cin.ignore();
    }
    void displayManagerDetails()
    {
        displayEmployeeDetails();
        cout << "Designation: " << designation << endl;
        cout << "Department: " << department << endl;
        cout << "Basic Salary: " << basic_salary << endl;
        cout << "--------------------------\n";
    }
    float getSalary()
    {
        return basic_salary;
    }
};
int main()
{
    int n, choice;
    cout << "Enter number of managers: ";
    cin >> n;
    cin.ignore();
    Manager managers[100]; // Assuming max 100 managers
    bool running = true;
    while (running)
    {
        cout << "\n--- MENU ---\n";
        cout << "1. Accept Details of Managers\n";
        cout << "2. Display Manager with Highest Salary\n";
        cout << "3. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;
        cin.ignore();
        switch (choice)
        {
        case 1:
            for (int i = 0; i < n; i++)
            {
                cout << "\nEnter details for Manager " << i + 1 << ":\n";
                managers[i].getManagerDetails();
            }
            break;
        case 2:
        {
            if (n == 0)
            {
                cout << "No manager data entered.\n";
                break;
            }
            float maxSalary = managers[0].getSalary();
            int index = 0;
            for (int i = 1; i < n; i++)
            {
                if (managers[i].getSalary() > maxSalary)
                {
                    maxSalary = managers[i].getSalary();
                    index = i;
                }
            }
            cout << "\nManager with Highest Salary:\n";
            managers[index].displayManagerDetails();
            break;
        }
        case 3:
            running = false;
            break;
        default:
            cout << "Invalid choice. Try again.\n";
        }
    }
    return 0;
}
