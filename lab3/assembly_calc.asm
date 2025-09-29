section .data
  msg1    db 'Addition RESULT: ',0  
  msg1Len equ $-msg1
	
  add_result db 0
  msg2    db 'Multiplication RESULT: ',0  
  msg2Len equ $-msg2
	
  mul_result db 0
section .text
  global _start
_start:
  mov al, 4
  mov bl, 2
  ; --- Addition ---
  add al, 2              ; AL = 6
  add al, '0'            ; convert to ASCII
  mov [add_result], al
  ; Multiplication
  mov al, 4             
  mul bl               
  add al, '0'            ; convert to ASCII
  mov [mul_result], al
  ; Print addition result
  mov eax,4
  mov ebx,1
  mov ecx,msg1
  mov edx,msg1Len
  int 0x80
  mov eax,4
  mov ebx,1
  mov ecx,add_result
  mov edx,1
  int 0x80
  ; Print multiplication result
  mov eax,4
  mov ebx,1
  mov ecx,msg2
  mov edx,msg2Len
  int 0x80
  mov eax,4
  mov ebx,1
  mov ecx,mul_result
  mov edx,1
  int 0x80
  ; Exit
  mov eax,1
  mov ebx,0
  int 0x80  
