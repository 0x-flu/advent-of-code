#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int main() {
	ifstream input_file("../input.txt");
	
	vector<int> col1;
	vector<int> col2;
	int num1, num2;

	while (input_file >> num1 >> num2) {
		col1.push_back(num1);
		col2.push_back(num2);
	}
	input_file.close();

	sort(col1.begin(), col1.end());
	sort(col2.begin(), col2.end());
	
	int sum1 = 0;
	int sum2 = 0;
	for (int i = 0; i < col1.size(); i++) {
		sum1 += abs(col1[i] - col2[i]);
	}
	cout << "The sum distance of part I: \n";
	cout << sum1 << endl;

	for (int i = 0; i < col1.size(); i++) {
		for (int j = 0; j < col2.size(); j++) {
			if (col1[i] == col2[j]) {
				sum2 += col1[i];
			}
		}
	}

	cout << "The sum distance of part II: \n";
	cout << sum2 << endl;
	return 0;
}
