
#pragma once
#include <iostream>
#include <vector>
#include <list>
#include <stack>
#include <algorithm>
#include "Graph.hpp"
using namespace std;
template <class N>
class AdjMatrixGraph: public Graph<N>  {
private:
    class NodeEntry {
    public:
        N node;
        int index;
    };
    const static int maxSize = 10;
    bool adjMatrix[maxSize][maxSize];
    NodeEntry *nodes[maxSize];
    int numNodes = 0;
    stack<N> addedNodes;
    int findNodeInMatrix(N x){
        for (int j=0; j < numNodes; ++j)
        {
            if (x == nodes[j]->node)
            {
                return j;
            }
        }
        return -1;
    }
public:
    // Default constuctor, create empty
    AdjMatrixGraph()
    {
        for(int i = 0; i < maxSize; i++)
            for (int j=0; j < maxSize; j++)
            {
                adjMatrix[i][j] = false;
            }
    }
    // Add the nodes in the list to graph
    AdjMatrixGraph(vector<N> newNodes, vector<pair<N,N>> newEdges)
    {
        for (const auto &node : newNodes) {
            addedNodes.push(node);
        }
        adjMatrix = new NodeEntry[maxSize][maxSize];
        for (typename vector<N>::const_iterator it = newNodes.begin();
             it < newNodes.end();
             ++it)
        {
            NodeEntry ne = new NodeEntry();
            ne.node = *it;
            ne.index = numNodes;
            nodes[numNodes] = ne;
        }
        for (typename vector<pair<N,N>>::const_iterator it = newEdges.begin();
             it < newEdges.end();
             ++it)
        {
            pair<N,N> edge = *it;
            int sourceIndex = findNodeInMatrix(edge.first);
            int destIndex = findNodeInMatrix(edge.second);
            if (sourceIndex != -1)
            {
                if (destIndex != -1)
                {
                    adjMatrix[sourceIndex][destIndex] = true;
                }
            }
        }
    }

    // Clean up behind ourselves
    ~AdjMatrixGraph() {};
    
    virtual bool adjacent(N x, N y)
    {
        bool result = false;
        int xIndex = findNodeInMatrix(x);
        int yIndex = findNodeInMatrix(y);
        if ((xIndex != -1) && (yIndex != -1))
        {
            bool xy = adjMatrix[xIndex][yIndex];
            bool yx = adjMatrix[yIndex][xIndex];
            result = xy && yx;
        }
        return(result);
    }

    virtual vector<N> neighbors(N x)
    {
        vector<N> *v = new vector<N>();
        int xIndex = findNodeInMatrix(x);
        if (xIndex != -1)
        {
            for (int i=0; i < numNodes; ++i) {
                if (adjMatrix[xIndex][i] == true) {
                    v->push_back(nodes[i]->node);
                }
            }
        }
        return *v;
    }
    virtual void addNode(N node)
    {
    
        if (find(addedNodes.begin(), addedNodes.end(), node) == addedNodes.end()) {
                
        NodeEntry *ne = new NodeEntry();
        ne->node = node;
        ne->index = numNodes;
        nodes[numNodes] = ne;
        numNodes++;

    }
    virtual void addEdge(N x, N y){
        int xIndex = findNodeInMatrix(x);
        int yIndex = findNodeInMatrix(y);
        if ((xIndex != -1) && (yIndex != -1))
        {
            adjMatrix[xIndex][yIndex] = true;
        }
    }
    virtual void deleteEdge(N x, N y)
    {
        int xIndex = findNodeInMatrix(x);
        int yIndex = findNodeInMatrix(y);
        adjMatrix[xIndex][yIndex] = false;
    }

    // Traversals
    void dfs(N startNode, std::function<void(N)> visit) {
        map<N, bool> visited;

         for (int i = 0; i < numNodes; ++i){
            visited[nodes[i]->node] = false;
        }
        stack<N> s;
        s.push(startNode);
        while (!s.empty()) {
            N currentNode = s.top();
            s.pop();
            bool beenVisited = visited[currentNode];
            if (!beenVisited) {
                visit(currentNode);
                visited[currentNode] = true;
            }
            vector<N> neighVec = neighbors(currentNode);
            for (auto neighbor: neighVec ) {
                if (!visited[neighbor]) { s.push(neighbor); }
            }
        }
    }
    
    void bfs(N startNode, std::function<void(N)> visit) {
        map<N, bool> visited;
        for (int i = 0; i < numNodes; ++i){
            visited[nodes[i]->node] = false;
        }
        queue<N> q;
        q.push(startNode);
        while (!q.empty()) {
            N currentNode = q.front();
            q.pop();
            bool beenVisited = visited[currentNode];
            if (!beenVisited) {
                visit(currentNode);
                visited[currentNode] = true;
            }
            vector<N> neighVec = neighbors(currentNode);
            for (auto neighbor: neighVec) {
                if (!visited[neighbor]) { q.push(neighbor); }
            }
        }
    }};