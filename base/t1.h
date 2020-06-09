#include <syscall.h>
#include <unistd.h>
#include <stdio.h>
#include <sys/types.h>
int main(void)
{
    long ID1, ID2;
    /*-----------------------------*/
    /* 直接系统调用*/
    /* SYS_getpid (func no. is 20) */
    /*-----------------------------*/
    ID1 = syscall(SYS_getpid);
    printf("syscall(SYS_getpid)=%ld/n", ID1);
    /*-----------------------------*/
    /* 使用"libc"封装的系统调用 */
    /* SYS_getpid (Func No. is 20) */
    /*-----------------------------*/
    ID2 = getpid();
    printf("getpid()=%ld/n", ID2);
    return (0);
}