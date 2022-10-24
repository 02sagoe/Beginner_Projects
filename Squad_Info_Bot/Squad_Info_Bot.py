# See the Instructions tab

import random

squad5_about = "\n\nThis is Kibo's 5th squad for the 2022 'Try Kibo' cohort. At first glance we thought this would be on eof the most interactive groups, but seems like people have crawlled into thier shells a bit. There has however been showing of cooperation between team members regularly holding study sessions and carrying each other all the way. We hope that the bonds formed will carry on far beyond the peaks of Kibo!\n"

names = ["Kojo S", "Kachisicho I", "James B", "Miriam H"]

about = [
    "Kojo S, 25 years old and 5'8 and born in Ghana. Has persevered through university to aquire his bachelors in Actuarial Science. Is there more for him? I think so beccause the sky is the limit for him",
    "Kachisicho I, 18 year old female who was born and bred in Nigeria. She is currently on the journey of pursuing her chosen career path. Being one of the very few females interested in technolgy,she is working hard to achieve her dreams",
    "James B, a 22 year old Nigerian. He is an undergraduate and has decided to learn how to code. He strongly believes team work is vital and embracing each other helps to caputalise on strengths and not weaknesses",
    "Miriam H, web developer and open to acquiring more skills. Believes that she can do whatever she sets her mind to and is happily living in a world of technology"
]

home_coutry = ["Ghana", "Nigeria", "Nigeria", "Kenya"]

superpowers = [
    "Telepathy",
    "Super Speed",
    "Super Strength",
    "Time Travel",
]

favorite_things = [
    "Football",
    "Travelling",
    "Swimming",
    "Reading",
]

jokes = [
    "When you put a bed in your bedroom \nYou have less bedroom.",
    "Can a kangaroo jump higher than a house? \nOf course, a house doesn’t jump at all.",
    "99.8% people have problems with math. ... \nI’m glad I’m in the remaining 1%.",
    "Many people are shocked when they found out how bad I actually am at this electrician thing.",
    "How can you tell your acne is really starting to get out of hand? - \nThe blind start reading your face.",
    "“Siri, why am I still single?!” - \nSiri activates front camera.",
    "My old aunts would come and tease me at weddings, “Well Sarah? Do you think you’ll be next?” \nWe settled this quickly once I started doing the same to them at funerals."
]

motivational_quotes = [
    "Success is not final; failure is not fatal: It is the courage to continue that counts.",
    "It is better to fail in originality than to succeed in imitation.",
    "Don’t let yesterday take up too much of today.",
    "When we strive to become better than we are, everything around us becomes better too.",
    "Either you run the day or the day runs you.",
    "Take the attitude of a student, never be too big to ask questions, never know too much to learn something new."
]

random_coding_phrases = [
    "Most good programmers do programming not because they expect to get paid or get adulation by the public, but because it is fun to program.",
    "There are two ways of constructing a software design. One way is to make it so simple that there are obviously no deficiencies. And the other way is to make it so complicated that there are no obvious deficiencies.",
    "People think that computer science is the art of geniuses but the actual reality is the opposite, just many people doing things that build on each other, like a wall of mini stones.",
    "To iterate is human, to recurse divine.",
    "Learning to program has no more to do with designing interactive software than learning to touch type has to do with writing poetry",
    "You can’t have great software without a great team, and most software teams behave like dysfunctional families."
]

print("Hi I'm the KS-Chatbot. How can I help you today?")

while True:
    input("\nPress [enter] to continue.")
    print(
        '''\n----------Menu-----------\n\n1. About Squad 5\n\n2. Members in Squad 5\n\n3. Tell me a joke\n\n4. Share a motivational quote\n\n5. Say a random coding phrase\n\n6. Exit\n\n--------------------------\n'''
    )
    print()

    choice = input("Enter your choice: ")

    if choice.isdigit() and int(choice) >= 1 and int(choice) <= 6:
        choice = int(choice)
        if choice == 1:
            print(squad5_about)
        elif choice == 2:
            print("\n----------Names-----------\n")
            for i, name in enumerate(names):
                print(f"{i+1}. {name}\n")
            print("--------------------------\n")
            choice_1 = input("Enter a choice: ")
            # while True:
            if choice_1.isdigit(
            ) and int(choice_1) >= 1 and int(choice_1) <= 4:
                # choice_1 == int(choice_1)
                print(choice_1)
                if int(choice_1) == 1:
                    print(
                        f"\n----------------------{names[0]}--------------------------"
                    )
                    print(
                        "\n----------------------About--------------------------\n"
                    )
                    print(about[0])
                    print(
                        f"\n\n----------------------Profile--------------------------"
                    )
                    print(
                        f"\nCountry: {home_coutry[0]} \nSuper power: {superpowers[0]} \nHobby: {favorite_things[0]}\n\n"
                    )
                elif int(choice_1) == 2:
                    print(
                        f"\n----------------------{names[1]}--------------------------"
                    )
                    print(
                        "\n----------------------About--------------------------\n"
                    )
                    print(about[1])
                    print(
                        "\n\n----------------------Profile--------------------------"
                    )
                    print(
                        f"\nCountry: {home_coutry[1]} \nSuper power: {superpowers[1]} \nHobby: {favorite_things[1]}\n\n"
                    )
                elif int(choice_1) == 3:
                    print(
                        f"\n----------------------{names[2]}--------------------------"
                    )
                    print(
                        "\n----------------------about--------------------------\n"
                    )
                    print(about[2])
                    print(
                        "\n\n----------------------profile--------------------------"
                    )
                    print(
                        f"\nCountry: {home_coutry[2]} \nSuper power: {superpowers[2]} \nHobby: {favorite_things[2]}\n\n"
                    )
                else:
                    print(
                        f"\n----------------------{names[3]}--------------------------\n"
                    )
                    print(
                        "\n----------------------About--------------------------"
                    )
                    print(about[3])
                    print(
                        "\n\n----------------------Profile--------------------------"
                    )
                    print(
                        f"\nCountry: {home_coutry[3]} \nSuper power: {superpowers[3]} \nHobby: {favorite_things[3]}\n\n"
                    )

            else:
                print("\nWrong input. Please try again!\n\n")
        elif choice == 3:
            print()
            print(random.choice(jokes))
            print()
        elif choice == 4:
            print()
            print(random.choice(motivational_quotes))
            print()
        elif choice == 5:
            print()
            print(random.choice(random_coding_phrases))
            print()
        elif choice == 6:
            print()
            print()
            break
    else:
        print("\nWrong input. Please try again!\n\n")
print("Thank you for using the KS-Chatbot")
