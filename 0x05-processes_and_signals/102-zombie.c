#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - loops infinitely
 *
 * Return: Always 0 - Success
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
 * main - Creates Zombie Process then sleeps 2 seconds
 *
 * Return: Always 0 - Success
 */
int main(void)
{
int pid, count;

for (count = 0; count < 5; count++)
{
pid = fork();
if (pid != 0)
{
printf("Zombie process created, PID: %d\n", pid);
}
else
return (0);
}
infinite_while();
return (0);
}
