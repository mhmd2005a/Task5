# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

try:

    height = float(input("Enter your height"))
    width = float(input("Enter your height"))
    height_and_width=height*width
    if height_and_width<0:
      print("invalid input ,Notfound area (-)")

    else:
      print(height_and_width)

except:
   print("invalid input")

try:
 first_rib=float(input("Enter first_rib"))
 second_rib=float(input("Enter second_rib"))
 third_rib = float(input("Enter third_rib"))
 four_rib = float(input("Enter four_rib"))
 rectangel=(first_rib+second_rib+third_rib+four_rib)
 if rectangel < 0:
       prtint("invaled Input(-)")
 else:
       print(rectangel)

except:
    print("invaled Input,NOtfound area")

my_list = []
my_dic = {
        my_list.append("Name") : my_list.append("Ahamed"),
        my_list.append("age") :  my_list.append("23"),
        "dic2": {
         my_list.append ("city") : my_list.append("Gaza"),
            my_list.append("Gender"):my_list.append ("Male")
        }
}
print(my_list)