#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<char> tree[26];

void preorder(char c);
void inorder(char c);
void postorder(char c);

int main()
{
	int n;

	cin >> n;
	for (int i = 0; i < n; i++)
	{
		char parent, leftChild, rightChild;
		cin >> parent >> leftChild >> rightChild;
		tree[parent - 'A'].push_back(leftChild);
		tree[parent - 'A'].push_back(rightChild);
	}

	preorder('A');
	cout << "\n";
	inorder('A');
	cout << "\n";
	postorder('A');
	cout << "\n";
}

void preorder(char c)
{
	if (c == '.')
	{
		return;
	}
	cout << c;
	preorder(tree[c - 'A'][0]);
	preorder(tree[c - 'A'][1]);
}

void inorder(char c)
{
	if (c == '.')
	{
		return;
	}
	inorder(tree[c - 'A'][0]);
	cout << c;
	inorder(tree[c - 'A'][1]);
}

void postorder(char c)
{
	if (c == '.')
	{
		return;
	}
	postorder(tree[c - 'A'][0]);
	postorder(tree[c - 'A'][1]);
	cout << c;
}