

open_file:
   mov     rsi, 0              ; flag for readonly access mode (O_RDONLY)
   mov     rdi, rcx            ; filename we want to open
   mov     rdx, 0666o          ; access flags
   mov     rax, 2              ; invoke SYS_OPEN (kernel opcode 2)
   syscall
   ret