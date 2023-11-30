#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int max_value = 50 * 50;
    vector<vector<char>> white_chess = {{'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'}};

    vector<vector<char>> black_chess = {{'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'},
                                        {'B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'},
                                        {'W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'}};
    vector<vector<char>> my_chess;
    int arr_x, arr_y;
    int cnt;
    cin >> arr_x >> arr_y;
    my_chess.resize(arr_x);
    for (int i = 0; i < arr_x; i++)
    {
        my_chess[i].resize(arr_y);
    }
    for (int i = 0; i < arr_x; i++)
    {
        for (int j = 0; j < arr_y; j++)
        {
            cin >> my_chess[i][j];
        }
    }

    for (int i = 0; i < arr_x - 7; i++)
    {
        for (int j = 0; j < arr_y - 7; j++)
        {
            cnt = 0;
            for (int k = 0; k < 8; k++)
            {
                for (int l = 0; l < 8; l++)
                {
                    if (white_chess[k][l] != my_chess[i + k][j + l])
                    {
                        cnt++;
                    }
                }
            }
            if (cnt < max_value)
            {
                max_value = cnt;
            }

            cnt = 0;
            for (int k = 0; k < 8; k++)
            {
                for (int l = 0; l < 8; l++)
                {
                    if (black_chess[k][l] != my_chess[i + k][j + l])
                    {
                        cnt++;
                    }
                }
            }
            if (cnt < max_value)
            {
                max_value = cnt;
            }
        }
    }
    cout << max_value;
}