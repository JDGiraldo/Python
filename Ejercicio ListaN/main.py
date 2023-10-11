from lists import SimplyLinkedList

#Crear el objeto. copia o instancia de la casle SimplyLikedList
lista = SimplyLinkedList()

for i in range(3):
    nums = list(map(int, input().split()))
    if i == 0:
        for valor in nums:
            lista.InsertFirst(valor)
    elif i== 1:
        for valor in nums:
            lista.InsertFirst(valor)
    else:
        lista.Insert(nums[0],nums[1])
lista.Show()