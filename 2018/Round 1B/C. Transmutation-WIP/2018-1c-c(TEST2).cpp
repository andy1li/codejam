#include <iostream>
#include <numeric> 
#include <string>
#include <vector>

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;

template <typename T>
void print(T &&x) {
    cout << x << endl;
}

template <typename T>
void print_1d(vector<T> &vector) {
    for (int i = 0; i < vector.size(); ++i) {
        cout << vector[i] << ' ';
    }
    cout << endl;
}

template <typename T>
void print_2d(vector<vector<T>> &grid) {
    for (int row = 0; row < grid.size(); ++row) {
        for(int col = 0; col < grid[row].size(); ++col)
            cout << grid[row][col] << ' ';
        cout << endl;
    }
}

template <typename T>
T sum(vector<T> &vector) {
    return accumulate(vector.begin(), vector.end(), 0);
}

bool check(int m, VVI &recipes, VI &have, int sum_have, int target) {
    if (have[0] >= target)
        return true;

    VI need(m, 0); need[0] = target;
    int sum_need = sum(need);

    // print_1d(need);

    while (sum_need <= sum_have) {
        bool OK;

        for (int i = 0; i < m; ++i) {
            if (i == 0) OK = true;

            if (need[i] > have[i]) {
                int gap = need[i] - have[i];

                need[i] -= gap;
                need[recipes[i][0]] += gap;
                need[recipes[i][1]] += gap;

                sum_need += gap;
                OK = false;
            }
        }
        if (OK) return true;
    }
    return false;
}

int main() {
    // Remember to delete "reopon" before submission
    freopen("sample.in", "r", stdin);

    int num_cases; cin >> num_cases;

    for (int case_i = 1; case_i < num_cases+1; ++case_i) {
        int m; cin >> m;
        // print(m);

        // read recipes
        VVI recipes;
        for (int m_i = 0; m_i < m; ++m_i) {
            int r1, r2;
            cin >> r1 >> r2;  
            recipes.push_back( {r1-1, r2-1} );
        }
        // print_2d(recipes);

        // read metals
        VI metals(m);
        for (int m_i = 0; m_i < m; ++m_i) {
            int metal; cin >> metal;  
            metals[m_i] = metal;
        }
        // print_1d(metals);

        // binary search
        int lo = 0;
        int hi = sum(metals);

        while (lo <= hi) {
            int mid = (lo + hi) / 2;
            // cout << "checking: "<< lo << ' ' << mid << ' ' << hi << endl; 

            if (check(m, recipes, metals, sum(metals), mid)) {
                lo = mid + 1;
            } else {
                hi = mid - 1;
            }                
        }

        
        cout << "Case #" << case_i << ": " << lo-1 << endl;
    }

    return 0;
}