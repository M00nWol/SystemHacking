#include "stdafx.h"
#include "Windows.h"

int _tmain(int argc, _TCHAR* argv[])
{
	__asm {
		// cmd
		mov		byte ptr[ebp - 4], 63h	// 'c'
		mov		byte ptr[ebp - 3], 6Dh	// 'm'
		mov		byte ptr[ebp - 2], 64h	// 'd'
		mov		byte ptr[ebp - 1], 0	// '\x0'
		// call WinExec('cmd', SW_SHOW)
		push	5						// SW_SHOW
		lea		eax, [ebp - 4]			// eax에 'cmd' 문자열 저장
		push	eax						// 스택에 'cmd' 문자열 주소 push
		mov		eax, 0x7FF9F2928600		// eax에 WinExec 함수 주소 저장
		call	eax						// WinExec 함수 실행
		// call ExitProcess(1)
		push	1
		mov		eax, 0x7FF9F28D7FA0
		call	eax
	};
}
