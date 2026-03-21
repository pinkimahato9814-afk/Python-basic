# # # iterator and generatodef
# # from time import time


# # def generate(num = 5):
# #     while num > 0:
# #         print(f"executing for  #{num}")
# #         time.sleep(1)
# #         yield num # yeld is generatorator
# #         print(f"executing for  #{num}")
# #         num -= 1    


# # gene_obj = generate()
# # breakpoint()  # to check the value of gene_obj
# # item_1 = next(gene_obj)  # to get the value of gene_obj
# # print(item_1)
# # breakpoint()


# # import time

# # def generate(num=5):
# #     while num > 0:
# #         print(f"executing for #{num}")
# #         time.sleep(1)
# #         yield num
# #         print(f"executing for #{num}")
# #         num -= 1    

# # gene_obj = generate()

# # breakpoint()   # debugger starts here

# # item_1 = next(gene_obj)
# # print(item_1)

# # breakpoint()



# # from typing import Counter


# # class counter:
# #     def __init__(self, start,end):
# #         self.current = start
# #         self.end = end

# #     def __iter__(self):
# #         return self

# #     def __next__(self):
# #         if self.current > self.end:
# #             raise StopIteration
# #         else:
# #             self.current += 1
# #             return self.current - 1
        
# #  counter = Counter(1,5)       
            

# class Counter:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self

#     def __next__(self):
#         if self.current > self.end:
#             raise StopIteration
#         else:
#             self.current += 1
#             return self.current - 1


# counter = Counter(1, 5)

# # for i in counter:
# #     print(i)


# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))    
# print(next(counter))    
# print(next(counter))  
# 
#      
# numbers = [10, 20, 30,40,50,60]

# iterator = iter(numbers)

# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# #print(next(iterator))
# numbers = [1,2,3]

# for i in numbers:
#     print(i)

# iterator = iter(numbers)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)
# next(iterator)


class Count:
    
    def __init__(self, max):
        self.max = max
        self.current = 1
        
    def __iter__(self):
        return self
        
    def __next__(self):
        if self.current <= self.max:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
            

counter = Count(5)

for i in counter:
    print(i)


def my_generator():
    yield 1
    yield 2
    yield 3
    yield 4

g = my_generator()

print(next(g))
print(next(g))
print(next(g))
print(next(g))

