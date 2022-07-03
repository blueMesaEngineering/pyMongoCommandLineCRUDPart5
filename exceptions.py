# Reference: https://www.programiz.com/python-programming/user-defined-exception

#****************************************************************************************************
# Function Name:      nameNotCapitalizedError
# In:                 Exception
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Input is not capitalized.
#****************************************************************************************************
class nameNotCapitalizedError(Exception):
  # """Exception raised for a name not having a first letter capitalized.
  
  # Attributes:
  #   input:    User input in the form of a user name. 
  #   message:  Explanation of the error.
  # """
  
  def __init__(self, input, message = "This name is not valid input. The first letter is not capitalized."):
    self.input = input
    self.message = message
    super().__init__(self.message)
    

#****************************************************************************************************
# Function Name:      nameTooManyCharactersError
# In:                 Exception
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Name is longer than 40 characters.
#****************************************************************************************************
class nameTooManyCharactersError(Exception):
  # """Exception raised for a name not having a first letter capitalized.
  
  # Attributes:
  #   input:    User input in the form of a user name. 
  #   message:  Explanation of the error.
  # """
  
  def __init__(self, input, message = "This name is not valid input. It is longer than 40 characters."):
    self.input = input
    self.message = message
    super().__init__(self.message)
    

#****************************************************************************************************
# Function Name:      nameTooFewCharactersError
# In:                 Exception
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Name is empty string.
#****************************************************************************************************
class nameTooFewCharactersError(Exception):
  # """Exception raised for a name not having a first letter capitalized.
  
  # Attributes:
  #   input:    User input in the form of a user name. 
  #   message:  Explanation of the error.
  # """
  
  def __init__(self, input, message = "This name is not valid input. It is a null string."):
    self.input = input
    self.message = message
    super().__init__(self.message)
    

#****************************************************************************************************
# Function Name:      nameContainsSpaceError
# In:                 Exception
# Out:                N/A
# In/Out:             N/A
# Returns:            N/A
# Description:        Name contains a space character.
#****************************************************************************************************
class nameContainsSpaceError(Exception):
  # """Exception raised for a name not having a first letter capitalized.
  
  # Attributes:
  #   input:    User input in the form of a user name. 
  #   message:  Explanation of the error.
  # """
  
  def __init__(self, input, message = "This name is not valid input. It contains at least one space character."):
    self.input = input
    self.message = message
    super().__init__(self.message)