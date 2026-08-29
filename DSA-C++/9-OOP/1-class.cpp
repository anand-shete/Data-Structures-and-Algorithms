#include <bits/stdc++.h>

using namespace std;


// Everything is private by default in a class
class Calculator {
int priv = 34;       // private

public:
    string name = "Anand";

    int add(int a, int b) {
        return a+b;
    }

    int mul(int a, int b) {
        return a*b;
    }
};  // ; required


class AdvanceCalculator {
vector <int> ans;

public:
    string name;            // public members must be explicitly defined
    int age;

    AdvanceCalculator (string name, int age) {
        this-> name = name;
        this-> age = age;
    }
    int add(int a, int b) {
        cout << greet() << endl;
        cout << a << " + " << b << " gives ";
        return a+b;
    }

private:
    string greet() {
        return "I am a calculator, my name is " + this->name + " and I am " + to_string(this->age) + " years old";
    }
};


int main() {
    // create instance
    Calculator cal;
    cout << cal.add(4,5) << endl << endl;

    AdvanceCalculator advCal("nunu",24);
    cout << advCal.add(3,5) << endl;

    return 0;
}