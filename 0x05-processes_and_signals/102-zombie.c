#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

/**
 * infinite_while - runs an infinite loop for testing
 *
 * Return: always 0
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - entry point for program
 *
 * Return: always 0
 */
int main(void)
{
	int i = 0, pid;

	while (i < 5)
	{
		pid = fork();
		if (pid == -1)
			continue;
		else if (pid == 0)
			exit(0);
		else
			printf("Zombie process created, PID: %d\n", pid);
		i++;
	}
	infinite_while();
	return (0);
}
