// William Romine
// 00103649
// Dr. Lewis CS472

#include <iostream>
#include <algorithm>
#include <vector>
#include <ctime>

using namespace std;

void randDataSet(vector<int>& dataSet, int size) {
    dataSet.clear();
    for (int i = 0; i < size; ++i) {
        dataSet.push_back(rand() % 10000);
    }
}

int main() {
    const int AmtRuns = 10;
    vector<int> dataSetSizes = {5, 10, 50, 100, 500, 1000, 5000, 10000};

    cout << "Data Size\tAverage Run Time (ms)" << endl;

    for (int size : dataSetSizes) {
        double totRunTime = 0;

        for (int runNumber = 0; runNumber < AmtRuns; ++runNumber) {
            vector<int> dataSet;
            randDataSet(dataSet, size);

            clock_t startTime = clock();
            sort(dataSet.begin(), dataSet.end());
            clock_t endTime = clock();

            double totTime = double(endTime - startTime) / CLOCKS_PER_SEC * 1000;
            totRunTime += totTime;
        }

        double avgRunTime = totRunTime / AmtRuns;
        cout << size << "\t\t" << avgRunTime << endl;
    }

    return 0;
}
