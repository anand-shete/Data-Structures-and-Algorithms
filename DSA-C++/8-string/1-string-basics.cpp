#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    
    // create string is O(n) except creating empty string O(1)
    string string1;                     // empty string
    string string2("hey string2");
    string string3(3,'R');              // repeat characters
    string string4(string2);            // copied initalization
    string string5(string2,4,2);        // start from 4, copy 2 chars from string2
    
    
    // O(1) operations
    string str1 = "Namaste";
    // size of string
    cout << "length of str1: " << str1.size() << endl;

    // access characters
    cout << "char at index 3 in str1: " << str1[3] << endl;
    
    // check extremen chars
    cout << "last character of str1: " << str1.back() << endl;
    cout << "first character of str1: " << str1.front() << endl;

    // pop last char
    str1.pop_back();
    cout << "pop last element" << str1 << endl;

    // clear a string
    str1.clear();
    
    // check if empty string
    cout << "is str1 empty: " << str1.empty() << endl;

    // isalnum() returns true if the character is alpanumeric (a-z or A-Z or 1-9)
    cout << "check alphanumeric: " << isalnum('A') << endl;

    // isdigit returns true if char is a digit
    cout << "check digit: " << isdigit('3') << endl;

    // check casing
    cout << "is uppercase: " << isupper('A') << endl;
    cout << "is lowercase: " << islower('A') << endl;

    // convert casing
    cout << "to lowercase: " << char(tolower('A')) << endl;
    cout << "to uppercase: " << toupper('a') << endl << endl << endl;



    // O(n) operations
    string s1 = "Hello";
    string s2 = "World!";
    
    // push single char - fastest
    s1.push_back(' ');

    // push_back() for single char
    string s3 = "god is";
    cout << "using += : " << (s3+=' ') << endl;            // O(1)
    cout << "using += : " << (s3+="devil") << endl;        // O(n)
    

    // string compare
    string str2 = "hello";
    cout << "string comparison: " << (str2 == "Hello") << endl;
    cout << "lexographic comparison: " << (str2 < str1) << endl;        // compares ASCII values
    cout << endl;
    

    // substr(index,length)
    string demo1("anand_shete");
    string str3 = demo1.substr(3);

    cout << "string from index 3 to end: " << str3 << endl;
    string demo2("anand_shete");
    string str4 = demo2.substr(0,3);
    cout << "substring from idx 0, length 3: " << str4 << endl;


    // return first index occurence of a substring in O(n*m), typical O(n)
    string s34 = "friend";
    cout << "friend contains end at index: " << s34.find("end") << endl;
    // cout << "returns string::npos  " << s34.find("start") << endl;


    // erase a part of string
    string str5 = "Namaste India!";
    cout << "erase from idx 7 to end: " << str5.erase(7) << endl;
    cout << "erase from idx 0, 3 chars: " << str5.erase(0,3) << endl;


    // replace a part of string
    string str6 = "New string!";
    cout << "start from idx 4, replace next 6 chars: " << str6.replace(4, 6, "world") << endl;


    // int to string
    string s = to_string(4567);
    cout << "convert int to string: " << s << endl;

    // char to int
    cout << "convert char to int: " << '9'-'0' << endl;

    // string to int 
    cout << "can overflow int range: " << stoi("-23451") << endl;
    cout << "for single char to int conversion: " << '4'-'0' << endl;

    // resize a string
    str6.resize(6);
    cout << "after resize: " << str6 << endl << endl;
    

    // traverse a string
    for (int i=0; i<s3.size(); i++) {   
        cout << s3[i];
    } cout << endl;
    
    for (char x:s3) {
        cout << x;
    } cout << endl << endl;



    // reverse a string - O(n)
    string rev = "a man a plan";
    reverse(rev.begin()+4, rev.begin()+9);
    cout << "reverse from idx 4 to 8: " << rev << endl; 

    return 0;
}