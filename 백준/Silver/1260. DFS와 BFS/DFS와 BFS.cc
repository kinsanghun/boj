#include <iostream>
#include <vector>
#include <stack>
#include <queue>
#include <algorithm>

using namespace std;

vector<int> g[1001];
bool visit[1001];

void clearVar()
{
	for (int i = 0; i < 1001; i++)
	{
		visit[i] = false;
	}
}

void dfs(int v)
{
	if (visit[v])
	{
		return;
	}
	visit[v] = true;
	cout << v << " ";
	for (int i = 0; i < g[v].size(); i++)
	{
		dfs(g[v][i]);
	}
}

void bfs(int v)
{
	queue<int> q;
	q.push(v);
	visit[v] = true;

	while (!q.empty())
	{
		int cur = q.front();
		cout << cur << " ";
		q.pop();

		for (int i = 0; i < g[cur].size(); i++)
		{
			if (!visit[g[cur][i]])
			{
				q.push(g[cur][i]);
				visit[g[cur][i]] = true;
			}
		}
	}
}

int main()
{
	int n, m, v;

	cin >> n >> m >> v;

	for (int i = 0; i < m; i++)
	{
		int v1, v2;
		cin >> v1 >> v2;
		
		g[v1].push_back(v2);
		g[v2].push_back(v1);
	}

	for (int i = 1; i <= n; i++)
	{
		sort(g[i].begin(), g[i].end());
	}

	dfs(v);
	clearVar();
	cout << "\n";
	bfs(v);
}