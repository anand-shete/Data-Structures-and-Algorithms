### Create Node

```c++
Node* node = new Node(34);
```

Allocates memory on both heap and stack

**On Heap**

- OS reserves block of 16bytes physical RAM at memory address e.g. `0x10000`
- First 8 bytes store integer `34`
- Next 8 bytes store pointer to next node `0x0000`

**On stack**

- A variable named `node` is created to store address `0x10000`
- This is destroyed automatically after function ends

> In total, `24 bytes` are being used, `16 bytes` on heap memory and `8 bytes` in stack.

### Create pointer to node

```c++
Node* temp = node;
```

- Absolutely nothing is created in heap memory
- Allocates `8 bytes` of stack memory to store the address of node `0x10000`
- Memory address of node is copied to temp pointer.

### Delete a Node

```c++
delete temp;
```

- Computer goes to the memory address inside the **heap memory** `0x10000` and deletes that `16 byte` block
- Stack variables `node` and `temp` are still in stack memory pointing to illegal heap addresses.
