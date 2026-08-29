#include <bits/stdc++.h>

using namespace std;

// O(n²), O(1)
pair <int, int> repeated_and_missing_number_1(vector <int> nums) {
    // Given array of size n contains values from 1 to n
    // each value appears once, except for A which appears twice and B is missing
    // return result as an array where first element is A and second is B
    int n = nums.size(), repeated=-1, missing=-1;
    pair <int,int> ans;

    for (int i=0; i<n; ++i) {
        int count = 0;

        for (int j=0; j<n; ++j) {
            if (nums[j] == i+1) count++;
        }

        if (count == 2) repeated = i+1;
        else if (count == 0) missing = i+1;
    }

    return {repeated,missing};
}

// O(2*n), O(n)
pair <int, int> repeated_and_missing_number_2(vector <int> nums) {
    int repeated=-1, missing=-1;
    vector <int> hash(nums.size());
    
    for (int i=1; i<nums.size(); ++i) {
        hash[nums[i]-1]++;
    }

    for (int i=0; i<hash.size(); ++i) {
        if (hash[i] == 2) repeated = i+1;
        if (hash[i] == 0) missing = i+1;
    }

    return {repeated, missing};
}

// XOR approach - O(n), O(1)
vector<int> repeated_and_missing_number_3(vector<int>& nums) {
    int n = nums.size(); 
    int xr = 0;

    for (int i = 0; i < n; i++) {
        // XOR of all elements in nums
        xr = xr ^ nums[i]; 
        
        // XOR of numbers from 1 to n
        xr = xr ^ (i + 1);  
    }

    // Get the rightmost set bit in xr
    int number = (xr & ~(xr - 1));

    //Group the numbers based on the differentiating bit
    // Number that falls into the 0 group
    int zero = 0; 
    
    // Number that falls into the 1 group
    int one = 0;  

    for (int i = 0; i < n; i++) {
        
        /* Check if nums[i] belongs to the 1 group
        based on the differentiating bit*/
        if ((nums[i] & number) != 0) {
            
            // XOR operation to find numbers in the 1 group
            one = one ^ nums[i];
            
        } else {
            // XOR operation to find numbers in the 0 group
            zero = zero ^ nums[i]; 
        }
    }

    // Group numbers from 1 to n based on differentiating bit
    for (int i = 1; i <= n; i++) {
        
        /* Check if i belongs to the 1 group 
        based on the differentiating bit*/
        if ((i & number) != 0) {
            
            // XOR operation to find numbers in the 1 group
            one = one ^ i; 
            
        } else {
            // XOR operation to find numbers in the 0 group
            zero = zero ^ i; 
        }
    }

    // Count occurrences of zero in nums
    int cnt = 0; 

    for (int i = 0; i < n; i++) {
        if (nums[i] == zero) {
            cnt++;
        }
    }

    if (cnt == 2) {
        /*zero is the repeating number,
        one is the missing number*/
        return {zero, one}; 
    }
    
    /* one is the repeating number, 
    zero is the missing number*/
    return {one, zero}; 
}


int main() {
    vector <int> nums = {1, 2, 3, 6, 7, 5, 7};

    // auto [f,s] = repeated_and_missing_number_1(nums);
    // cout << f << " " << s;
    
    pair <int, int> p = repeated_and_missing_number_2(nums);
    cout << p.first << " " << p.second;

    cout << endl;
    return 0;
}