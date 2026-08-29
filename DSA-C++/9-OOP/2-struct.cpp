#include <iostream>

using namespace std;

// In a struct, everything is public by default
struct User {
    string name;
    int age;
};

struct Calculator {
    string name;
    int age;

    Calculator (string name, int age) {
        this->name = name;
        this-> age = age;
    }
    int add(int a, int b) {
        return a+b;
    }

    string greet() {
        return "I am a caculator, my name is " + this->name + " and age " + to_string(this->age);
    }
};

int main() {
    User user1;
    user1.name = "Anand";
    user1.age = 22;
    
    // alternative init
    User user2 = {"Shiledar", 34};
    cout << "Hi, i am " << user2.name << " and i am " << user2.age << " years old" << endl;


    Calculator calc("Ayaan", 14);
    calc.add(4,5);
    cout << calc.greet() << endl;
    return 0;
}