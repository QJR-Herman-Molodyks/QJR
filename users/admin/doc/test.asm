
mov ax, "Hello, World!!!"
out ax

push ax
mov ax, "No"
out ax

pop ax
out ax

mov ax, 5
mov bx, 3
mov cx, 1
mov dx, "Hello, World!!!"

out "AX: "
out ax

out "BX: "
out bx

out "CX: "
out cx

out "DX: "
out dx

pusha

mov ax, 0
mov bx, 0
mov cx, 0
mov dx, 0

out ax
out bx
out cx
out dx

popa

out ax
out bx
out cx
out dx

