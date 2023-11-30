#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int T;
    string K;
    cin >> T;
    vector<string> lst;
    vector<string> new_lst;
    for (int i = 0; i < T; i++)
    {
        cin >> K;
        lst.push_back(K);
    }
    sort(lst.begin(), lst.end());
    for (int i = 1; i < 51; i++)
    {
        for (int j = 0; j < lst.size(); j++)
        {
            if (i == lst[j].size() && find(new_lst.begin(), new_lst.end(), lst[j]) == new_lst.end())
            {
                new_lst.push_back(lst[j]);
            }
        }
    }
    for (int i = 0; i < new_lst.size(); i++)
    {
        cout << new_lst[i] << endl;
    }
}