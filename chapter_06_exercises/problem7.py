# 7. Write a program to find out whether a given post is talking about “Harry” or not.
name="Harry"
post=input("Enter your post ")
if name.lower() in post.lower():
    print('This post is talking about "harry"')