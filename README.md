# Python-Learning

# 1.Why choose Python?
    - Designed for clear, logical code that is easy to read and learn
    - Lots of existing libraries and frameworks written in python allowing users to apply Python to a wide variety of tasks.
    - Focuses on optimizing developer time, rather than a computer's proccessing time.
    - Great documentation online:
        docs.python.org/3;

# 1.What can you do with Python?

    - Create website:
        Use web framework such as Django and flask to handle the backend of a website and user data
        Create interactive dashboards for users

    - Automate simple tasks:
        Search for files and editing them 
        Scraping information from a website
        Reading and editing excel files
        Work with PDFs
        Automate emails and text messages 
        Fill out forms
    
    - Data Science and machine Learning
        Analyze large data files
        Create visualizations
        Perform machine learning tasks
        Create and runf predictive algorithms

# 3 String - FAQ
    1. Are string mutable?
        String not mutable(meaning you can't use indexing to change individual elements of a string)
    2. How do i create comments in my code?
        You can use the hashtag to create a comment in your code

# 4 Print Formatting FAQs
    1. I imported print from the_future_module, now print isn't working. what happened?
        This's because once you import from the_feature_module in Python 2.7. a print statement will no longer work, and print must then use a print() funtion. meaning that you must use print('Whatever you were going to print') or if you are using some formatting: 
        print('this is a string with an {p}'.format(p='insert'))
        the_future_module allows you to use Python3 functionality in a Python2 environment, but some functionality is overwritten(such as the print statement, or classic division when you import division).

        Since we are using Jupyter Notebooks, once you so the import alll cells will require the use if the print() function. you'll have to restart Python or start a new notebook to regain the old functionality back.  

# 5.Objects and data structures Assessment Test (Numners, Strings, Lists, Tuples, Dictionaries)
    - Dictionaries: Using keys and indexing, grab the "hello" from the following dictionaries:
        d = {'simple_key': 'hello'}
        # grab "hello"
        d['simple_key']
        Can you sort a Dictionaries? why or why not?
        -> No! Because normal Dictionaries are mappings not a sequence
    - Tuples: 
        - What is the major difference between tuples and lists?
            -> Tuple're immutable.
        - How do you create a Tuples?
            -> t = (1, 2, 3)
    - Sets: 
        - What's unique about a Set?
            -> They don't  allow for duplicate items! (like javascript)
        - Use set to find the unique values of the list
            list = [1, 2, 3, 4, 5, 5, 5, 6, 10]
            set(list)  # 1 , 2, 3, 5, 6, 10 remove duplicate values.
                