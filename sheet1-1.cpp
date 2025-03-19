#include <iostream>
#include <string>
#include <queue>

using namespace std;

bool is_prime(int num) 
{
    if (num < 2) return false; 
    for (int i = 2; i * i <= num; i++) 
    {
        if (num % i == 0)
            return false;
    }
    return true;
}

string solve(string str, int N) 
{
    string s;
    priority_queue<string> qc; // Max Heap
    priority_queue<string, vector<string>, greater<string>> qp; 

    for (int i = 0; i < N; i++) 
    {
        if (is_prime((int)str[i])) 
            qp.push(string(1, str[i])); 
        else 
            qc.push(string(1, str[i])); 
    }

    while (!qp.empty()) 
    {
        s += qp.top();
        qp.pop();
    }

    while (!qc.empty()) 
    {
        s += qc.top();
        qc.pop();
    }

    return s;
}

int main() 
{
    string str = "Kkunjkhahorin";
    int N = str.length(); 
    cout << solve(str, N);
    return 0;
}
