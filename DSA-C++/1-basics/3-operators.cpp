#include <iostream>
#include <math.h>

int convert_to_base2();
int convert_to_base10();


using namespace std;
int main() {
    // The insertion operator (<<) is used to send data to an output stream, which is often the console but can also be a file or a network connection.
    cout << "Hello" << endl;

    // Extraction operator (>>) is used to read data from an input stream, such as the keyboard, and store it in a variable
    // int t;
    // cin >> t;



    // Arithmetic Operators
    int a = 3;
    int b = 5;
    cout << "a+b = " << a+b << endl;
    cout << "a-b = " << a-b << endl;
    cout << "a*b = " << a*b << endl;
    cout << "a/b = " << a/b << endl;
    cout << "a%b = " << a%b << endl << endl;
    
    

    // Comparison (relational) operators return True or false. 
    // C++ internally converts boolean to integers.
    cout << "a==b " << (a==b) << endl;
    cout << "a!=b " << (a!=b) << endl;
    cout << "a>b " << (a>b) << endl;
    cout << "a<b " << (a<b) << endl;
    cout << "a<=b " << (a<=b) << endl;
    cout << "a>=b " << (a>=b) << endl << endl;
    
 

    // Logical operators always return either 0 or 1
    // && returns true, if both true
    cout << "Logical AND: "<< (5 && 10) << endl;
    // || returns false if both false
    cout << "Logical OR: "<< (5 || 10) << endl;
    // ! Logical NOT negates given operand
    cout << "Logical NOT: "<< (!67) << endl << endl;
    
    


    // Operations involving bitwise operator return any integer.
    // Bitwise AND operator (&) returns result of 1 if both the bits at same position are 1.
    cout << "Bitwise AND: " << (8 & 1) << endl;

    // Bitwise OR (|) returns 0 if both bits at same position are 0
    cout << "Bitwise OR: " << (8 | 0) << endl;

    // Bitwise XOR (^) returns 0 if both operands are same. 
    cout << "Bitwise XOR: " << (6^0) << endl;

    // Bitwise NOT (~) operator flips every bit in the operand’s binary representation. For unsigned integers, this simply inverts the bits. For signed integers (two’s complement), it produces the value -(x + 1).
    cout << "Bitwise NOT: " << (~5) << ", another eg. " << (~-6) << endl;

    // Bitwise Left shift (<<) shifts bits to left by n places and add zeroes
    // Left shift multiplies the number by 2^n where n is numver of bits shifted
    cout << "<< 3 by 4 bits:  " << (3 << 4) << endl; 
    cout << "<< -3 by 1 bits: " << (-3 << 1) << endl;

    // Bitwise Right shift (>>) operator shifts the bits to the right, and any bits that overflow are discarded
    cout << ">> 3 by 1 bits: " << (3 >> 1) << endl << endl;

    

    
    // 5. Assignment Operators
    // These are used as a shorthand for arithmetic operations
    // = Simple assignment
    // +=  Addition assignment
    // -=  Subtraction assignment
    // *=  Multiplication assignment
    // /=  Division assignment
    // %=  Modulus assignment
    // &=  Bitwise AND assignment
    // |=  Bitwise OR assignment
    // ^=  Bitwise XOR assignment
    // <<= Left shift assignment
    // >>= Right shift assignment
    int p = 3;
    p+=5;
    cout << p << endl;


    
    // 6. Increment/Decrement operators increase or decrease value of variable by one
    int x = 6;
    int y = 6;
    cout << "increment and return: " << ++x << endl;    // slightly faster because no copy created
    cout << "return and increment: " << y++ << endl;



    // 7. Conditional (Ternary) Operator
    string result = (1==0) ? "yes": "no";
    cout << result << "\n\n\n";
    return 0;
}