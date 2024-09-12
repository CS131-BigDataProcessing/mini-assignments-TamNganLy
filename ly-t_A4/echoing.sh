# Activity 1
echo "Activity 1"
echo "The time and date are:" 
date
echo "Let's see who is logged into the system:"
who
echo "For $USER, the home directory is $HOME."
printf "\n"

# Activity 2
name="Tam Ly"
money="10"
echo "Activity 2"
echo "My name is $name and I have \$$money in my wallet."
printf "\n"

# Activity 3
mathvar1=$[1+5]
mathvar2=$[mathvar1*20]
mathvar3=10
mathvar4=$[$mathvar1*($mathvar2+$mathvar3)]
echo "Activity 3"
echo "Varibale 1 is $mathvar1. Variable 2 is $mathvar2. Using $mathvar3 for Variable 3, our final Variable 4 is $mathvar4."
printf "\n"

# Activity 4
floating=$(echo "scale=3; 4.5/1.7" | bc)
echo "Activity 4"
echo "Our floating varibale is $floating"
printf "\n"
