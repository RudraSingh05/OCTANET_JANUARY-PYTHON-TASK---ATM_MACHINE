import mysql.connector

mydb=mysql.connector.connect (host='localhost', user='root')
mycursor=mydb.cursor()

mycursor.execute ("CREATE DATABASE IF NOT EXISTS ATM_MACHINE") 
mycursor.execute("USE ATM_MACHINE")
mn="CREATE TABLE IF NOT EXISTS RECORDS (ACCONT_NO INT(4) PRIMARY KEY, PASSWORD INT(3), NAME VARCHAR(20), CR_AMT INT DEFAULT (0), WITHDRAWL INT DEFAULT(0), BALANCE INT DEFAULT(0))"
mycursor.execute(mn)

conn=mysql.connector.connect (host='localhost', user='root', database='ATM_MACHINE')
cl=conn.cursor()
print("=====================================================")
print("------------------WELCOME TO OUR ATM-----------------")
print("=====================================================")
print("1.To create account")
print("2.To login")
print("3.Exit")
print("=====================================================")
op=int(input("Enter your choice:"))
print("=====================================================")
if op==1:
    c="y"
    while c=="y":
        m=int(input("Enter a 4 digit number as account number:"))
        cb="select * from records where ACCONT_NO={}".format(m)
        cl.execute(cb)
        d=cl.fetchall()
        data=cl.rowcount
        if data==1: 
            print("=====================================================")
            print("This account number already exists:")
            c=input("Do you want to continue y/n -")
            print("=====================================================")
            if c=="y":
                continue
            else:
                print("Thank you.")
                print("PLEASE CLOSE THIS FILE BEFORE EXITING")
                print("Visit again")
                print("=====================================================")
        else:
            name=input("Enter your name:")
            passw=int(input("Enter your pass word:"))
            ab="insert into records (ACCONT_NO, PASSWORD, NAME) values ({}, {}, '{}')".format(m,passw, name)
            print("=====================================================")

            cl.execute(ab)
            conn.commit()
            print("Account sucessfully created")
            print("The minimum balance is 1000 ")
            print("=====================================================")

            s=int(input("Enter the money to be deposited: "))
            print("=====================================================")

            sr="update records set CR_AMT={} where ACCONT_NO={}".format(s,m)
            cl.execute(sr)
            conn.commit()
            ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(m)
            cl.execute (ef)
            conn.commit()
            print("sucessfully deposited")
            print(" Thank you")
            print(" PLEASE CLOSE THIS FILE BEFORE EXITING")
            print("Visit again")
            break

if op==2:
    y="y"
    while y=="y":
        acct=int(input("Enter your account number:"))
        cb="select * from records where ACCONT_NO={}".format(acct)
        cl.execute(cb)
        cl.fetchall()
        data=cl.rowcount
        if data==1:
            pas=int(input("Enter your password :"))
            print("=====================================================")

            e="select password from records where ACCONT_NO={}".format(acct)
            cl.execute(e)
            a=cl.fetchone()
            d=list(a)
            if pas==d[0]:
                print("Successfully Logged In")
                print("1. Depositng money")
                print("2. withdrawing money")
                print("3. Transfering money")
                print("4. Checking balance")
                print("=====================================================")
                r=int(input("Enter your choice:"))
                print("=====================================================")

                if r==1:
                    amt=int(input("Enter the money to be deposited:"))
                    print("=====================================================")
                    sr="update records set CR_AMT=CR_AMT + {} where ACCONT_NO={}".format(amt, acct)
                    cl.execute(sr)
                    conn.commit()
                    ef="update records set balance=cr_amt-withdrawl where ACCONT_NO={}".format(acct)
                    cl.execute (ef)
                    conn.commit()
                    print("sucessfully deposited")

                    t=input("Do you want to continue y/m - ")
                    print("=====================================================")

                    if t=='y':
                        continue
                    else:
                        print("Thank You")
                        print("please close the file before exiting")

                if r==2:
                    amt=int(input("Enter the amount to withdraw : "))
                    ah="select BALANCE from records where ACCONT_NO={}".format(acct)
                    cl.execute (ah)
                    m=cl.fetchone ()
                    if amt >m[0]:
                        print("You are having less than", amt)
                        print("Please try again")
                        print("=====================================================")
                        
                    else:
                        sr="update records set balance = balance - {} where ACCONT_NO={}".format(amt, acct) 
                        ed="update records set WITHDRAWL = {} where ACCONT_NO={}".format(amt, acct)
                        cl.execute(ed)
                        cl.execute(sr)
                        conn.commit()
                        print("Please collect the amount")
                    y=input("do you want to continue y/n -")
                    if y=="y":
                        continue
                    else:
                        print("Thank you")
                        print("PLEASE CLOSE THIS FILE BEFORE EXITING")

                if r==3:
                    act = int(input("Enter the account number to be transferred: "))
                    cb = "SELECT * FROM records WHERE ACCONT_NO = {}".format(acct)
                    cl.execute (cb)
                    cl.fetchall ()
                    data = cl.rowcount
                    if data==1:
                        print(act, "number exists")
                        m = int(input("Enter the money to be transferred: "))
                        ah="SELECT BALANCE FROM records WHERE ACCONT_NO = {}".format(acct)
                        cl.execute(ah)
                        c = cl.fetchone()
                        if m>c[0]:
                            print("You have less than", m)
                            print("Please try again")
                        else:
                            av = "UPDATE records SET BALANCE = BALANCE - {} WHERE ACCONT_NO = {}".format(m, acct)
                            cv = "UPDATE records SET BALANCE = BALANCE + {} WHERE ACCONT_NO = {}".format(m, acct)
                            w = "UPDATE records SET WITHDRAWL = WITHDRAWL + {} WHERE ACCONT_NO = {}".format(m, acct)
                            t = "UPDATE records SET CR_AMT = CR_AMT + {} WHERE ACCONT_NO = {}".format(m, acct)
                            cl.execute(av)
                            cl.execute(cv)
                            cl.execute(w)
                            cl.execute(t)
                            conn.commit()
                            print("Successfully transferred")
                            y = input("Do you want to continue? (y/n): ")
                            if y=="y":
                                continue
                            else:
                                print("Thank you")
                                print("PLEASE CLOSE THIS FILE BEFORE EXITING")

                if r == 4:
                    ma = "SELECT BALANCE FROM records WHERE ACCONT_NO = {}".format(acct)
                    cl.execute(ma)
                    k = cl.fetchone()

                    print("Balance in your account = ", k[0])
                    print("=====================================================")

                    y = input("Do you want to continue? (y/n): ")
                        
                    if y == "y":
                        continue
                    else:
                        print("Thank you")
                        print("PLEASE CLOSE THIS FILE BEFORE EXITING")

            else:
                print("wrong password")
                print("=====================================================")
                y=input("do you want to continue y/n -")
                if y=="y":
                    continue
                else:
                    print("Thank you")
                    print("PLEASE CLOSE THIS FILE BEFORE EXITING")
        else:
            print("account does not exists")

if op==3:
    print("exiting")
    print("please close this file before exiting")
    cl.close()