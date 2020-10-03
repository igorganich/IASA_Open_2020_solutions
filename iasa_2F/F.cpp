#include <iostream>
#include <math.h>
#include <map>

using namespace std;

int *mas;
int *secmas;
int N;
long int *numbers;
char *table;
map<int, char> mapfirst;
map<int, char> mapsecond;
int sum;
char *firsttable;
char *secondtable;

int check_sum(int a, int b)
{
        long int suma = 0;
        long int sumb = 0;
        for (int i = 0; i < N; i++)
        {
                if ((a & (1 << i)) != 0)
                {
                        suma += numbers[i];
                }
                else if ((b & (1 << i)) != 0)
                {
                        sumb += numbers[i];
                }
        }
        return (suma == sumb);
}


void recur(int *mas, int i, int prev, int prevsum)
{
        if (i == N)
        {
		if (prev == 0)
			return;
		int index = prevsum % 25000000;
                if (secmas[index] != 0)
                {
                        if ((secmas[index] | prev) == (secmas[index] ^ prev))
                        {
                                if (check_sum(secmas[index], prev))
                                {
                                        cout << "YES\n";
                                        exit(0);
                                }
                        }
                }
                else
                        secmas[index] = prev;
		return ;
        }
        recur(mas, i + 1, prev ^ (0 << i), prevsum);
        recur(mas, i + 1, prev ^ (1 << i), prevsum + numbers[i]);
}

int main()
{
	cin >> N;
	numbers = new long int[N];
	table = new char[N];
	firsttable = new char[N];
	secondtable = new char[N];
	secmas = new int[50000000];
	secmas += 25000000;
	sum = 0;
	for (int i = 0; i < N; i++)
	{
		cin >> numbers[i];
		sum += numbers[i];
	}
	for (int i = 0; i < N - 1; i++)
	{
		for (int j = 0; j < N - i - 1; j++)
		{
			if (abs(numbers[j]) > abs(numbers[j + 1]))
			{
				long int temp = numbers[j];
				numbers[j] = numbers[j + 1];
				numbers[j + 1] = temp;
			}
			else if (abs(numbers[j]) == abs(numbers[j + 1]))
			{
				if (numbers[j] < numbers[j + 1])
				{
					long int temp = numbers[j];
					numbers[j] = numbers[j + 1];
	                                numbers[j + 1] = temp;
				}
			}
		}
	}
	for (int i = 0; i < N; i++)
	{
		mapfirst.insert(pair<int, char>(numbers[i], 0));
		mapsecond.insert(pair<int, char>(numbers[i], 0));
	}
	recur (mas, 0, 0, 0);
	cout << "NO" << endl;
	return (0);
}
