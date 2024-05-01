from flask import Flask, render_template, url_for, jsonify, request, redirect, session
from output_chaser import tests_operator
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(248)
a = {"root": "pass"}
b = {}


with open("results.txt") as texter:
    bk = list(map(lambda x: x.strip("\n"), texter.readlines()))
    b = {}
    for i in bk:
        if i == "":
            break
        for n, j in enumerate(i.split()):
            if j.isdigit() or j == "-1" and n != 0:
                break
        s, k = " ".join(i.split()[:n]), list(map(int, i.split()[n:]))
        cs = {}
        for j in range(1, 25):
            cs[j] = k[j-1]
        b[s] = cs
    
with open("users.txt") as texter:
    bk = list(map(lambda x: x.strip("\n"), texter.readlines()))

    for i in bk:
        if i == "":
            break
        i = i.split()
        a[" ".join(i[:-1])] = i[-1]


@app.route('/')
def hi():
    return redirect("http://localhost:5000/login/", code=302)



@app.route('/login/', methods=['post', 'get'])
def login():
    message = ''
    message1 = ''
    if request.method == 'POST':
        username = request.form.get('username')  # запрос к данным формы
        password = request.form.get('password')
        username1 = request.form.get('username1')  # запрос к данным формы
        password1 = request.form.get('password1')
        if (username is not None and password is not None):
            if username in a.keys() and password == a[username]:
                message = "Correct username and password"
                return redirect(f"http://localhost:5000/{username}", code=302)
            else:
                message = "Wrong username or password"
        elif (username1 is not None and password1 is not None):
            if username1 not in a.keys():
                a[username1] = password1
                with open("users.txt", "w") as w:
                    for i in a.items():
                        w.write(i[0] + " " + i[1] + "\n")
                b[username1] = {}
                for i in range(1, 25):
                    b[username1][i] = -1
                print(b)
                with open("results.txt", 'w') as f:
                    for i in b.items():
                        s, k = i[0], i[1]
                        xxx = []
                        for i in k.values():
                            xxx.append(int(i))
                        st = " ".join(list(map(str, xxx)))
                        f.write(s + " " + st)
                        f.write('\n')
            else:
                message1 = "Already existing user"
            return redirect(f"http://localhost:5000/{username1}", code=302)


    return render_template("login.html", message=message, message1=message1)

@app.route('/<username>', methods=['post', 'get'])
def main(username):
    global a, b
    results = b[username]
    if request.method == "POST":
        code = request.form.get('useless_text1')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test1.py", "tests_1.txt")
            b[username][1] = max(result, b[username][1])
            print(result, b[username][1], max(result, b[username][1]))
            print()

        code = request.form.get('useless_text2')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test2.py", "tests_2.txt")
            b[username][2] = max(result, b[username][2])

        code = request.form.get('useless_text3')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test3.py", "tests_3.txt")
            b[username][3] = max(result, b[username][3])

        code = request.form.get('useless_text4')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test4.py", "tests_4.txt")
            b[username][4] = max(result, b[username][4])

        code = request.form.get('useless_text5')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test5.py", "tests_5.txt")
            b[username][5] = max(result, b[username][5])

        code = request.form.get('useless_text6')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test6.py", "tests_6.txt")
            b[username][6] = max(result, b[username][6])

        code = request.form.get('useless_text7')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test7.py", "tests_7.txt")
            b[username][7] = max(result, b[username][7])

        code = request.form.get('useless_text8')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test8.py", "tests_8.txt")
            b[username][8] = max(result, b[username][8])

        code = request.form.get('useless_text9')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test9.py", "tests_9.txt")
            b[username][9] = max(result, b[username][9])

        code = request.form.get('useless_text10')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test10.py", "tests_10.txt")
            b[username][10] = max(result, b[username][10])

        code = request.form.get('useless_text11')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test11.py", "tests_11.txt")
            b[username][11] = max(result, b[username][11])

        code = request.form.get('useless_text12')
        print(code)
        if code != None and code.strip() != "":
            result = tests_operator(code, "good_test12.py", "tests_12.txt")
            b[username][12] = max(result, b[username][12])
        print()
        print(result, b)
    if request.method != "GET":
        with open("results.txt", 'w') as f:
            for i in b.items():
                s, k = i[0], i[1]
                xxx = []
                for i in k.values():
                    xxx.append(int(i))
                st = " ".join(list(map(str, xxx)))
                f.write(s + " " + st)
                f.write('\n')
    results = b[username]
    results[-1] = username
    return render_template("ez_1.html", results=results)

app.run()
