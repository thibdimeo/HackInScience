import textwrap
import itertools
def sidebyside(left,right,width=79):
    width = round((width+1)/2)
    leftwrapped = textwrap.wrap(left,width = width)
    
    for i in range(0,len(leftwrapped)):
        leftwrapped[i] = leftwrapped[i].ljust(width)
    
    rightwrapped = textwrap.wrap(right,width = width)
    
    for i in range(0,len(rightwrapped)):
        rightwrapped[i] = rightwrapped[i].ljust(width)
    
    pipes = ["|"]*max(len(leftwrapped),len(rightwrapped))
    
    paragraph = itertools.zip_longest(leftwrapped,pipes,rightwrapped, fillvalue="".ljust(width))
    result = ""
    for a in paragraph:
        result = result + a[0] + a[1] + a[2] + "\n"
    
    return(result)


left = (
"Lorem ipsum dolor sit amet, consectetur adipiscing elit. "
"Sed non risus. "
"Suspendisse lectus tortor, dignissim sit amet, "
"adipiscing nec, utilisez sed sin dolor."
)

right = (
"Morbi venenatis, felis nec pretium euismod, "
"est mauris finibus risus, consectetur laoreet "
"sem enim sed arcu. Maecenas sit amet eleifend sem. "
"Nullam ac libero metus. Praesent ac finibus nulla, vitae molestie dolor."
" Aliquam vestibulum viverra nisl, id porta mi viverra hendrerit."
" Ut et porta augue, et convallis ante."
)

print(sidebyside(left,right,20))
Lorem     |Morbi     
Lorem    |Morbi ven