from django import template 

register=template.Library()

# refer geekforgeeks.org generator function in python
# custom template tag for looping products by 3 each row

@register.filter(name='chunks')
def chunks(list_data, chunk_size):
    chunk=[]
    i=0
    for data in list_data:
        chunk.append(data)
        i=i+1
        if i==chunk_size:
            yield chunk
            i=0
            chunk=[]
    yield chunk
