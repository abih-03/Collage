#include <iostream>
using namespace std;
// Publisher class
class Publisher 
{
protected:
    string title;
public:
    void getPublisherData() 
    {
       // cout << "Enter Title Name: ";
        getline(cin, title);  // Properly takes full line input
    }
    void displayPublisherData() 
    {
        cout << "Title: " << title << endl;
    }
};
// Sales class
class Sales 
{
protected:
    int numberOfSales;
public:
    void getSalesData()
    {
        cout << "Enter Number of Sales: ";
        cin >> numberOfSales;
    }
    void displaySalesData() 
    {
        cout << "Number of Sales: " << numberOfSales << endl;
    }
};
// Book class using multiple inheritance
class Book : public Publisher, public Sales 
{
public:
    void getBookData() 
    {
        getPublisherData();   // Input title first
        getSalesData();       // Then input sales
    }
    void displayBookData() 
    {
        cout << "\n--- Book Details ---" << endl;
        displayPublisherData();
        displaySalesData();
    }
};
// Main function
int main() 
{
    Book b;
    // Fix: Clear input buffer before getline
    cout << "Enter title name:\n";
    b.getBookData();
    b.displayBookData();
    return 0;
}
