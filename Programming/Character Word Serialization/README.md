#### This folder contains solution to Character Word Serialization question.

The problem is solved in java programming language. The code can be easily run on terminal window.

#### How to run:-
  1. Just clone the repository as it is.
  2. Open command prompt in the location where the repository is cloned.
  3. Run command >java CharacterTreeSerialization create /csv-file.csv /serialized-output.bin ---- to create the tree of characters and then serialize it and save it to the file-path serialized-output.bin
  4. Run command >java CharacterTreeSerialization load /serialized-ouput.bin ---- to read the serialized file, recreate the character tree and print all the words present in the tree. 

The create function takes an input of array of strings in csv format, and outputs a binary file at location specified in cmd line. The load function loads any binary file created by the create function and prints the strings in the original csv.

