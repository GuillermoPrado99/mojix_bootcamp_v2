import streamlit as st

st.title(" 10 Cool Beginner Python Tricks That Will Make Your Life Easier ")
st.header(" Simple but effective tips for every python lovers ")

st.markdown("<h3 style='text-align: center;'> </h3>", unsafe_allow_html=True)

st.write(" The compactness of Python can make a developer's life a lot easier when writing lines and lines of code. But there are some lesser-known Python tricks that can surprise you with their amazing capabilities. ")
st.write(" In today's article, I will discuss 10 Python tips and tricks that will be really helpful for beginners to write more compact code. Knowing these tips and tricks will definitely save you some valuable time. ")

st.markdown("<h3 style='text-align: center;'>. . .</h3>", unsafe_allow_html=True)

st.subheader(" 1. Walrus operator ")
st.write(" The Walrus or := operator is one of the latest additions to python 3.8. It is an assignment operator that lets you assign value to a variable within an expression like conditional statements, loops, etc. ")
st.write(" Example ")
st.write(" If we want to check and print the length of a list: ")
code1 = ''' if(l := len(mylist) > 2)
print(l) '''
st.code(code1, language='python')
st.write(" Output ")
res1 = ''' 3 '''
st.code(res1, language='python')

st.subheader(" 2. Splitting a string ")
st.write(" If you want to split the components of a string into a list you can do that easily using the split() function in python. This will make the string operations a lot easier! ")
st.write(" Example ")
code2 = ''' string = "hello world"
string.split() '''
st.code(code2, language='python')
st.write(" Output ")
res2 = ''' ['hello', 'world'] '''
st.code(res2, language='python')

st.subheader(" 3. Reversing a string ")
st.write(" If you want to reverse a given string, you can do that with only one line of code using the negative indexing of the string. ")
st.write(" Example ")
code3 = ''' str="hello world!"
a=str[::-1]
print(a) '''
st.code(code3, language='python')
st.write(" Output ")
res3 = ''' !dlrow olleh '''
st.code(code3, language='python')

st.subheader(" 4. Merging two dictionaries ")
st.write(" This amazing trick will help you merge two dictionaries with just 1 line of code. We just need to use ** in front of the name of the two dictionaries like below two merge them into a single dictionary: ")
st.write(" Example ")
code4 = ''' d1 = {"a": 10, "b":20}
d2 = {"c": 30, "d":40}
d3 = {**d1, **d2}
print(d3) '''
st.code(code4, language='python')
st.write(" Output ")
res4 = ''' {'a': 10, 'b': 20, 'c': 30, 'd': 40} '''
st.code(res4, language='python')

st.subheader(" 5. The zip() function ")
st.write(" The zip() function in python can make your life a lot easier when working with lists and dictionaries. It is used to combine several lists of the same length. ")
st.write(" Example ")
code5 = ''' colour = ["red", "yellow", "green"]
fruits = ['apple', 'banana', 'mango']
for colour, fruits in zip(colour, fruits):
print(colour, fruits) '''
st.code(code5, language='python')
st.write(" Output ")
res5 = ''' red apple
yellow banana
green mangotext '''
st.code(res5, language='python')
st.write(" The zip() function can also be used for combining two lists into a dictionary. This method can be really helpful while grouping data from the list. ")
st.write(" Example ")
c5 = ''' students = ["Rajesh", "kumar", "Kriti"]
marks = [87, 90, 88]
dictionary = dict(zip(students, marks))
print(dictionary) '''
st.code(c5, language='python')
st.write(" Output ")
r5 = ''' {'Rajesh': 87, 'kumar': 90, 'Kriti': 88} '''
st.code(r5, language='python')

st.subheader(" 6. Assigning multiple list values to a variable ")
st.write(" If you want to assign some specific values of a list to a variable and all the remaining values to another variable in a list format, you can use the following technique: ")
st.write(" Example ")
code6 = ''' mylist = [1,2,3,4,5]
a,*b = mylist
print(f"a =",a)
print(f"b =",b) '''
st.code(code6, language='python')
st.write(" Output ")
res6 = ''' a = 1
b = [2, 3, 4, 5] '''
st.code(res6, language='python')
st.write(" This process is also called list unpacking and you can apply this method for more than 2 variables also! ")

st.subheader(" 7. Remove duplicate list items ")
st.write(" Do you have duplicate items in your list which you want to remove? You can do that with only one line of code using the set() function. ")
st.write(" Example ")
code7 = ''' mylist = [1,1,1,2,2,3,3,4,4,5,6,7,7,8,9]
newlist = set(mylist)
print(newlist) '''
st.code(code7, language='python')
st.write(" Output ")
res7 = ''' {1, 2, 3, 4, 5, 6, 7, 8, 9} '''
st.code(res7, language='python')

st.subheader(" 8. Lambda function ")
st.write(" If you need a function that is not very complicated, it can be done easily in one line using lambda. They are also called anonymous functions and are used heavily in data science and web development. ")
st.write(" Example ")
st.write(" Let's say you want to write a function to multiply two numbers. Instead of writing a conventional function, you can do that in one line using : ")
code8 = ''' mul = lambda a,b: a*b
mul(5,6) '''
st.code(code8, language='python')
st.write(" Output ")
res8 = ''' 30 '''
st.code(res8, language='python')

st.subheader(" 9. Swapping variable value ")
st.write(" One of the first programs that we learn while learning about variables is swapping the values of two variables. In python you can achieve that with one line of code: ")
st.write(" Example: ")
code9 = ''' a = 100
b = 200
a,b = b,a
print(f'a = ',a)
print(f'b = ',b) '''
st.code(code9, language='python')
st.write(" Output: ")
res9 = ''' a = 200
b = 100 '''
st.code(res9, language='python')

st.subheader(" 10. Use a password in your code ")
st.write(" This python trick is amazing for securing your code with a password. We will use the getpass() function from the library getpass which encodes your input. This will prevent anyone from running the code without a password. Isn’t that cool! ")
st.write(" Example ")
code10 = ''' from getpass import getpass
password = getpass("password: ")
if password == "abcd":
    print("welcome strnger!")
else:
    print("wrong password") '''
st.code(code10, language='python')
st.write(" Output ")
res10 = ''' password: **** [abcd]
Welcome stranger!
Password: **** [abdc]
Wrong password '''
st.code(res10, language='python')
st.write(" Here is a book on Python programming that I would definitely recommend for all beginners. ")

st.markdown("<h3 style='text-align: center;'>. . .</h3>", unsafe_allow_html=True)

st.subheader(" Conclusion ")
st.write(" These were a few amazing Python tips and tricks which will make your work a lot easier while coding. There are many more shortcuts like these that you can explore from the official documentation or any other website. ")
st.write(" Note: This article contains an affiliate link. This means that if you click on it and choose to buy the resource I linked above, a small portion of your subscription fee will go to me. ")
st.write(" However, the recommended resource is experienced by me and helped me in my data science career journey. ")

st.markdown("<h3 style='text-align: center;'>. . .</h3>", unsafe_allow_html=True)

st.write(" Before you go… ")
st.write(" If you liked this article and want to stay tuned with more exciting articles on Python & Data Science — do consider becoming a medium member by clicking here https://pranjalai.medium.com/membership. ")
st.write(" Please do consider signing up using my referral link. In this way, the portion of the membership fee goes to me, which motivates me to write more exciting stuff on Python and Data Science. ")
st.write(" Also, feel free to subscribe to my free newsletter: Pranjal’s Newsletter. ")

st.caption(" Thanks to Elliot Gunn ")
