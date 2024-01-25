// William Romine
// 00103649
// Dr. Lewis CS472

//https://www.educative.io/answers/how-to-implement-dfs-in-cpp

#include "AdjMatrixGraph.hpp"
#include "AdjListGraph.hpp"
#include <chrono>
#include <iostream>

using namespace std;
using namespace std::chrono;

template <class N>
double measureDFSExecutionTime(Graph<N>& graph, N startNode) {
    auto start = high_resolution_clock::now();
    graph.dfs(startNode, [](N node) { /* DFS visit function, do nothing */ });
    auto stop = high_resolution_clock::now();
    auto duration = duration_cast<microseconds>(stop - start);
    return duration.count() / 1e6; // Convert to seconds
}

int main() {
    vector<int> graphSizes = {2, 8, 64, 256, 1024};

    double edgeProbability = 0.5;

    for (const auto& size : graphSizes) {
        AdjListGraph<int> adjListGraph = generateAdjListGraph(size, edgeProbability);
        cout << "AdjListGraph with " << size << " nodes:" << endl;
        double adjListTime = measureDFSExecutionTime(adjListGraph, 0);
        cout << "Depth First Search Execution Time: " << adjListTime << " seconds" << endl;

        AdjMatrixGraph<int> adjMatrixGraph = generateAdjMatrixGraphGraph(size, edgeProbability);
        cout << "AdjMatrixGraph with " << size << " nodes:" << endl;
        double adjMatrixTime = measureDFSExecutionTime(adjMatrixGraph, 0);
        cout << "Depth First Search Execution Time: " << adjMatrixTime << " seconds" << endl;

    }

    return 0;
}
