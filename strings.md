1.  In python strings, it's just a sequence of character

    1.1 : we can escape a single quote causing problem is single quoted string using back slash('\')

    ex : name = 'yash\'s world'

    1.2 : mostly use double quotes in string

    1.3 : functions and methods in python are the same thing , it's just method is function that belongs to an object.

2.  string methods :
    example : message = "hello world";

                2.1 print(len(message)) : use to find length of string.

                example : message = "Hello world"
                print(message[0:len(message)])
                the message[firstIndex : index upto string needs to printed] -
                first Index = is inclusive
                last Index = exclusive

                2.3 strings are 0-indexed

                2.4 message = "HELLO WORLD"
                print(message.lower())

                output - hello world

                2.5 message = "hello world"
                print(message.upper())

                output -HELLO WORLD

                2.6 count method ➡️

                2.6.1 : if exist - number of occurences will be returned

        example ->
        name = "hakuna matata"
        <!-- print(name.count("a")) -->
        output - 5 ("a" occurred 5 times in name)

                2.6.2 : if doesn't exist it will return 0

        example ->
        name = "hakuna matata"
        <!-- print(name.count("l")) -->
        output - 0 ("l" haven't appeared a single time in name)

                2.7 find() method ⬇️
                2.7.1 : if exist it will return the starting index of the arguement passed that occurred in object

        example ->
        message = "Hello world"
        <!-- print(message.find("o")) -->
        output - 4 (the starting index where "o" occured for the first time)

                2.7.2 : if doesn't exists it will return -1 instead of any index.
        example ->
        message = "Hello world"
        <!-- print(message.find("i")) -->
        output -> -1 ("i" did not appeared a single time in object message so message.fin() returned -1)

               2.8 replace() method ⬇️: use to replace the first argument passed with whatever in the second argument into the object
        example ->
        message = "hello world"
        message = message.replace('world', 'universe')
        print(message)
        output - hello universe

3.  STRING CONCATENATION ➡️

greetings = 'Hello master'
name = 'yash'
message = greetings + ', ' + name
print(message)
print(greetings + ', ' + name)

OUTPUTS :
Hello master, yash
Hello master, yash

4. FORMATTED STRINGS :

greetings = "Hello, master"
name = "yash"

message = '{} {}'.format(greetings, name)
print(message)

output : Hello, master yash

5. f - strings

greetings = "Hello master"
name = 'yash'
message = f'{greetings}, {name}'
print(message)
print(f'{greetings}, {name}')

OUTPUT ->
Hello master, yash
Hello master, yash
