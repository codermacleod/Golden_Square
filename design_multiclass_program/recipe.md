# Diary Entry/Tasks/Contacts Multi-Class Planned Design Recipe for 

## 1. Describe the Problem

Keep a regular diary

Read my past diary entries

Select diary entries to read based on time(t) and reading speed(rs)

Keep a todo list tracker

List all of the mobile phone numbers in all my diary entries

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
CLASSES--------------->
    Diary()
        Add()
        ReadEntries()
        ValidReadingMaterial()
        GetPhoneNumbers()
    DiaryEntry() 
    ToDoList()
        Todo_Complete()
        Todo_Incomplete()





```

_Also design the interface of each class in more detail._

```python
class Diary():
    def __init__(self):
        self.entries = []

    def add(self,diary_entry):
        #return nothing
        #adds to diary entries
        pass

    def read_entries(self,diary_entry):
        return all entries

    def GetPhoneNumbers():
    #return all phone numbers from diary entries
    pass


class DiaryEntry():
    def __init__(self,title,contents)
    self.title = title
    self.contents = contents
    #return nothing
    

class ToDoList():
    def complete():
        #return list of all completed tasks
    def incomplete():
        # return list of all incomplete tasks



```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Adding an instance of DiaryEntry to Diary list 
"""
dans_diary=Diary()
e1 = DiaryEntry('entry 1', 'one two three')
dans_diary.add(e1)
dans_diary.read_entries()=[e1] 


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE
"""
Initial creation of Diary instance should return empty list of diary entries
"""
dans_diary=Diary()
dans_diary.read_entries=[]

"""
Initial creation of DiaryEntry should assign title and diary entry properties to instance
"""
e1=DiaryEntry('entry 1','one two three')
e1.title = 'entry 1'
e1.contents = 'one two three'




```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._




