#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <array>
#include <algorithm>
#include <utility>
#include <map>
#include <queue>
#include <set>
#include <cmath>
#include <cstdio>
#include <cstring>
#include <functional>
#include <numeric>

using namespace std;

#define int int64_t

struct State {
    pair<int, int> curr_beam_loc;
    vector<pair<int, int>> G;
    bool operator<(State const& other) const {
        if (curr_beam_loc != other.curr_beam_loc) {
            return curr_beam_loc < other.curr_beam_loc;
        }
        return G < other.G;
    }
};

int32_t main(){
    string S;
    vector<string> G;
    while(cin >> S){
        G.push_back(S);
    }

    int N = int(G.size());
    int M = int(G[0].size());

    // find start
    std::pair<int, int> start_loc = {-1, -1};
    for(int r = 0; r < N; ++r){
        for(int c = 0; c < M; ++c){
            if(G[r][c] == 'S'){
                start_loc = {r, c};
            }
        }
    }    

    vector<vector<int>> freq(N, vector<int>(M, 0));
    freq[start_loc.first][start_loc.second] = 1; 
    auto valid = [&](int x, int y) -> bool{
        {};
        if(x < 0 or x >= N or y < 0 or y >= M){
            return false;
        } 
        return true;
    };
    
    int curr_row = start_loc.first;
    for(int iter = 0;;){
        // check if its valid 
        if(curr_row >= N){
            break;
        }
        int ret = 0;
        for(int c = 0; c < M; ++c){
            ret += freq[curr_row][c];
            if(freq[curr_row][c] > 0){
                int nx = curr_row + 1;
                int ny = c;
                if(valid(nx, ny)){
                    if(G[nx][ny] == '^'){
                        int nx1 = nx, ny1 = ny - 1;
                        int nx2 = nx, ny2 = ny + 1;
                        if(valid(nx1, ny1)){
                            freq[nx1][ny1] += freq[curr_row][c];
                        }
                        if(valid(nx2, ny2)){
                            freq[nx2][ny2] += freq[curr_row][c];
                        }   
                    } else{
                        freq[nx][ny] += freq[curr_row][c];
                    }
                }
            }
        }
        cout << iter++ << " " << ret << "\n";
        curr_row++;
    }
    int res = 0;
    for(int i = 0; i < M; ++i){
        res += freq[N-1][i];
    }
    cout << res << "\n";

}