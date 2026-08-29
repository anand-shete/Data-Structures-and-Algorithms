#include <iostream>
#include <bits/stdc++.h>

using namespace std;

// Brute force - O(n), O(n)
string reverse_words_of_string_1(string str) {
    // Given a string with spaces, reverse only the words of string
    vector <string> v;
    string temp = "";

    for (int i=0; i<str.size(); i++) {
        if (str[i] != ' ') {
            temp+=str[i];
        } 
        else if (str[i] == ' ' && temp != "") {
            v.push_back(temp);
            temp = "";
        }
    }

    if (!temp.empty()) {
        v.push_back(temp);
        temp="";
    }

    for (int i=v.size()-1 ; i>=0 ; i--) {
        temp+=v[i];
        if (i!=0) temp+=" ";
    }

    return temp;
}

// Two pointers - O(n), O(1)
string reverse_words_of_string_2(string str) {
    vector<string> words;
    string temp = "";

    for (int i=0; i<str.size();i++) {
        if (str[i] != ' ') {
            temp += str[i];
        } 
        else if (str[i] == ' ' && temp != "") {
            words.push_back(temp);
            temp = "";
        }
    }

    int left = 0, right = words.size() - 1;
    while (left < right) {
        swap(words[left], words[right]);
        left++;
        right--;
    }

    string result;
    for (const string& w : words) {
        if (!result.empty()) {
            result += " ";
        }
        result += w;
    }

    return result;
}


int main() {
    string str = " the sky is blue ";

    // cout << reverse_words_of_string_1(str);
    // cout << reverse_words_of_string_2(str) << endl; 

    cout <<endl;
    return 0;
}