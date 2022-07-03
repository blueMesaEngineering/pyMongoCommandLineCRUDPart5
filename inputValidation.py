from curses.ascii import isalpha
import datetime
import pprint
import exceptions
import sys


#****************************************************************************************************
# Function Name:      validateName
# In:                 input
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        
#****************************************************************************************************
def validateName(input):
  try:
    if(len(input) > 0):
      if(len(input) < 41):
        if(not input.isspace()):
          if(input[0].isupper()):
            return("true")
          else:
            raise exceptions.nameNotCapitalizedError(input)
        else:
          print("input.isspace(): ")
          print(input.isspace())
          raise exceptions.nameContainsSpaceError(input)
      else:
        raise exceptions.nameTooManyCharactersError(input)
    else:
      raise exceptions.nameTooFewCharactersError(input)
  except:
    print("The error ", sys.exc_info()[0], " occurred.")
    return("false")
  
  
#****************************************************************************************************
# Function Name:      validatePostTitle
# In:                 input
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        
#****************************************************************************************************
def validatePostTitle(input):
  try:
    if(len(input) > 0):
      if(len(input) < 41):
        if(input[0].isupper()):
          return("true")
        else:
          raise exceptions.nameNotCapitalizedError(input)
      else:
        raise exceptions.nameTooManyCharactersError(input)
    else:
      raise exceptions.nameTooFewCharactersError(input)
  except:
    print("The error ", sys.exc_info()[0], " occurred.")
    return("false")
  
  
#****************************************************************************************************
# Function Name:      validatePostBody
# In:                 input
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        
#****************************************************************************************************
def validatePostBody(input):
  try:
    if(len(input) > 0):
      if(len(input) < 301):
        if(input[0].isupper()):
          return("true")
        else:
          raise exceptions.nameNotCapitalizedError(input)
      else:
        raise exceptions.nameTooManyCharactersError(input)
    else:
      raise exceptions.nameTooFewCharactersError(input)
  except:
    print("The error ", sys.exc_info()[0], " occurred.")
    return("false")


#****************************************************************************************************
# Function Name:      validate
# In:                 input, type
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        
#****************************************************************************************************
def validate(input, type):
  if(type == "name"):
    result = validateName(input)
    return(result)
  elif(type == "title"):
    result = validatePostTitle(input)
    return(result)
  elif(type == "body"):
    result = validatePostBody(input)
    return(result)
    