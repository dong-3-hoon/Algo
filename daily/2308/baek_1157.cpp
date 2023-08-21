#include <iostream>
#include <map>
#include <string>
using namespace std;

int main()
{
    string str;
    map<char, int> tmp;
    // 여기서 char형식이 아닌 string형식을 사용해서 count가 안됐음
    cin >> str;
    for (int i = 0; i < str.length(); i++)
    {
        str[i] = toupper(str[i]);
        if (tmp.count(str[i]) == 1)
        {
            tmp[str[i]] += 1;
        }
        else
        {
            tmp[str[i]] = 1;
        }
    }
    int n = -1;
    char c;
    for (const auto &pair : tmp)
    {
        if (pair.second > n)
        {
            n = pair.second;
            c = pair.first;
        }
    }
    int cnt = 0;
    for (const auto &pair : tmp)
    {
        if (pair.second == n)
        {
            cnt++;
        }
    }
    if (cnt > 1)
    {
        cout << '?';
    }
    else
    {
        cout << c;
    }
}