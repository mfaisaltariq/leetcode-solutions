class DynamicArray(object):
    def __init__(self) -> None:
        self.index = 0
        self.capacity = 1

        self.array = self._create_array(self.capacity)
    
    def __len__(self):
        '''
            len(array) return the length of the array it will be the last known index
        '''
        return self.index

    def __getitem__(self, index):
        if not 0 <= index < self.index:
            return IndexError(f'Index {index} out of bound')
        else:
            return self.array[index]

    def __str__(self):
        return str(self.array[:self.index])

    def _create_array(self, new_capacity):
        return [None] * new_capacity

    def _resize(self, new_capacity):
        new_arr = self._create_array(new_capacity)

        for i in range(self.index):
            new_arr[i] = self.array[i]

        self.array = new_arr
        self.capacity = new_capacity
    
    def max_cap(self):
        '''
            max_cap() return the capacity of the array
        '''
        return self.capacity
    
    def is_empty(self):
        '''
            is_empty() returns True if empty else false
        '''
        if self.index == 0:
            return True
        else:
            return False

    def append(self, item):
        '''
            append(item) adds a new item at the end.
        '''

        if self.index == self.capacity:
            self._resize(2*self.capacity)

        self.array[self.index] = item
        self.index = self.index + 1
        
    
    def pop(self):
        ''' 
            pop() removes and returns the last item
        '''
        if self.index == 0:
            return IndexError('No items available to remove')
        else:
            el = self.array[self.index]
            self.array[self.index] = None
            self.index = self.index -1
            return el

    def insert_at(self, index, item):

        if index < 0 or index > self.index:
            return IndexError(f'Index {index} out of bound')

        if self.index == self.capacity:
            self._resize(2*self.capacity)
        print(self.index)
        for i in range(self.index - 1, index-1, -1):
            print(self.array, i)
            self.array[i+1] = self.array[i]

        self.array[index] = item
        self.index = self.index + 1

    def delete(self, index):

        if index < 0 or index > self.index:
            return IndexError(f'Index {index} out of bound')

        for i in range(index+1, self.index):
            self.array[i-1] = self.array[i]

        self.array[self.index] = None
        self.index = self.index - 1





arr = DynamicArray()
print(arr[3])
print(arr.pop())
arr.append(1)
arr.append(2)
arr.append(3)
arr.append(5)
print(arr.max_cap())
print(len(arr))
print(arr[2])
arr.insert_at(3,4)
arr.insert_at(0,0)
arr.delete(3)

print(arr)
        
    

    



