from pickle import TRUE
from select import select
from venv import create
# from psycopg2 import cursor
import pymongo
import datetime
import pprint
from pymongo import MongoClient
from bson.objectid import ObjectId
from sqlalchemy import false, true

from inputValidation import validate

client = MongoClient('mongodb://localhost:27017/')
db = client.test_database
collection = db.test_collection
posts = db.posts


#****************************************************************************************************
# Function Name:      createPost
# In:                 posts
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Creates a post consisting of a user first name, a user last name, a message 
#                       title, and a message, and writes it to the MongoDB, test_database.
#****************************************************************************************************
def createPost(posts):
  print("\nCreate Post")
  authorFirstName = input("Enter author first name: ").strip()
  result = validate(authorFirstName, "name")
  if result == "false":
    print("Error occurred. Post not successful!")
    return
  authorLastName =  input("Enter author last name: ").strip()
  result = validate(authorLastName, "name")
  if result == "false":
    print("Error occurred. Post not successful!")
    return
  postTitle = input("Enter post title: ").strip()
  result = validate(postTitle, "title")
  if result == "false":
    print("Error occurred. Post not successful!")
    return
  postBody = input("Enter post body: ").strip()
  result = validate(postBody, "body")
  if result == "false":
    print("Error occurred. Post not successful!")
    return
  print("")
  post = {"author first name": authorFirstName, "author last name": authorLastName, "title": postTitle, "text": postBody, "date": datetime.datetime.utcnow()}
  post_id = posts.insert_one(post).inserted_id
  pprint.pprint(posts.find_one({"_id": post_id}))
  print("\nPost successful!")


#****************************************************************************************************
# Function Name:      printReadPostSubMenu
# In:                 N/A
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints submenu.
#****************************************************************************************************
def printReadPostSubMenu():
  print("\nRead")
  print("1 - Read by author first name")
  print("2 - Read by author last name")
  print("3 - Read by post title")
  print("4 - Exit Read")


#****************************************************************************************************
# Function Name:      readPost
# In:                 posts
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Takes a collection, posts, finds posts by parameter, displays posts.
#****************************************************************************************************
def readPost(posts):
  printReadPostSubMenu()
  readChoice = input("\nEnter a selection: ")
  while readChoice != "4":
    if readChoice == "1":
      authorFirstName = input("Enter author first name: ")        # To do: validate input here.
      cursor = posts.find({"author first name": authorFirstName})
      readPostDisplayResults(cursor, "read")
      break
    elif readChoice == "2":
      authorLastName = input("Enter author last name: ")          # To do: validate input here.
      cursor = posts.find({"author last name": authorLastName})
      readPostDisplayResults(cursor, "read")
      break
    elif readChoice == "3":
      postTitle = input("Enter post title: ")                     # To do: validate input here.
      cursor = posts.find({"title": postTitle})
      readPostDisplayResults(cursor, "read")
      break
    elif readChoice == "4":
      break
    else:
      break


#****************************************************************************************************
# Function Name:      updateOrDeletePost
# In:                 post, flag
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Updates or deletes a post based on the setting of the 'flag' parameter.
#****************************************************************************************************
def updateOrDeletePost(post, flag):
  print("")
  pprint.pprint(post)
  print("")
  if flag == "read":
    return                    # Nothing to do. Return.
  elif flag == "update":
    updatePost = ""
    while ((updatePost != "Y") or (updatePost != "n")):
      updatePost = input("Update this post [Y/n]? Default is [n].")
      if updatePost == "Y":
        updatePostByID(post, post["_id"])
        break
      else:
        break
  elif flag == "delete":
    deletePost = ""
    while ((deletePost != "Y") or (deletePost != "n")):
      deletePost = input("Delete this post [Y/n]? Default is [n].")
      if deletePost == "Y":
        deletePostByID(post, post["_id"])
        break
      else:
        break


#****************************************************************************************************
# Function Name:      readPostDisplayResults
# In:                 cursor, flag
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Retrieves queried data from MongoDB and displays to user.
#****************************************************************************************************
def readPostDisplayResults(cursor, flag):
  selectedPosts = []
  selectedPostIDs = []
  for post in cursor:
    selectedPosts.append(post)
    selectedPostIDs.append(post["_id"])
  if len(selectedPosts) > 1:
    viewPosts = ""
    while ((viewPosts != "Y") or (viewPosts != "n")):
      viewPosts = "n"
      viewPosts = input("\nYour query returned more than one post. Would you like to view the posts [Y/n]?")
      if viewPosts == "Y":
        for post in selectedPosts:
          updateOrDeletePost(post, flag)
        break
      else:
        break
      
  else:
    post = selectedPosts
    updateOrDeletePost(post, flag)


#****************************************************************************************************
# Function Name:      printUpdatePostSubMenu
# In:                 N/A
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints submenu.
#****************************************************************************************************
def printUpdatePostSubMenu():
  print("\nUpdate")
  print("1 - Update by author first name")
  print("2 - Update by author last name")
  print("3 - Update by post title")
  print("4 - Exit Update")
  

#****************************************************************************************************
# Function Name:      updatePost
# In:                 posts
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Takes a collection, posts, finds posts by parameter, displays posts, requests
#                       user input regarding which post to update, updates or does not update a post
#                       based on input from the user.
#****************************************************************************************************
def updatePost(posts):
  printUpdatePostSubMenu()
  updateChoice = input("\nEnter a selection: ")
  while updateChoice != "4":
    if updateChoice == "1":
      authorFirstName = input("Enter author first name: ")        # To do: validate input here.
      cursor = posts.find({"author first name": authorFirstName})
      readPostDisplayResults(cursor, "update")
      break
    elif updateChoice == "2":
      authorLastName = input("Enter author last name: ")          # To do: validate input here.
      cursor = posts.find({"author last name": authorLastName})
      readPostDisplayResults(cursor, "update")
      break
    elif updateChoice == "3":
      postTitle = input("Enter post title: ")                     # To do: validate input here.
      cursor = posts.find({"title": postTitle})
      readPostDisplayResults(cursor, "update")
      break
    elif updateChoice == "4":
      break


#****************************************************************************************************
# Function Name:      printupdatePostByIDSubMenu
# In:                 N/A
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints submenu.
#****************************************************************************************************
def printupdatePostByIDSubMenu():
  print("1 - Update author first name")
  print("2 - Update author last name")
  print("3 - Update post title")
  print("4 - Update post body")
  print("5 - Exit Update")


#****************************************************************************************************
# Function Name:      printUpdatedPostByID
# In:                 posts, post_id
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints a post.
#****************************************************************************************************
def printUpdatedPostByID(posts, post_id):
  post = posts.find_one({"_id": post_id})
  print("")
  pprint.pprint(post)
  print("\nUpdate successful.")


#****************************************************************************************************
# Function Name:      updatePostByID
# In:                 posts, post_id
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Changes a parameter of a post based on input from the user after retrieving the 
#                       post by ID.
#****************************************************************************************************
def updatePostByID(posts, post_id):
  printupdatePostByIDSubMenu()
  selection = input("\nEnter a selection: ")
  while selection != "5":
    if selection == "1":
      authorFirstName = input("Enter new author first name: ")    # To do: validate input here.
      posts.update_one({"_id": post_id}, { "$set": {"author first name": authorFirstName}})
      printUpdatedPostByID(posts, post_id)
      break
    elif selection == "2":
      authorLastName = input("Enter new author last name: ")      # To do: validate input here.
      posts.update_one({"_id": post_id}, { "$set": {"author last name": authorLastName}})
      printUpdatedPostByID(posts, post_id)
      break
    elif selection == "3":
      postTitle = input("Enter new post title: ")                 # To do: validate input here.
      posts.update_one({"_id": post_id}, { "$set": {"title": postTitle}})
      printUpdatedPostByID(posts, post_id)
      break
    elif selection == "4":
      postBody = input("Enter new post body: ")                   # To do: validate input here.
      posts.update_one({"_id": post_id}, { "$set": {"text": postBody}})
      printUpdatedPostByID(posts, post_id)
      break
    elif selection == "5":
      break


#****************************************************************************************************
# Function Name:      deletePostByID
# In:                 post, post_id
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Deletes a post as designated by user input.
#****************************************************************************************************
def deletePostByID(post, post_id):
  pprint.pprint(post)
  deletePost = "n"
  deletePost = input("Delete this post [Y/n]?")
  if deletePost == "Y":
    posts.delete_one({"_id": post_id})


#****************************************************************************************************
# Function Name:      printDeletePostSubMenu
# In:                 N/A
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints submenu.
#****************************************************************************************************
def printDeletePostSubMenu():
  print("\nDelete")
  print("1 - Delete by author first name")
  print("2 - Delete by author last name")
  print("3 - Delete by post title")
  print("4 - Exit Delete")


#****************************************************************************************************
# Function Name:      deletePost
# In:                 posts
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Deletes a record from MongoDB based on user input.
#****************************************************************************************************
def deletePost(posts):
  printDeletePostSubMenu()
  deleteChoice = input("\nEnter a selection: ")
  while deleteChoice != "4":
    if deleteChoice == "1":
      authorFirstName = input("Enter author first name: ")        # To do: validate input here.
      cursor = posts.find({"author first name": authorFirstName})
      readPostDisplayResults(cursor, "delete")
      break
    elif deleteChoice == "2":
      authorLastName = input("Enter author last name: ")          # To do: validate input here.
      cursor = posts.find({"author last name": authorLastName})
      readPostDisplayResults(cursor, "delete")
      break
    elif deleteChoice == "3":
      postTitle = input("Enter post title: ")                     # To do: validate input here.
      cursor = posts.find({"title": postTitle})
      readPostDisplayResults(cursor, "delete")
      break
    elif deleteChoice == "4":
      break


#****************************************************************************************************
# Function Name:      printDoStuffMainMenu
# In:                 N/A
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Prints menu.
#****************************************************************************************************
def printDoStuffMainMenu():
  print("\nPlease make a selection from 1 to 5: ")
  print("1 - Create Post")
  print("2 - Read Post")
  print("3 - Update Post")
  print("4 - Delete Post")
  print("5 - Exit")


#****************************************************************************************************
# Function Name:      doStuff
# In:                 posts
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Primary logic control function for application.
#****************************************************************************************************
def doStuff(posts):
  choice = "0"
  while choice != "5":
    printDoStuffMainMenu()
    choice = input()
    if choice == "1":
      createPost(posts)
    elif choice == "2":
      readPost(posts)
    elif choice == "3":
      updatePost(posts)
    elif choice == "4":
      deletePost(posts)
    elif choice == "5":
      print("\nExiting...")
      dropDatabase = "n"
      dropDatabase = input("\nDrop database test_database [Y/n]? Default is [n].")
      if dropDatabase == "Y":
        client.drop_database('test_database')
      print("")
      break

doStuff(posts)