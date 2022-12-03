; ----------------------------------------------------------------------------------------
;     system call table for x64 - https://blog.rchapman.org/posts/Linux_System_Call_Table_for_x86_64/
;     ascii table https://www.asciitable.com/
;     nasm -f elf64 -gdwarf -o task_1.o task_1.asm && ld -o task_1 task_1.o && gdb task_1
;
;
;
; useful GDB commands
; layout asm - to see assembly listing
; x/10c <address> to print first 10 values by address as chars
; ----------------------------------------------------------------------------------------
bits 64
default rel

SECTION     .data

path:   db  "input.txt", 0

error_msg1 db "couldn't open file", 0xa, 0
error_msg1_len equ $-error_msg1

out_message db "result is %d", 0xa, 0

max_callories dq 0
curr_callories dq 0

SECTION .bss

buffer resb 65536             ; zero initialized buffer

SECTION   .text

global      _start
extern      printf

_start: 
   mov     rsi, 0              ; flag for readonly access mode (O_RDONLY)
   mov     rdi, path           ; filename we want to open
   mov     rdx, 0666o          ; access flags
   mov     rax, 2              ; invoke SYS_OPEN (kernel opcode 2)
   syscall


   test    rax, rax            ; check for error and jump to error handler if so
   js      error_open

   ; read content
   mov      rdx, 65536          ; number of bytes to read
   mov      rsi, buffer         ; memory address of buffer
   mov      rdi, rax            ; file handle from previous kernell call stored in rax
   mov      rax, 0              ; invoke SYS_READ
   syscall

   mov      rdi, rsi            ; move buffer address  

next_elf:
   mov      r8, [curr_callories]
   mov      r9, [max_callories]
   
   cmp      r8, r9
   jl       cont
   
   mov      [max_callories], r8
cont:
   mov      dword [curr_callories], 0
current_elf:
   call     atoi
   add      rax, [curr_callories]
   mov      [curr_callories], rax

   inc      rdi
   movzx    rsi, byte [rdi]
   cmp      rsi, 10
   je       next_elf

   test     rsi, rsi              ; test for \0  
   je       quit

   jmp      current_elf

quit:

   ; mov     rdx, [max_callories]
   ; lea     rcx, [out_message]
   ; call    printf

   mov     ebx, 0
   mov     eax, 1
   int     80h
   ret


error_open:
   mov rax,1                    ; sys_write 
   mov rdi,1                    ; File descriptor 1, stdout
   mov rsi, error_msg1          ; Pass offset of message
   mov rdx, error_msg1_len      ; Length of error message
   syscall 
    
   call quit


atoi:
   mov rax, 0              ; Set initial total to 0
     
convert:
   movzx rsi, byte [rdi]   ; Get the current character
   
   cmp rsi, 10             ; Check for \n as numbers are delimited by \n
   je done

   test rsi, rsi           ; check for \0  (end of data)
   je done
    
   cmp rsi, 48             ; Anything less than 0 is invalid
   jl error
    
   cmp rsi, 57             ; Anything greater than 9 is invalid
   jg error
     
   sub rsi, 48             ; Convert from ASCII to decimal 
   imul rax, 10            ; Multiply total by 10
   add rax, rsi            ; Add current digit to total
    
   inc rdi                 ; Get the address of the next character
   jmp convert             ; repeat

error:
   mov rax, -1             ; Return -1 on error
 
done:
   ret