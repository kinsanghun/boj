#include <iostream>
#include <string>

using namespace std;

template <typename T> class customStak;
template <typename T>
class Node
{
	friend class customStak<T>;
private:
	Node<T>* next;
	Node<T>* prev;
	T data;

public:
	Node()
	{
		next = nullptr;
		prev = nullptr;
	}
	Node(T d) :data(d) {};


};

template <typename T>
class customStak
{
private:
	Node<T>* head;
	Node<T>* tail;
	Node<T>* cur;
	int sizeVal;

public:
	customStak()
	{
		head = new Node<T>();
		tail = new Node<T>();
		head->next = tail;
		tail->prev = head;
		cur = head;
		sizeVal = 0;
	}
	void push(T X)
	{
		Node<T>* newNode = new Node<T>(X);
		if (this->empty())
		{
			head->next = newNode;
			newNode->prev = head;
			tail->prev = newNode;
			newNode->next = tail;
		}
		else
		{
			Node<T>* leftNode = tail->prev;
			leftNode->next = newNode;
			newNode->prev = leftNode;
			tail->prev = newNode;
			newNode->next = tail;
		}
		sizeVal++;
	}
	T pop()
	{
		Node<T>* delNode = tail->prev;
		if (this->empty())
		{
			return -1;
		}
		Node<T>* leftNode = delNode->prev;
		leftNode->next = tail;
		tail->prev = leftNode;
		T data = delNode->data;
		delete delNode;
		sizeVal--;
		return data;
	}

	bool empty()
	{
		if (this->size() == 0)
		{
			return 1;
		}
		return 0;
	}

	T top()
	{
		if (this->empty())
		{
			return -1;
		}
		return tail->prev->data;
	}

	int size()
	{
		return sizeVal;
	}

	void print()
	{
		Node<T>* curNode = head->next;
		while (curNode != tail)
		{
			cout << curNode->data;
			curNode = curNode->next;
		}
	}
};

int priority(char c)
{
	if (c == '*' || c == '/')
	{
		return 3;
	}
	else if (c == '+' || c == '-')
	{
		return 2;
	}
	else
	{
		return 1;
	}
}

int main()
{
	customStak<char> sign;
	string str;
	cin >> str;
	for (int i = 0; i < str.size(); i++)
	{
		if ('A' <= str[i] && str[i] <= 'Z')
		{
			cout << str[i];
		}
		else if (sign.empty() || str[i] == '(')
		{
			sign.push(str[i]);
		}
		else if (str[i] == ')')
		{
			while (true)
			{
				if (sign.top() == '(')
				{
					sign.pop();
					break;
				}
				cout << sign.pop();
			}
		}
		else if (priority(sign.top()) >= priority(str[i]))
		{
			while (priority(sign.top()) >= priority(str[i]))
			{
				cout << sign.pop();
			}
			sign.push(str[i]);
		}
		else
		{
			sign.push(str[i]);
		}
	}
	while (!sign.empty())
	{
		cout << sign.pop();
	}
}