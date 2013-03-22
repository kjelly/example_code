#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int main(){
    vector<int> v = {1, 2, 3, 4, 5};
    int data = 3;
    int counter = 0;
    for_each(v.begin(), v.end(), [data, &counter](int s) -> int{
      counter += 1;
      cout << s * data << endl;
    });
    cout << "counter: " << counter << endl;
    return 0;
}
