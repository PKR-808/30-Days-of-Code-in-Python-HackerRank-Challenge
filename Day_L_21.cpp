#include <iostream>
#include <vector>
#include <string>

using namespace std;

/**
*    Name: printArray
*    Print each element of the generic vector on a new line. Do not return anything.
*    @param A generic vector
**/
//I don't know why but python was not enabled in the Hackerrank code editor. So, I had to implement this using C++, which I didn't use for a long time.
// Write your code here
template <class T>
void printArray(vector<T> vect) {
    for (int i = 0; i < vect.size(); i++)
        cout << vect[i] << endl;
}


int main() {
	int n;
	
	cin >> n;
	vector<int> int_vector(n);
	for (int i = 0; i < n; i++) {
		int value;
		cin >> value;
		int_vector[i] = value;
	}
	
	cin >> n;
	vector<string> string_vector(n);
	for (int i = 0; i < n; i++) {
		string value;
		cin >> value;
		string_vector[i] = value;
	}

	printArray<int>(int_vector);
	printArray<string>(string_vector);

	return 0;
}
