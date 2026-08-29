#include <iostream>
#include <climits>
#include <cstdint>  

// A namespace is a logical group that holds a set of identifiers like variables, functions, classes... to avoid name collisions that can occur when using different libraries.

// In C++, many standard library components like std::cout, std::cin, std::string, etc. are defined inside the std namespace.

using namespace std;

namespace std2 {
    int a = 30;
}

namespace std3 {
    int a = 20;
}

int main() {
    cout << "variable a from std2 namespace: " << std2::a << endl;
    cout << "variable a from std3 namespace: " << std3::a << endl << endl;


    // Defining a variable allocates memory
    int p; 		    

    // Define + Initialize (allocates memory and assigs value)
    int q = 20;		

    
    cout << "// INT ranges" << endl;
    cout << INT8_MIN << " to " << INT8_MAX <<  endl;
    cout << INT16_MIN << " to " << INT16_MAX << endl;

    // standard int
    cout << INT32_MIN << " to " << INT32_MAX << endl;
    
    // long long int use when exceeding  2 X 10⁹ input size
    cout << INT64_MIN << " to " << INT64_MAX << endl << endl;

     
    cout << "// Data Types" << endl;
    // The sizes of data types shown in data-types.png are typical but depend on the platform, compiler, and architecture
    int a = 27;
    float b = 45.67f;
    double c = 45.67;
    char d = 'x';
    bool e = false;    
    unsigned long f = 34;           // no sign bit is present, -ve no's cannot be respresented
    unsigned long long g = -69;     // c++ uses modulo arithmetic to convert -ve unsigned values to a large positive value
       
    cout<< "a=" << a << "\tsize is " << sizeof(a) << endl
        << "b=" << b << "\tsize is " << sizeof(b) << endl
        << "c=" << c << "\tsize is " << sizeof(c) << endl
        << "d=" << d << "\tsize is " << sizeof(d) << endl
        << "e=" << e << "\tsize is " << sizeof(e) << endl
        << "f=" << f << "\tsize is " << sizeof(f) << endl
        << "g=" << g << "\tsize is " << sizeof(g) << endl << endl;


    // Single quotes '' are used to represent single character literal (1 byte)
    char m = 'e';
    cout << "char variable m=" << m << endl;

    // double quotes "" are used to respresent only string
    string n = "hello, mam";
    cout << "string n=" << n << "\n\n";



    // const denotes constant values which cannot be modified
    const int x = 45;

    // auto automatically infers the type from value
    auto y = 46;



    cout << "// Typecasting" << endl;
    // Typecasting is the process of converting type of variable. 
    // Implicit typecasting is done by c++ internally
    int int1 = 34;
    float float1 = int1;
    cout << "float1=" << float1 << endl;

    // Explicit Typecasting is done by humans
    int int2 = 3;
    cout << "int2=" << int2 << " cast to " << static_cast<double>(int2) << endl << endl;




    cout << "// Scope of variables" << endl;
    // Variables defined inside a function or a block have local scope. 
    if(1) {
        int z = 34;
        cout << "z="<< z << endl;
    }
    
    // Variables defined outside any function or block have global scope.
    int r = 2;


    // size_t operator only stores 0 and positive integers
    size_t t = 0.3;
    cout << "size_t operator: " << t << endl;

    return 0;
}
