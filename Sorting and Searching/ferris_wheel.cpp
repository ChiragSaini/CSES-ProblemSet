#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main()
{
    ll n, x;
    cin >> n >> x;
    vector<ll> v;
    for (int i = 0; i < n; i++)
    {
        cin >> v[i];
    }
    ll ptr = 0;
    ll res = 0;
    while (ptr < n)
    {
        if (v[ptr] + v[ptr] <= x)
        {
            res++;
            ptr += 2;
        }
        else
        {
            res++;
            ptr++;
        }
    }
    cout << res << "\n";
    return 0;
}